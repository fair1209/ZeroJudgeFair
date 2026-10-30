
def filt(n):
    result=[]
    for i in range(2,int(n**0.5)+1): #i是因數
        ct=0
        while n%i==0:
            ct+=1
            n=n//i
        if ct>0:
            if ct==1:
                result.append(str(i))
            else:
                result.append(f"{i}^{ct}")
    result.append(str(n)) if n>1 else None
    return " * ".join(result)

n=int(input())
print(filt(n))



