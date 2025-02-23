import os
from datetime import datetime
from supabase import create_client
import re
import subprocess
from subprocess import run

# No changes in Supabase setup
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('S_KEY')
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# MAJOR CHANGES in should_update function
def should_update(problem_name, commit_date):
    """
    CHANGED: Now checks for exact duplicate entries (same problem_name AND commit_date)
    instead of just checking the latest commit.
    Returns True only if no exact duplicate exists.
    """
    result = supabase.table('leetcode_questions')\
        .select('*')\
        .eq('question_name', problem_name)\
        .execute()
    
    if not result.data:
        return True
    
    # NEW: Check for exact commit date match
    commit_datetime = datetime.strptime(commit_date, "%Y-%m-%d %H:%M:%S")
    
    for entry in result.data:
        db_date = datetime.strptime(entry['commit_date'], "%Y-%m-%dT%H:%M:%S")
        db_date_formatted = db_date.strftime("%Y-%m-%d %H:%M:%S")
        
        if db_date_formatted == commit_date:
            # Found exact match - don't update
            return False
    
    # No exact match found - should add new entry
    return True

# No changes in get_last_commit_date function
def get_last_commit_date(file_path):
    git_command = f"git log -1 --pretty=format:%cd --date=format:'%Y-%m-%d %H:%M:%S' {os.path.abspath(file_path)}"
    process = subprocess.run(git_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = process.stdout.strip()
    print(f'output - {output}')
    return output

# No changes in extract_difficulty function
def extract_difficulty(readme_contents):
    match = re.search(r'<h3>(Easy|Medium|Hard)</h3>', readme_contents)
    if match:
        return match.group(1)
    else:
        return 'Unknown'

# CHANGES in parse_and_update function
def parse_and_update(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            language = None
            print(f'file:{file}')
            
            # No changes in file filtering
            if file == 'sync_script.py' or file == 'sync_leetcode_data.yml':
                continue
            
            # No changes in language detection
            if file.endswith('.py'):
                language = 'Python'
            elif file.endswith('.sql'):
                language = 'SQL'
            elif file.endswith('.js'):
                language = 'Javascript'
            elif file.endswith('.ts'):
                language = 'Typescript'
            
            if language:
                problem_name = root.split('/')[-1]
                print(f'Processing {problem_name}')
                file_name = file[:4]
                readme_path = os.path.join(root, 'README.md')
                difficulty = 'Unknown'

                if os.path.isfile(readme_path):
                    with open(readme_path, 'r') as readme_file:
                        first_lines = ''.join([next(readme_file) for _ in range(2)])
                        difficulty = extract_difficulty(first_lines)

                # CHANGED: Now getting commit date for the specific file
                commit_date = get_last_commit_date(os.path.join(root, file))
                print(f"{problem_name} - Committed on: {commit_date}")
                
                if should_update(problem_name, commit_date):
                    # No changes in data preparation
                    data = {
                        'question_name': problem_name,
                        'file_name': file_name,
                        'readme_file_name': 'README.md' if 'README.md' in files else None,
                        'commit_date': commit_date,
                        'difficulty': difficulty,
                        'language': language,
                    }
                    
                    # CHANGED: Using insert instead of upsert to maintain history
                    response = supabase.table('leetcode_questions').insert(data).execute()
                    print(f"Added new entry for {problem_name} with commit date: {commit_date}")
                else:
                    # CHANGED: Updated message to be more specific
                    print(f"Entry already exists for {problem_name} with commit date: {commit_date}")

# No changes in script execution
parse_and_update('.')
