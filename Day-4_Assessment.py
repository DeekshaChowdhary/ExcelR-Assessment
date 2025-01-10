# Program to calculate the sum of even numbers between 1 and n

n = int(input("Enter a positive integer: "))
even_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:  
        even_sum += i  
print("The sum of all even numbers between 1 and", n, "is:", even_sum)
