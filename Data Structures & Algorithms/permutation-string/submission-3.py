class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m : 
            return False 
        
        s1_map = {}
        s2_map = {}

        for i in range(n):
            char_s1 = s1[i]
            char_s2 = s2[i]
            s1_map[char_s1] = s1_map.get(char_s1 , 0) + 1
            s2_map[char_s2] = s2_map.get(char_s2 , 0) + 1
        
        if s1_map == s2_map :
            return True 

        for fast in range(n , m):
            char_s2 = s2[fast]
            s2_map[char_s2] = s2_map.get(char_s2 , 0) + 1
            char_to_remove =  s2[fast - n]
            s2_map[char_to_remove] -= 1 
            if s2_map[char_to_remove] <= 0 :
                del s2_map[char_to_remove]
            
            if s1_map == s2_map : 
                return True

        return s1_map == s2_map