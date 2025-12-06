numbers = list(range(1, 11))

first_five = numbers[slice(0, 5)]

reversed_first_five = first_five.copy()
reversed_first_five.reverse()

print("Original list:", numbers)
print("Extracted list:", first_five)
print("Reversed list:", reversed_first_five)
