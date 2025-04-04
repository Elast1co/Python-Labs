def get_sorted_numbers():
    number_list = []
    
    for i in range(5):
        while True:   
            try:
                numb = int(input(f"Enter your number {i+1}: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        
        number_list.append(numb)

    asc = sorted(number_list)
    dsc = sorted(number_list, reverse=True)

    return number_list, asc, dsc


numbers, ascending, descending = get_sorted_numbers()

print("Original List:", numbers)
print("Ascending Order:", ascending)
print("Descending Order:", descending)
