def primepartition(m):
    if m < 2:
        return False
    for i in range(1,m+1):
        j = m - i
        if(isprime(i) and isprime(j)):
            return True
    return False
def isprime(n):
    if n < 2:
        return False
    f = 0
    for i in range(1,n+1):
        if(n%i == 0):
            f+=1
    if(f == 2):
        return True
    return False
def main():
    p = primepartition(7)
    print(p)
    

