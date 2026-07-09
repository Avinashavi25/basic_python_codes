
# O(n) time | O(1) space 
# def validateSubsequence(array,subSequence):
#     arrInd = 0
#     seqInd = 0
#     while seqInd < len(subSequence) and arrInd < len(array):
#         if array[arrInd] == subSequence[seqInd] :
#             seqInd += 1
#         arrInd += 1
#     return seqInd == len(subSequence)
    
# O(n) time | O(1) space 
def validateSubsequence(array,subSequence):
    seqInd = 0
    for ele in array:
        if seqInd == len(subSequence):
            return True
        if subSequence[seqInd] == ele:
            seqInd += 1
    return seqInd == len(subSequence)

array = [3,5,-4,8,11,1,-1,6]
subSequence = [ -4, 11, -1]
result =validateSubsequence(array,subSequence)
if result:
    print("validate subSequence")
else:
    print( "Not validate subSequence")
