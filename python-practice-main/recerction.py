'''
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))
'''
'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(4))
'''
'''
def sd(n):
    if n==0:
        return 0
    return n%10+sd(n//10)
print(sd(389))

'''
L=[11,[22,[45,44,66],25],24]
def SId(L):
    summ=0
    for i in L:
        summ=summ+SId(i)
    else:
        summ=summ+i
    return summ
print(SId(L))
