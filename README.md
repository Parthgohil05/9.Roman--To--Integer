# Roman Numeral Converter

This Python script allows you to convert a Roman numeral to its corresponding integer value.

## Usage

1. Run the script.
2. When prompted, enter a valid Roman numeral.
3. The script will output the integer value of the Roman numeral you entered.

## How it Works

1. The script defines a dictionary `num_dict` that maps Roman numeral symbols to their corresponding integer values.

2. The user is prompted to enter a Roman numeral, which is immediately converted to uppercase for consistency.

3. The script initializes an integer variable `num` with a value of 0.

4. The script iterates through each character in the Roman numeral string:
   - If the current character's value is greater than the previous character's value, it means the current character represents a subtraction (e.g., IV represents 4, where the value of V (5) is subtracted from the value of I (1)).
   - In this case, the script subtracts twice the value of the previous character from the value of the current character and adds the result to `num`.
   - Otherwise, the script simply adds the value of the current character to `num`.

5. After iterating through the entire string, the script prints the integer value of the Roman numeral.

## Example

```
Enter a Roman numeral: MCMXCIV
The integer value of MCMXCIV is: 1994
```

This script correctly handles Roman numerals where subtraction is involved, such as IV (4), IX (9), XL (40), XC (90), CD (400), and CM (900).

Note: The script assumes that the user enters a valid Roman numeral. It does not perform any error checking or validation for invalid inputs.
