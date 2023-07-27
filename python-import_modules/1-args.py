def listarguments(*args):
   if args:
      print('{} arguments:'.format(len(args)))
      for index, arg in enumerate(args):
         print('{} : {}'.format(index +1,arg))
   else :
      print('{} arguments.'.format(0))
