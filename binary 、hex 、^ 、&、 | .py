# another usage of int function
print(int(input(),2)) # convert binary to decimal


print(int(input(),16)) # convert hex to decimal


print(bin(int(input()))) # convert decimal to binary


print(hex(int(input()))) # convert decimal to hex


print(0b10001^0b10) # XOR: 1 if digits are different, else 0


print(bin(0b10001^0b10)) # confirm XOR result(convert to binary)


print(0b10001&0b01) # AND: 1 if both digits are 1, else 0


print(bin(0b10001&0b01)) # confirm AND result(convert to binary)


print(0b10001|0b0)  # OR: 1 if any digit is 1, else 0


print(bin(0b10001|0b0)) # confirm OR result(convert to binary)
