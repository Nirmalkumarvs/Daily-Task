class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(par,open,close,n): 
            if len(par)==2*n: 
                res.append(par) 
                return 
            if open<n: 
                backtrack(par+"(",open+1,close,n) 
            if close<open: 
                backtrack(par+")",open,close+1,n) 
                
        res=[] 
        backtrack("",0,0,n)
        return res
