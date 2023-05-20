f = open('file.txt','a')
x = input("Enter student name")
y = input('Enter Student Marks'
)
z = f"{x}:{y}"
text = f.write(f'{x}:{y}\n')
f.close()