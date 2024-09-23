# Enter your code here. Read input from STDIN. Print output to STDOUT

N = 10
def listPrimes(N):
    
    for i in range(2, N):
        prime = False
        
        for j in range(2, i):
            print(i, j)
            if (i % j == 0):
                prime = True
    
        if prime:
            print(i)

listPrimes(N)