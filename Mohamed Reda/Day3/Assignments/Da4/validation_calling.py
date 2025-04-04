import modules.validtion_fun as valid

def main():
    name = valid.get_valid_name()
    email = valid.get_valid_email()

    print("\n===== User Information =====")
    print("Name:", name)
    print("Email:", email)
    print("Welcomet to the system")


main()