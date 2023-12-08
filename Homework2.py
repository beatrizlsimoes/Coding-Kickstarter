# Question 1
for number in range(100):
     output = 'o' * number
print(output)
# the program will write a string with 99 (because it starts in 0, not 1) characters

# Question 2
def calculate_vat(amount):
    return amount * 1.2
total = calculate_vat(100) 
print(total)