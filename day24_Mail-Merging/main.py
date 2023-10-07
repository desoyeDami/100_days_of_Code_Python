with open("./Input/Names/invited_names.txt") as name:
    current_name = name.readlines()

for individual_name in current_name:
    with open("./Input/Letters/starting_letter.txt") as letter:
        individual_letter = letter.readlines()

    comma_individual_name = individual_name.replace("\n", ",\n")
    dear = individual_letter[0].replace("[name],\n", f"Dear {comma_individual_name}")
    individual_letter[0] = dear

    with open(f"./Output/ReadyToSend/letter_for_{individual_name}.txt", "w") as ready_to_send:
        for i in range(0, len(individual_letter)):
            ready_to_send.write(str(individual_letter[i]))
