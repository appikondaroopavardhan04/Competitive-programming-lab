def factorial(fact):
    if (fact==1):
        return 1
    result=fact*factorial(fact-1)
    return result
fact=int(input())
res=factorial(fact)
print(res)
