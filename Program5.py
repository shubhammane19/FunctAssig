def Parent():
    
    count1 = 0
    count2 = 0
    count3 = 0

    def digitCount(num):
        nonlocal count1 
        while(num != 0):
            count1 = count1 +1
            num = num//10
         
    def evenDigCount(num):
        nonlocal count2
        while(num!=0):
            if(num%2 == 0):
                count2 = count2+1
            num = num//10
    
    def oddCount(num):
        nonlocal count3
        while(num!=0):
            if(num%2!=0):
                count3 = count3+1
            num = num//10
            
    num = 12345    
    digitCount(num)
    evenDigCount(num)
    oddCount(num)
    retlist = [count1,count2,count3]
    print(retlist)

Parent()
#print(ret)
