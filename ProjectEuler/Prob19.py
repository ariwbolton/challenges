
days = {"January" : 31, "February" : 28, "March" : 31, "April" : 30, "May" : 31, "June" : 30, "July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December": 31 }
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

dayOfWeek = 1
num = 0

for year in range(1901, 2001):
    for month in range(1, 13):
 
        daysInMonth = days[months[month - 1]]

        if year % 4 == 0 and month == 2:
            daysInMonth = daysInMonth + 1;
        
        for day in range(1, daysInMonth + 1):
 
            if dayOfWeek == 6 and day == 1:
                num = num + 1

            dayOfWeek = dayOfWeek + 1
            dayOfWeek = dayOfWeek % 7

print(num)

                
