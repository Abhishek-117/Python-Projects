print("Hi, What's your name?")
name=input()
print('Hello '+name+', tell me your Date Of Birth : ')
year = int(input('Enter year : '))
month = int(input('Enter month : '))
date = int(input('Enter date : '))

def checkLeapYear(year):
  if year%4 ==0 and year%100 != 0 or year%400 == 0:
    return True
  return False

monthCode = {1:6,2:2,3:2,4:5,5:0,6:3,7:5,8:1,9:4,10:6,11:2,12:4}

dayCode = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday',
           4:'Thursday', 5:'Friday', 6:'Saturday'}

oddDays = 0
leapYear = 0

oddDaysYear = year%400
oddDaysYear = oddDaysYear//100

leapYear=checkLeapYear(year)

if oddDaysYear == 1:
  oddDays += 5
elif oddDaysYear == 2:
  oddDays += 3
elif oddDaysYear == 3:
  oddDays += 1

oddDays += year%100 + (year%100)//4

oddDays += monthCode[month]

if leapYear == True and (month == 1 or month == 2):
  oddDays -= 1
  
oddDays += date

oddDays %= 7

print('\nHey '+name+', you were born on '+dayCode[int(oddDays)])
