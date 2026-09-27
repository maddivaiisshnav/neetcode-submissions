class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}
        for i in nums:
            h_map[i] = h_map.get(i,0)+1
        l = []
        h_map = dict(
            sorted(h_map.items(),key=lambda x: x[1], reverse=True)
            )
        res = list(h_map.keys())[:k]
        return res







        
        
        