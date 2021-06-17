a=int(input("enter the terms"))
f=0
s=1
if a<=0:
print("the requested series is",f)
else:
print(f,s,end="")
for x in range(2,a):
next=f+s
print(next,end="")
f=s
s=next
enter the terms=13
0,1,1,2,3,5,8,13,21,34,55,89,144
