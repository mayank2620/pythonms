with open("myfile.txt",'r') as f:
  s = ""
  text = f.read()
  list = text.split()
  for i in list:
    if len(i) > len(s):
      s = i
  print(s)