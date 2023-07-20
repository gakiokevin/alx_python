import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
m = str(number)
lastDigit = m[-1]
if int(lastDigit) > 5:
   print("Last digit of {m} is {lastDigit} and is greater than 5".format(m = m, lastDigit=lastDigit))
elif int(lastDigit) == 0:
    print("Last digit of {m} is {lastDigit} and is 0".format(m = m, lastDigit=lastDigit))
elif int(lastDigit) < 6 and int(lastDigit) != 0:
   print("Last digit of {m} is {lastDigit} and is less than 6 and not 0".format(m = m, lastDigit=lastDigit))