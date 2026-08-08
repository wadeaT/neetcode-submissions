class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        padded_bed = [0] + flowerbed + [0]

        for i in range(1,len(flowerbed)+1):
            if padded_bed[i] == 0:
                if padded_bed[i-1] == 0 and padded_bed[i+1] == 0:
                    padded_bed[i] = 1
                    n-=1
                    if n == 0:
                        return True 
                    
        if n<= 0:
            return True
        return False