def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    if(x<a[mid]):
        return mid
    elif(x>a[mid]):
        return mid+1
 

case1 = int(input())
st = input().strip(" ").split(" ")
l = [int(st[0])]
for k in range(1,len(st)):
    l.append(l[-1]+int(st[k]))
print (l)
for k in range(int(input())):
    print (binary_search(l,int(input()))+1)
