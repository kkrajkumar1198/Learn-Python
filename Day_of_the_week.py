# Used Tomohiko Sakamoto’s Algorithm
# To find the day of the week - Calculate total number of days considering leap/non leap year and modulus with 7 to get the day of the week
# year // 4 - leap year
# year // 100 - not a leap year (so minus)
# year // 400 - leap year
# To not add leap year days in non-leap year, and if the day to find is in Jan or Feb, we are reducing one year. And to balance that, we are reducing one day every month from March

from sys import stdin

def dayOfWeek(day, month, year) :
	#actual_month_code = "033614625035"
	month_code = [0,3,2,5,0,3,5,1,4,6,2,4]
	day_code = {0:"Sunday",
				1:"Monday",
				2:"Tuesday",
				3:"Wednesday",
				4:"Thursday",
				5:"Friday",
				6:"Saturday"}
	if month < 3:
		year -= 1
	day = day_code[(year + year//4 - year//100 + year//400 + month_code[month-1]+day)%7]
	return day

def takeInput() :

	day_month_year = list(map(int,stdin.readline().strip().split(" ")))
	day = day_month_year[0]
	month = day_month_year[1]
	year = day_month_year[2]

	return day, month, year

t = int(input().strip())
for i in range(t) :

	day, month, year = takeInput()
	print(dayOfWeek(day, month, year))

