# n=int(input("necenci ededi cap etsin:"))
# fib=[1,1]
# a=0
# while True:
#     next=int(fib[a])+int(fib[a+1])
#     fib.append(next)
#     a+=1
#     if len(fib)==n:
#         break
# print(fib[n-1])
    
# a=[1,2,3,4,4,5,7,8,12,31,34,45,66,76,78,98]
# target=35
# l=len(a)//2
# while True:

#     if a[l]==target:
#         print("true")
#         break
#     elif a[l]<target:
#         l+=1
#     elif a[l]>target:
#         l-=1
#     elif (l==0 and a[l]!=target)or( l==(len(a)-1) and a[l]!=target):
#         print("false")
#         break

a=[1,2,3,4,4,5,7,8,12,31,34,45,66,76,78,98]
target=35
if a.count(target)==0:
    print("false")
else:
    print("true")