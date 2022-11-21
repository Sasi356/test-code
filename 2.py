stng=input()
sub_str=input()
cnt=0
l=0
for i in sub_str:
    l+=1
for i in range(l):
    if i==l-1:
        last_character=sub_str[i]
for i in stng:
    if i==last_character:
        cnt+=1
print(cnt)
