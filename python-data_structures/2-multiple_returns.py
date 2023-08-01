def multiple_returns(sentence):
   length = len(sentence)
   first_char = ('Length: {} - First character: {}'.format(length,sentence[0])) if length > 0 else None
   return first_char,