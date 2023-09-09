#Problem Statement
#Find the sum of all numbers below N which divide the sum of the factorial of their digits.
#for eg: 19 >>> 1! + 9! = 1+362880 = 362881 which is also divisible by 19. Therfore it is a required number.

#SOLUTION
N = int(input()) #takesInput
def factorial(n): #defined a function to find factorial
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

def splitI(s): #defined a function to break a number into indiviual digits. For eg: 14 to [1,4]
    a =[]
    for i in str(s):
        a.append(int(i))
    return a

out = []
for i in range(11,N): #loop to find the requied numbers and sum them and check the if statement and returns the output
    a = sum([factorial(x) for x in splitI(i)])
    if a%i == 0:
        out.append(i)
    else:
        pass
print(sum(out))
