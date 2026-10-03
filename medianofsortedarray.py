
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.extend(b)
l=len(a)
a.sort() 
median = (a[l//2]+a[l//2-1])/2 if l%2==0 else a[l//2]
if median == int(median):
    print(f"{median:.1f}")
else:
    print(median)
