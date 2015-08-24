__author__ = 'ngo'
import random
# tao list 4 so ngau nhien
four_uniform_random=[random.random() for _ in range(4)]
print(four_uniform_random)
# set seed cho ham random
random.seed(10)
print(random.random())
# lay gia tri random trong mot khoang
print(random.randrange(10))
print(random.randrange(3,6))
# shuffle list random
up_to_tens= [x for x in range(10)]
random.shuffle(up_to_tens)
print(up_to_tens)