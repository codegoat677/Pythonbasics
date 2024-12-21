# print('on the firts line', end="")  #prints on the next line "end="
# a= int(input('enter the value', end=""))
# print(6//5)    #floor division takes lower value
# print(6/5)
# print(2**3)    #2 to the power 3
a= [1,2,'hi', 3.45, "hello"]
# print(a[2])
# print(type(a[2]))
# print(a[:])
# print(a[:2])
# print(a[2:])
# print(a[-2:])  # - starts from the back
# print(a[::2])  # jumps 2 places
# print(a[::-1])   # prints it in reverse
# a[2] = 6         # re assgin the value
# print(a)
# a[2:4]=["hi", 5.22]
# print(a)
#print(len(a)) 
#print(a[4])
#print(a[::-1])
#if(len(a)==5):

    #print("Yes")
#else:
    #print("No")
# a=int(input("enter a number"))
# print(a)
# b= []
# print(b)
# b.append(a)
# print(b)
# for i in range(0,5):
    # a=int(input("enter a number "))
    # b.append(a)
# print(b)    

# b.pop(4)
# b.pop(0)
# b.sort()
# print(b) 
# import random
# a= []
# for i in range(0,20):
    # a.append(random.randint(1,100))
# print(a)    
# a= (2, (2,4,7), [1,2,3], 'hi')
# print(a)
# b = list(a)
# print(b)
# print(a[2][1])
# list of prime numbers below 100 using list comprehension
# a= {1,2,3,2,4,4,5}      #set doesnt print duplicate values
# print(a)
# a.discard(5)
# print(a)
# a.discard(7)

# a.add(66)
# print(a)
# b= {"lol": "laugh out loud", "wu": "whats up"}   #dictionary
# print(b)        
# b["lol"] = "lol"  #update key value
# print(b)
# print(b.keys())
# dict={}
# n= int(input("number of products are: "))
# for i in range(0,n):
    # n2= str(input("product name: "))
    # p= int(input("product price: "))
    # dict[n2]= p
# for i in range(0,n):
    # n3= str(input("enter product name: "))
    # print(dict[n3])
# am= int(input("enter amount"))
# if()
# 
# 
# def sum(a,b):
    # print("sum is", a+b)
# sum(2,3)

# def divide(a,b):
    # return a/b
# print(divide(3,2))

# sum(b=3, a=4)
# recursion use for factorial:-
# def facto(n):
    #if (n==1):
        #return 1
    #else:
        #return (n * facto(n-1))
# print(facto(5))

# def rectangle(m,n):
    # for i in range(0,m):
        # for j in range(0,n):
            # print("*", end='')
        # print("")
# rectangle(4,3)    

def add_excitement(m):
    for i in range(len(m)):
        m[i] += '!'
        
n= ["lol",'hi', 'bye']
add_excitement(n)
print(n)




a={10, 20, 30, 40.369, 123+5j}
b={'python', 'java', 'c++'}
a.update(b)
print(a)

