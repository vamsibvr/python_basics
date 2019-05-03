def f1(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    print res
f1(5)



for num in range(1,20):
    for j in range(2,num):
        if num%j==0:
            break
    else:
        print num


a,b=0,1
while b<=20:
    print b
    a,b=b,a+b
    
