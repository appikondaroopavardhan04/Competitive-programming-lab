'''import statistics as st
n=int(input())
a=list(map(int,input().split()))
m=st.mode(a)
if a.count(m)==1:
    print("-1")
else:
    print(m)'''
    
n=int(input())
a=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i,n):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]

mode=a[0]
maxcount=1
count=1
for i in range(1,n):
    if a[i] == a[i-1]:
        count+=1
    else:
        if count>maxcount:
            maxcount=count
            mode=a[i-1]
        count=1

if maxcount==1:
    print("-1")
else:
    print(mode)
    
    
