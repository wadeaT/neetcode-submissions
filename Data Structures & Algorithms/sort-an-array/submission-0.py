class Solution:
    #merge Sort
    def merge(self,arr,l,mid,h):
        n1 = mid - l + 1 
        n2 = h - mid

        L1 = [0] * n1
        L2 = [0] * n2 

        for i in range(n1):
            L1[i] = arr[l+i]
        for i in range(n2):
            L2[i] = arr[i+mid+1]
        
        i = 0 
        j = 0
        k=0

        while i < n1 and j <n2:
            if L1[i] <= L2[j]:
                arr[l+k] = L1[i]
                i+=1
            else:
                arr[l+k] = L2[j]
                j+=1
            k+=1
        while i<n1:
            arr[l+k] = L1[i]
            i+=1
            k+=1
        while j<n2:
            arr[l+k] = L2[j]
            j+=1
            k+=1

    def mergeSort(self,arr, l,h):
        mid = l+(h-l) // 2
        if l<h : 
            self.mergeSort(arr, l,mid)
            self.mergeSort(arr,mid+1,h)
            self.merge(arr,l,mid,h)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums