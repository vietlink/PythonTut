__author__ = 'v11424'
def shape(A):
    num_rows=len(A)
    num_cols=len(A[0]) if A else 0
    return num_rows, num_cols
def get_row(A,i):
    return A[i]
def get_col(A,j):
    return [A_i[j] for A_i in A]
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j)
             for i in range(num_cols)]for j in range(num_rows)]
def is_diagonal(i, j):
    return 1 if i==j else 0
M=[[1,2], [3,4], [5,6]]
print (shape(M))
print(get_col(M,1))
print(get_row(M, 0))
