n = int(input("Enter the value of n: "))

total = 0

print("Numbers from 1 to", n, ":")

for i in range(1, n+1):
    print(i, end=" ")
    total += i

print("\nSum of numbers from 1 to", n, "is:", total)
