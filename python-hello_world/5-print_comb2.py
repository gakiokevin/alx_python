number = ""
for i in range(0,100):
   if i < 10:
      number += "0{i}, ".format(i=i)
   elif i < 99:
      number += "{i}, ".format(i=i)
   else:
      number += "{i}".format(i=str(i))
print(number)