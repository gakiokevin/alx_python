def raise_exception_msg(message=""):
   raise NameError('{} '.format(message))
try :
  # raise_exception_msg('C')
   raise_exception_msg()
except NameError as ne :
   print(ne)
   raise NameError('{}'.format(message))
