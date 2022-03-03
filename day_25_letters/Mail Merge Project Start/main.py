#  TODO: Create a letter using starting_letter.txt

email = open(
    "C:\\Users\\sarah\\OneDrive\\Desktop\\100_days_of_code\\day_25_letters\\Mail Merge Project "
    "Start\\Input\\Letters\\starting_letter.txt",
    "r")
names = open(
    "C:\\Users\\sarah\\OneDrive\\Desktop\\100_days_of_code\\day_25_letters\\Mail Merge Project "
    "Start\\Input\\Names\\invited_names.txt",
    "r")

email_text = email.read()
lines = names.readlines()

for line in lines:
    line = line.strip()
    new_letter = f"C:\\Users\\sarah\\OneDrive\\Desktop\\100_days_of_code\\day_25_letters\\Mail Merge Project Start\\Output\\ReadyToSend\\{line}.txt"
    new_file = open(new_letter, "w+")
    new_file.write(email_text.replace("[name]", line))

    new_file.close()

email.close()
names.close()
