# Ask the user for a decimal number
decimal_number = int(input("Enter a decimal number: "))

# Convert the decimal number to binary and remove the "0b" prefix
binary_representation = bin(decimal_number)[2:]

# Print the binary representation
print(f"The binary representation of {decimal_number} is: {binary_representation}")
