def prime(n):
    count=0
    i=1
    while(i<=n):
        if(n%i==0):
            count=count+1
            i=i+1
            return n
n=int(input("Enter a number"))
if(count==2):
     print("Prime")
else:
     print("not Prime")



