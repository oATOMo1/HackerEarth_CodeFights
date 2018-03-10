# Calculate GCD ( Greatest Common Divisor ) of x and y using EUCLIDEAN ALGORITHM
def gcd(x,y):
    while(y):
        x,y = y, x%y
    return x
	
# Calculate number of numbers that are relatively prime within the range [1, current]
def finalExamRank(current):
    counter = 0 # for counting the numbers
    for i in range(1, current):
        if gcd(i, current) == 1: # function returns 1 if numbers are relatively prime
            counter += 1 # incrementing counter
    return counter # returning the max numbers relatively prime

# Asking input and calling our functions
for i in range(0, int(input())):
    print(finalExamRank(int(input())))
