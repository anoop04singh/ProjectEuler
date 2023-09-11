#Work out the first ten digits of the sum of N50-digit numbers.
"""Input Format:
First line contains N, next N lines contain a 50 digit number each.

Output Format:
Print only first 10 digit of the final sum
"""

def digitSum(s): #function to return thr sum of digits
    return sum([int(i) for i in s])
               
N = int(input()) #takes input N
l = []               
for a0 in range(N):
    n = str(input()) #takes input for N lines
    l.append(int(n) - digitSum(n)) #appends the values in a list
print(str(sum(l))[:10]) #outputs the sum of first 10 digits of the sum
