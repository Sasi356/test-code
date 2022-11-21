def solve1(n):
    while(n>0):
        rem=n%10
        n//=10
        if(rem==3 or rem==4 or rem==7):
            return False
    return True
def solve(n):
    x,cnt=1,1
    while(cnt<n):
        x+=1
        if solve1(x):
            cnt+=1
    return x
n=int(input())
print(solve(n))
