def Factorial(arr):
    
    for i in (arr):
        fact = 1
        for j in range(1,i+1):
            fact = fact*j
        print(fact,end=" ")

arr = [1,2,3,4,5]
Factorial(arr)