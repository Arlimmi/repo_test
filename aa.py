# Write a program that converts a roman numeral to an integer.
def roman_to_int(s: str) -> int:
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_numerals[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
            
        prev_value = value
        
    return total

# Example usage
if __name__ == "__main__":
    roman_numeral = input("Enter a Roman numeral: ")
    integer_value = roman_to_int(roman_numeral)
    print(f"The integer value of {roman_numeral} is {integer_value}.")
    
