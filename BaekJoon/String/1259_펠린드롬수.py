while True:
  case = input()
  if case==str(0):
    break
  if ''.join(reversed(case)) == case:
    print('yes')
  else:
    print('no')