def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter your string: ")
vowel_count = count_vowels(user_input)
print("The count is", vowel_count)
