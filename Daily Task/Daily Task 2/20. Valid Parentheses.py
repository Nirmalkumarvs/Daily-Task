class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}'} 
        stack=[] 
        for p in s: 
            if p in dic: 
                stack.append(dic[p]) 
            else: 
                if not stack or stack.pop()!=p: 
                    return False 
        if stack: 
            return False 
        return True
                    
        
