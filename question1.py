def findshortestNum(source: str, target: str) -> int:
        m, n = len(source), len(target)
        res, j = 0, 0
        while j < n:
            i = 0
            ok = False
            while i < m and j < n:
                if source[i] == target[j]:
                    ok = True
                    j += 1
                i += 1
            if not ok:
                return -1
            res += 1
        
        return res
source1,target1 = 'abc','abcbc' 
source2,target2 = 'abc','acdbc'
source3,target3 = 'xyz','xzyxz'

res1 = findshortestNum(source1,target1)
res2 = findshortestNum(source2,target2)
res3 = findshortestNum(source3,target3)
print(f"res1:{res1},res2:{res2},res3:{res3}")
        
             
