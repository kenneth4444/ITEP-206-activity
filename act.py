def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_vowel_or_consonant(letter):
    if letter.lower() in 'aeiouAEIOU':
        return "Vowel"
    else:
        return "Consonant"

def is_special_character(char):
    if not char.isalnum(): 
        return "Special Character"
    return "Not a Special Character"

def main():
    while True:
        print("\nSelect a number you want:")
        print("1. for odd or even")
        print("2. for vowel or consonant")
        print("3. Check if a character is special")
        print("4. Exit")

        choice = input("Enter your choice (1-4 or 'STOP' to exit): ")

        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                print(f"The number is: {is_even_or_odd(num)}")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "2":
            letter = input("Enter a letter: ")
            if len(letter) == 1 and letter.isalpha():
                print(f"The letter is: {is_vowel_or_consonant(letter)}")
            else:
                print("Please enter a valid single letter.")
                
        elif choice == "3":
            char = input("Enter a character: ")
            if len(char) == 1:
                print(f"The character is: {is_special_character(char)}")
            else:
                print("Please enter a valid single character.")
                
        elif choice == "4":
            print("Exiting the program.")
            break
            
        elif choice.lower() == "stop":
            print("Program stopped.")
            break
            
        else:
            print("Invalid, select a number between 1-4 or type 'STOP'.")

if __name__ == "__main__":
    main()