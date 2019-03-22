def Missno(A): 
    n = len(A)
    total = (n+1)*(n+2)/2
    return total - sum(A)  
A = [1,2,3,4,6] 
print(Missno(A)) 
