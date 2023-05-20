print("1.Want Straight like You")
print("2.Want Reverse like Your Gf")
a = input()
if a == '1':
    n = input("Enter Start Point")
    c = n.isdigit()
    f = input("Enter Stop Point")


    if c:

     print("1.Want Horizontal")
     print("2.Want Vertical")
     g = int(n)
     b = input()
     v = int(f)
     for i in range(g, v + 1):
          if b == '1':
            print(i, end=",")
          elif b == '2':
              print(i)
          else:
              print("Invalid")
          if g > v:

            print("1.Want Horizontal")
            print("2.Want Vertical")
            for i in range(g, v - 1, -1):
               if b == '1':
                print(i, end=",")
               elif b == '2':
                  print(i)
               else:
                   print("Invalid")
    else:
        print("Enter numbers only")
elif a == '2':
    n = int(input("Enter Start Point"))
    f = int(input("Enter Stop Point"))
    print("1.Want Horizontal")
    print("2.Want Vertical")

    b = input()
    for i in range(n, f - 1,-1):
        if b == '1':
            print(i, end=",")
        elif b == '2':
            print(i)
        else:
            print("Invalid")
    if n<f:
        for i in range(n, f + 1):
            if b == '1':
                print(i, end=",")
            elif b == '2':
                print(i)
            else:
                print("Invalid")

else:

    while a != '1':
        print("Invalid")
        print("1.Want Straight like You")
        print("2.Want Reverse like Your Gf")
        a = input()
        if a != '1' and not '2':
            continue
        if a == '1':
            n = int(input("Enter Start Point"))
            f = int(input("Enter Sto Point"))
            print("1.Want Horizontal")
            print("2.Want Vertical")

            b = input()

            for i in range(n, f + 1):
                  if b == '1':
                    print(i, end=",")
                  elif b == '2':
                    print(i)
                  else:
                    print("Invalid")
                    break
            if n > f:
                for i in range(n, f - 1, -1):
                    if b == '1':
                        print(i, end=",")
                    elif b == '2':
                        print(i)
                    else:
                        print("Invalid")
        elif a == '2':
            n = int(input("Enter Start Point"))
            f = int(input("Enter Stop Point"))
            print("1.Want Horizontal")
            print("2.Want Vertical")

            b = input()
            for i in range(n, f - 1, -1):
                if b == '1':
                    print(i, end=",")
                elif b == '2':
                    print(i)
                else:
                    print("Invalid")
            if n < f:
                for i in range(n, f + 1):
                    if b == '1':
                        print(i, end=",")
                    elif b == '2':
                        print(i)
                    else:
                        print("Invalid")
            break