s='kkbbrr'
res=' '
count=1
for ind in range(0,len(s)-1):
    if s[ind]==s[ind+1]:
        count=count+1
    else:
        res=res+str(count)+s[ind]
        count=1
res=res+str(count)+s[ind+1]
print(res)
            
