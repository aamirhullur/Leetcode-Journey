def encode(strs):
    # write your code here
    stri = ""
    for i,r in enumerate(strs):
        length = len(r)
        stri += str(length) + "#" + r

    return(stri)

def decode(string):
    new = ""
    res = []
    for i,r in enumerate(string):
        if r.isdigit():
            if string[i+1] != '#':
                continue
            else:
                num = int(r)
                res.append(string[i+2:i+2+num])
    return res



a = encode(["leet11","code","love","you"])
print(a)
print(decode(a))
