n=int(input())
def solve(n):
    res= ""
    while n!=0:
        res=str(n%3)+res
        n=n//3
    return res
print(solve(n))
