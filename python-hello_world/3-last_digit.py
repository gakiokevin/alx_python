import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
   m = str(number)
   if m[-1] == 0:
      print("Last digit of {number} is {lastDigit} and is 0".format(number=number, lastDigit=int(m[-1])))
   else:
       lastDigit = "-"+ m[-1]
      lastDigit = int(lastDigit)
   print("Last digit of {number} is {lastDigit} and is less than 6 and not 0".format(number=number, lastDigit=lastDigit))
else:
   m = str(number)
   lastDigit = m[-1]
   if int(lastDigit) > 5:
       print("Last digit of {m} is {lastDigit} and is greater than 5".format(m = number, lastDigit=lastDigit))
   elif int(lastDigit) == 0 :
           print("Last digit of {m} is {lastDigit} and is 0".format(m = number, lastDigit=lastDigit))
   else:
       print("Last digit of {m} is {lastDigit} and is less than 6 and not 0".format(m = number, lastDigit=lastDigit))
