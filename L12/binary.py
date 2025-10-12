decimal = int(input("Enter a decimal number: "))
binary = ""

# We'll use a for loop to simulate the conversion
for i in range(8):  # assuming 8-bit binary for simplicity
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

print("Binary number is:", binary)
