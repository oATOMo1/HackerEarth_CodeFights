def gcd(x,y):
    while(y):
        x,y = y, x%y
    return x
	

def finalExamRank(current):
    counter = 0
    for i in range(1, current):
        if gcd(i, current) == 1:
            counter += 1
    return counter

for i in range(0, int(input())):
    print(finalExamRank(int(input())))
