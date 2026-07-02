memberships = []

print("Give me the membership info for all members. type 'quit' when done. ")

while True:
    membership_name = input("What is the members name? ").title()
    if membership_name == "Quit":
        break
    membership_bday = input("What is the members birthday? (mm/dd/yy) ")
    membership_record_number = input("What is the members membership record number? ")
    memberships.append([membership_name, membership_bday, membership_record_number])

for record in memberships:
    print(record[0])
    print(record[1])
    print(record[2])
    print()