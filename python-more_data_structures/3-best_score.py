def best_score(a_dictionary):
   if not a_dictionary:
      return None
   try:
      max_value = max(a_dictionary.values())
      for key,value in a_dictionary.items():
         if value == max_value :
            return key
   except ValueError:
      return None