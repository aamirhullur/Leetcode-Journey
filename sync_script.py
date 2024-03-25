import os
from datetime import datetime
from supabase import create_client
import re
import subprocess
from subprocess import run

def should_update(problem_name, commit_date):
    """
    Checks if the database entry for problem_name needs an update based on commit_date.
    Returns True if update is needed, False otherwise.
    """
    result = supabase.table('leetcode_questions').select('commit_date').eq('question_name', problem_name).execute()
    
    # If problem not found in database, it should be added
    if not result.data:
        return True
    
    # Check if the commit date in the database matches the fetched commit date
    db_commit_date = result.data[0]['commit_date']
    if db_commit_date != commit_date:
        return True
    
    return False

def parse_and_update(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'sync_script.py' or file == 'sync_leetcode_data.yml':
                continue
            if file.endswith('.py') or file.endswith('.sql'):
                problem_name = root.split('/')[-1]
                file_name = file
                language = 'Python' if file.endswith('.py') else 'SQL'
                readme_path = os.path.join(root, 'README.md')
                difficulty = 'Unknown'
                
                if os.path.isfile(readme_path):
                    with open(readme_path, 'r') as readme_file:
                        first_lines = ''.join([next(readme_file) for _ in range(2)])
                        difficulty = extract_difficulty(first_lines)
                
                commit_date = get_last_commit_date(os.path.join(root, file))
                
                if should_update(problem_name, commit_date):
                    data = {
                        'question_name': problem_name,
                        'file_name': file,
                        'readme_file_name': 'README.md' if 'README.md' in files else None,
                        'commit_date': commit_date,
                        'difficulty': difficulty,
                        'language': language,
                    }
                    
                    response = supabase.table('leetcode_questions').upsert(data).execute()
                    if response.get('error'):
                        print(f"Error upserting data for {problem_name}: {response['error']}")
                else:
                    print(f"No update required for {problem_name}.")

parse_and_update('.') 
