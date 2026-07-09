# O(n^2) time | O(1) space
# def twoNumberSum(array,target):
#     for i in range(len(array) -1):
#         firstNum = array[i]
#         for j in range(i+1,len(array)):
#             secondNum = array[j]
#             if (firstNum + secondNum == target):
#                 return [ firstNum, secondNum]
#     return []

# O(n) time | O(n) space 
# def twoNumberSum(array,target):
#     hashtable = {}
#     for num in array:
#         if target - num in hashtable:
#             return [ num, target - num ]
#         else:
#             hashtable[num] = True
#     return []

# O(nlogn) time | O(1) space 
def twoNumberSum(array,target):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        Sum = array [ left ] + array [ right ]
        if Sum == target:
            return [ array[left], array[right]]
        elif Sum < target:
            left += 1
        elif Sum > target:
            right -= 1
    return []
    
    
array = [3,5,-4,8,11,1,-1,6]
target =10
result =twoNumberSum(array,target)
print(result)
