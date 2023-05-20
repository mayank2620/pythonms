with open("myfile.txt", 'r') as f:
    s = ""
    text = f.readlines()
    print(len(text))