def missing_char(str, n):
  new_str = ''
  count = 0
  for ch in range(0,len(str)-1):
    if str[n] == str[ch]:
        print("str[n] is",str[n])
        count += 1
    else:
      new_str = new_str + str[ch]
      print("new_str is now: ", new_str)
      count += 1
  return new_str

str_result = missing_char('kitten',1)
print(str_result)