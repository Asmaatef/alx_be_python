x = int(input("Enter the number for the multiplication table: "))
y = int(input("Enter the number of rows for the multiplication table: "))
for i in range(1, y + 1):
    result = x * i
    print(f"{x} * {i} = {result}")
    if i >= 10:
        print("The number of rows has been limited to 10.")
        break
else:
    if y > 10:
        print("The number of rows has been limited to 10.")
