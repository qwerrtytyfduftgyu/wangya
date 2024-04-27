def digui(n):
    if int(n) > 0 :
       return int(n) * digui(n-1)
    else:
       return 1

print(digui(4.1))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# n = 5
# result = factorial(n)
# print(f"The factorial of {n} is: {result}")


