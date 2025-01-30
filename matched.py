def matched(s):
    c = 0
    for i in s:
        if(i == "("):
            c+=1
        elif(i == ")"):
            c-=1
        if(c < 0):
            return False
    if(c == 0):
        return True
    else:
        return False

def main():
    print(matched("zb%78"))
    