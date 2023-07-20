number = ""
for i in range(0,100):
   if i < 10:
      number += f"0{i}, "
   elif i < 99:
      number += f"{i}, "
   else:
      number += str(i)
print(number)