# In this we need to find second largest number of array in O(n) time complexity.
# Input: Given array of integers.
# Output: Second Largest element of array but array not sorted.

arr = [int(n) for n in input().split()]
f=s=check=-999999999 
if len(arr)<2:
    print('Length should be greater than 2.')

for x in arr:
    if (x>f):
        s=f
        f=x
    elif (x>s and x!=f):
        s=x
if (s==check):
    print('No max second Element.')
else:
    print('Second Maximum Element is',s) 


