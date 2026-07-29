l=["apple","banana","cherry","date","fig","grape"]

def rem(l,word):
    n =[]

    for i in l:
        if not(i==word):
            n.append(i.strip())
    return n    
print(rem(l,"date"))