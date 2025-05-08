from math import factorial
import sys

ans=0
print("n e")
print("- -----------")

for i  in range(10):
    ans+=1/factorial(i)
    if ans>2.5:  print("%d %.9f"%(i, ans))
    elif ans==1 or ans==2 : print("%d %d"%(i, ans))
    elif ans==2.5 : print("%d %.1f"%(i, ans))