__author__ = 'ngo'
even_numbers=[x for x in range(10) if x%2==0]
print("Even number: ", even_numbers)
square= [x*x for x in range(10)]
print("Square: ",square)
even_squares=[x*x for x in even_numbers if x%2==0]
print("Even square: ", even_squares)
square_dict={x:x*x for x in even_numbers}
print(square_dict)
zeroes= [0 for _ in even_numbers]
print(zeroes)
