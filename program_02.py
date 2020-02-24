from itertools import permutations
def largest(1):
    lst=[]
    for i in permutations(1,len(1)):
        lst.append("".join(map(str,i)))
    return max(lst)
ls=[]
n=int(input('enter the no. of elements'))
for i in range(0,n):
    ls.append(int(input()))
print(largest(ls))