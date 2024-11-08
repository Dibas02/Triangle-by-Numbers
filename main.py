rows = int(input("Enter the number of rows:"))

for i in range(rows):
    n = 1
    for j in range(i+1):
        print(n, end=" ")
        n = n+1
    print()