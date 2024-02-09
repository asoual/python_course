with open ("input/names/invited_names.txt", "r") as names:
    list_invited_names = names.readlines()
    invited_names = [elem.strip("\n") for elem in list_invited_names]

with open ("input/letters/starting_letter.txt") as data:
    mail = data.read()
    for i in invited_names:
        mail_names = mail.replace("[name]" , i)
        with open (f"output/readytosend/{i}_letter.txt", "w") as readytosend:
            readytosend.write(mail_names)
