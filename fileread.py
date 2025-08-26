def modify_file():
    # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Ask user what modification they want
        print("\nChoose a modification:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Remove blank lines")
        print("4. Find and replace words")
        
        choice = input("Enter your choice (1-4): ")
        
        # Apply modification based on user choice
        if choice == '1':
            modified_content = content.upper()
        elif choice == '2':
            modified_content = content.lower()
        elif choice == '3':
            modified_content = "\n".join([line for line in content.splitlines() if line.strip()])
        elif choice == '4':
            old_word = input("Enter the word to replace: ")
            new_word = input("Enter the new word: ")
            modified_content = content.replace(old_word, new_word)
        else:
            print("Invalid choice. No changes made.")
            return
        
        # Ask for output filename
        output_file = input("\nEnter the name for the new file (e.g., output.txt): ")
        
        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"\nModified file has been saved as '{output_file}'")
    
    except FileNotFoundError:
        print(f"\nError: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"\nError: You do not have permission to read '{input_file}'.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Run the function
modify_file()
