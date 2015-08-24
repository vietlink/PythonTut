__author__ = 'v11424'
def vector_add(v, w):
    return [v_i+w_i for v_i, w_i in zip(v, w)]
def vector_subtract(v, w):
    return [v_i-w_i for v_i, w_i in zip(v, w)]
def vectors_sum(vectors):
    result=vectors[0]
    for vector in vectors[1:]:
        result=vector_add(result, vector)
    return result
def scalar_multiply(c, v):
    return [c*v_i for v_i in v]
def vector_mean(vectors):
    n=len(vectors)
    return scalar_multiply(1/n, vectors_sum(vectors))
v=[1,2,3,4]
w=[2,3,4,5]
print(vector_add(v, w))
print(vector_subtract(v, w))
print (vector_mean(v))
