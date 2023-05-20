marks = {"Mayank": 23 , "Harsh" : 42 , "Megha": 23}
print(marks)
sv = sorted(marks.items(),key = lambda x : x[1])#sort by value in ascending
print(sv)
sv = sorted(marks.items(),reverse = True,key = lambda x : x[1])#sort by value in Descending
print(sv)