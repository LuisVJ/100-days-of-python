letter = open("./Input/Letters/starting_letter.txt")
names = open("./Input/Names/invited_names.txt")

for name in names:
    letter.seek(0)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as send:
        for line in letter:
            send.write(line.replace("[name]", name.strip()))

names.close()
letter.close()