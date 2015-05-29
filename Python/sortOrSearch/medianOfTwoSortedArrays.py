import pdb
class Solution:
    def findMedianSortedArrays(self, A, B):
        totalLen = len(A) + len(B)
        if totalLen % 2 == 0 :
            front = self.findMedianSortedArraysRecur(A, 0, len(A), B, 0, len(B), totalLen / 2)
            end =  self.findMedianSortedArraysRecur(A, 0, len(A), B, 0, len(B), totalLen / 2 + 1)
            #print front, end
            return (front + end) / 2.0
        else:
            return self.findMedianSortedArraysRecur(A, 0, len(A), B, 0, len(B), totalLen / 2 + 1)

    def findMedianSortedArraysRecur(self, A, AStart, AEnd, B, BStart, BEnd, k):
        if AEnd - AStart > BEnd - BStart:
            return self.findMedianSortedArraysRecur(B, BStart, BEnd, A, AStart, AEnd, k)
        #pdb.set_trace()
        #print A, AStart, AEnd, B, BStart, BEnd, k
        if AEnd - AStart <= 0:
            return B[BStart + k - 1]

        if BEnd - BStart <= 0:
            return A[AStart + k - 1]
        
        if k == 1:
            return min(A[AStart], B[BStart])

        pa = min(k / 2, AEnd - AStart)
        pb = k - pa
        #print "pa, pb"
        #print pa, pb

        if A[AStart + pa - 1] < B[BStart + pb - 1]:
            return self.findMedianSortedArraysRecur(A, AStart + pa, AEnd, B, BStart, BEnd, k - pa)
        elif A[AStart + pa - 1] > B[BStart + pb - 1]:
            return self.findMedianSortedArraysRecur(A, AStart, AEnd, B, BStart + pb, BEnd, k - pb)
        else:
            return A[AStart + pa - 1]

A = Solution()
#test_list1 = [4, 7, 12, 14, 21]
#test_list2 = [5, 9, 15, 17, 23, 25]
test_list1 = [1]
test_list2 = []
print A.findMedianSortedArrays(test_list1, test_list2)
