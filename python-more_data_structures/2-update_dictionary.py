a = {
   'a':10
}
def update_dictionary(a_dictionary, key, value):
  if  str(key):
    a_dictionary[key] = value
    return a_dictionary
print(update_dictionary(a,'one', 'two'))