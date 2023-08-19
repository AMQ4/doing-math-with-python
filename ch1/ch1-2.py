try:
    n = int(input("Enter the number for the multiplication table:\n> "))
    max_multiple = int(input("Enter the maximum multiple you want to see:\n> "))
except ValueError as e:
    print(e)
else:
    for i in range(1, max_multiple+1):
        print("{0} x {1} = {2}".format(n, i, i*n))