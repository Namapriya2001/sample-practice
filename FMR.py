from functools import reduce
nums=(2,3,4,5,6,7,8,9)
evens=list(filter(lambda x:x%2==0,nums))
double=list(map(lambda x:x*2,evens))
sum=reduce(lambda a,b:a+b,double)
print(evens)
print(double)
print(sum)
