def rotatelist(l, k):
    if(k<0):
        return l
    if(k>len(l)):
        k = k % len(l)
    return l[k:] + l[:k]
def main():
    l = [1, 2, 3, 4, 5]
    k = 3
    print(rotatelist(l, k))