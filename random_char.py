'''
'disabled_char' is useful in situations when we want to block specific char.
'without' is a parameter that must be a list of chars. The chars will be blocked
'''

def random_char(disabled_char=None, without=None):
  list_of_chars = []
  list_of_chars.extend(string.ascii_lowercase)
  list_of_chars.extend(string.ascii_uppercase)
  list_of_chars.extend(string.digits)
  list_of_chars.extend(string.punctuation)

  if disabled_char != None:
    list_of_chars.remove(disabled_char)

  if without != None:
    for ch in without:
      list_of_chars.remove(ch)

  return random.choice(list_of_chars)

