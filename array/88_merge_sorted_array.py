class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        # nums1 = [1,2,3,0,0,0], m = 3, 
        # nums2 = [2,5,6], n = 3

        while m and n:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n:
            nums1[:n] = nums2[:n]

        return nums1
    

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        # nums1 = [0,1,2,3,5,6], m = 0, 
        # nums2 = [2,], n = 1


        while m and n:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
                
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n:
            nums1[:n+m] = nums2[:n]
        return nums1
    

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [1,2,3,0,0,0], m = 3, 
        # nums2 = [2,5,6], n = 3


        while m > 0  and n >0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n >0:
            nums1[:n] = nums2[:n]

        return nums1

