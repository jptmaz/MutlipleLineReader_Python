# Write a method in python to write multiple line of text contents into a text file mylife.txt.

# Create a text file and name it mylife.txt

import sys
print(" ======= + =======")
print("       PATH       ")
print(sys.path)
print(" ======= + =======")

with open("C:/Users/HomePC/OOP_SourceCode/MultiLineWriter/mylife.txt", "w") as mylife_file:
    
    # Ask the user to enter Lines.
    
    Line_input = input("Enter a line: ")
    mylife_file.write(Line_input + "\n")
    print("Would you like to add more lines? Yes or no?")
    user_option = input(str("Answer: "))
    user_option = user_option.upper()
    
    # Create a while and if loops.
    
    while user_option == "YES":
        if user_option == "YES":
            Line_input = input("Enter a line: ")
            mylife_file.write(Line_input + "\n")
            print("Would you like to add more lines? Yes or no?")
            user_option = input(str("Answer: "))
            user_option = user_option.upper()
        else:
            break

print ("Thank you for using this program!")
        