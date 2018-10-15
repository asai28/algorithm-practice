# -*- coding: utf-8 -*-
"""
@Author: Anuhya Sai Nudurupati
"""

def L( i , j ):
    if i >= 0 and j >= 0:
        if A[i] == B[j]:
            return 1 + L(i-1, j-1)
        else:
            return max(L(i-1, j), L(i, j-1))
    else:
        return 0
    
        
if __name__ == "__main__":
    A = "AGGTAB"
    B = "GXTXAYB"
    print(L(len(A)-1, len(B) - 1))

