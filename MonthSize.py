year = int(input())
month = int(input())
largeMonths = [1,3,5,7,8,10,12]

for i in largeMonths:
    if(month == i):
        print("Number of days is 31")
    elif(month == 2):
        print("Number of days is 28")
    elif((month == 2) and ((year%400==0) or (year%4==0 and year%100!=0))):
        print("Number of days is 29")
    else:
        print("Number of days is 30")
    break