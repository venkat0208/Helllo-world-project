#Print missing numer from array
def get_missing_num(a):
    n=a[-1]
    print(n)
    sum1=0
    total=n*(n+1)//2
    print(total)
    sum1=sum(a)
    print(total -sum1)

a=[1,2,4,5,6,7]
get_missing_num(a)