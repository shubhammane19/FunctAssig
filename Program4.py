def searchEle(listData,x):
    count = 0
    for num in listData:
        count = count +1
        if num == x:
            print(num, "found in list at count",count)
            break

listData = [1,2,3,4,5,3]
x = int(input("Enter element you want to search: "))
searchEle(listData,x)