def fibonacci_sequence(n):
     sum = []
     a, b = 0, 1
     if n <= 0:
        sum = []
     else:
      while len(sum) < n :
         sum.append(a)
         a, b = b, a+b
      return sum
