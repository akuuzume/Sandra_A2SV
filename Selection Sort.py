class Solution: 
    def selectionSort(self, arr):
        #code here
        for _ in range(len(arr)):
            for i in range(0,len(arr)-1):
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
        return arr
