class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = 0
        i,j = 0,1
        cnt = 1
        while j < len(chars):
            if chars[j] == chars[i]:
                j+=1
                # cnt+=1
            else:
                if j - i  == 1:
                    chars[curr] = chars[i]
                    curr+=1
                else:
                    
                    # if j-i < 10:
                    #     chars[curr] = chars[i]
                    #     curr+=1
                    #     chars[curr] = str(j-i)
                    #     curr+=1
                    # else:
                    #     chars[curr] = chars[i]
                    #     curr+=1
                    #     chars[curr] = str((j-i)//10)
                    #     curr+=1
                    #     chars[curr] = str((j-i)%10)
                    #     curr+=1
                    chars[curr] = chars[i]
                    curr+=1
                    for x in str(j-i):
                        chars[curr] = x
                        curr+=1

                i = j
                j+=1
            
        if j - i  == 1:
            chars[curr] = chars[i]
            curr+=1
        else:
            # if j-i < 10:
            #     chars[curr] = chars[i]
            #     curr+=1
            #     chars[curr] = str(j-i)
            #     curr+=1
            # else:
            #     chars[curr] = chars[i]
            #     curr+=1
            #     chars[curr] = str((j-i)//10)
            #     curr+=1
            #     chars[curr] = str((j-i)%10)
            #     curr+=1
            chars[curr] = chars[i]
            curr+=1
            for x in str(j-i):
                chars[curr] = x
                curr+=1


        print([chars,curr,i,j])
        while j > curr:
            chars.pop()
            j-=1

