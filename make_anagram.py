from collections import Counter
def make_anagram(a,b):
    A = dict(Counter(a))
    B = dict(Counter(b))
    D = 0
    for i in A:
        try:
            if A[i] > B[i]:
                D += A[i] - B[i]
                del B[i]
            elif A[i] < B[i]:
                D += B[i] - A[i]
                del B[i]
            elif A[i] == B[i]:
                del B[i]
        except:
            D += A[i]
    for i in B:
        D += B[i]
    return D
