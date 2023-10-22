def palindrome_n(string):
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]
input_string = input("Enter a string: ")
if palindrome_n(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
