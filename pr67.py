with open("myfile.txt",'r') as f:
  s = ""
  text = f.read()
  list = text.split()
  print(len(list))