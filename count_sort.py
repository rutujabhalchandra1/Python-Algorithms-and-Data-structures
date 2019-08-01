#Sort numbers 0-200, there can be multiple occurences of the number


def count_sort(input_arr):
    A = [0] * 6
    for i in input_arr:
        A[i] += 1
    print(A)
    B = []
    for i in range(len(A)):
        #B.extend([i] * A[i])
        B += ([i] * A[i])
    return B


a = count_sort([0,4,1,1,2,5,3,3])
print(a)



