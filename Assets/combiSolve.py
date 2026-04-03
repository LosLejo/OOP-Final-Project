

def solve(n, r):
    result = 0
    
    def combination(n, r):
        try:
            if (n - r) < 0:
                result = 0
                return result
            return (fact(n) / (fact(r) * fact(n - r)) )
        except:
            result = -1
            return result

    def fact(n):
        res = 1
        for i in range(2, n + 1):
            res = res * i
        return res
    
    result = int(combination(n, r))
    return result
    
