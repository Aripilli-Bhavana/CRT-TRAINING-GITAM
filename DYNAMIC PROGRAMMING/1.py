#write  program to find the 5th term in fibonacci series
#recursion approach

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print("5th term in fibonacci series is:", fibonacci(5))