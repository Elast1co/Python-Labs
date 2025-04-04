def generate_nested_list():
    while True:
        try:
            x = int(input("Enter your value: "))
            if x <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    big_list = []
    
    for i in range(1, x + 1):
        s_list = []
        for j in range(1, i + 1):
            s_list.append(j * i) 
        big_list.append(s_list)

    return big_list


nested_list = generate_nested_list()
print("\nGenerated List:", nested_list)
