REPLACESTRING = "[name]"



with open("./Input/Names/invited_names.txt") as names_files:
    names= names_files.readlines()
    print(names)
    
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents= letter_file.read()    
    # print(letter_file)
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(REPLACESTRING, name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
            
    