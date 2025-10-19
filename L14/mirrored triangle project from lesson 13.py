rows = int(input("How many rows do you want: "))

for i in range(1, rows + 1):
    spaces = rows - i
    stars = i
    print(' ' * spaces + '*' * stars)
    