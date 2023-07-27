def safe_print_division(a, b):
   result = None
   try:
     result = a / b
   except ZeroDivisionError:
      print('{} / {} = None'.format(a,b))
   finally:
      print('inside result : {}'.format(result))
      print('{} / {} = {}'.format(a,b,result))