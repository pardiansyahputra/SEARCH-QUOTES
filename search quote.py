# Number search tool formula
# Using ANSI escape code (number, f"\033[92m{number}\033[0m")
def find_number(sentence):
    count = sentence.count(number)

    if number in sentence:
        highlighted_number = sentence.replace(number, f"\033[92m{number}\033[0m") # target will be green
        print(f"Found sentence: {highlighted_number}")
    return count

# Word search tool formula
# Using ANSI escape code (word, f"\033[92m{word}\033[0m")
def find_word(sentence):
    count = sentence.count(word)

    if word in sentence:
        highlighted_word = sentence.replace(word, f"\033[92m{word}\033[0m") # target will be green
        print(f"Found sentence: {highlighted_word}")
    return count

# Counting the number of letters in a sentence
# This tool does not involve the use of ANSI
def count_letters(sentence):
    count = 0

    for letter in sentence:
        if letter != " ":
            count += 1

    return count

# Initial display of the program
while True:
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("*******************************   @     @    **********************************")
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("**************************     ###         ###     ****************************")
    print("========================== From Phantom to Security ===========================")
    print("================================================================================")
    print("WELCOME TO WORD SEARCH, WHAT DO YOU WANT TO SEARCH FOR \n -1. Find number\n -2. Find word\n -3. Number of words/letters\n -4. Exit\n")

    # Input data or options
    choice = str(input("Enter a choice in number: "))

    # Program 1
    if choice == "1":

        try:
            sentence = str(input("Enter the target sentence: "))
            number = str(input("Enter the number to search for: "))
            print("===================================================================================================================")
            number_count = find_number(sentence)
            print(f"Found {number_count} in the search")

            # Process of saving information
            print("===================================================================================================================")
            save = str(input("Do you want to save it? ..(yes/no) \n PLEASE NOTE THAT SAVING WILL NOT INVOLVE COLOR>>>"))
            if save == "yes":
                with open("search code.txt", "w") as file:
                    file.write(f"The sentence: {number in sentence}\n")
                    file.write(f"The number: {number}\n")
                    file.write(f"The number count: {number_count}\n")
                    print("Saved as (search quotes) \n")

            else:
                print("Thank you...")
                print("===================================================================================================================")

        except ValueError:
            print("ENTER THE CORRECT CHOICE....")

    # Program 2
    elif choice == "2":

        try:
            sentence = str(input("The sentence: "))
            word = str(input("Enter the word to search for: "))
            print("===================================================================================================================")
            word_count = find_word(sentence)
            print(f"Found {word_count} in the search")

            # Process of saving information
            print("===================================================================================================================")
            save = str(input("Do you want to save it? ..(yes/no) \n PLEASE NOTE THAT SAVING WILL NOT INVOLVE COLOR>>>"))
            if save == "yes":
                with open("search code.txt", "w") as file:
                    file.write(f"The sentence: {word in sentence}\n")
                    file.write(f"The word: {word}\n")
                    file.write(f"The word count: {word_count}\n")
                    print("Saved as (search quotes) \n")
                    print("PLEASE NOTE THAT SAVING WILL NOT INVOLVE COLOR")
            else:
                print("Thank you...")
                print("===================================================================================================================")

        except ValueError:
            print("PLEASE ENTER CORRECT DATA.....")

    # Program 3
    elif choice == "3":
        try:
            sentence = (input("Enter a sentence: "))
            result = count_letters(sentence)
            print("===================================================================================================================")
            print(f"The number of letters in the sentence is: {result}")
            print("===================================================================================================================")
        except ValueError:
            print("PLEASE ENTER CORRECT DATA.....")

    elif choice == "4":
        exit()
    else:
        print("PLEASE ENTER 1, 2 OR 3")