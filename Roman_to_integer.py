num_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_str = input("Enter a Roman numeral: ").upper()

num = 0

# Convert Roman numerals to integer
for i in range(len(roman_str)):
    if i > 0 and num_dict[roman_str[i]] > num_dict[roman_str[i - 1]]:
        num += num_dict[roman_str[i]] - 2 * num_dict[roman_str[i - 1]]
    else:
        num += num_dict[roman_str[i]]

print("The integer value of", roman_str, "is:", num)
