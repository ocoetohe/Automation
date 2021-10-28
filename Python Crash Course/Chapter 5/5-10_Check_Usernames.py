current_users = ['freddie', 'brian', 'roger', 'john', 'spike']

new_users = ['george', 'brian', 'JOHN', 'david', 'leon']

low = [x.lower() for x in new_users]

for current_user in current_users:
    if current_user in low:
        print(f"Sorry {current_user.title()} is already in use!")
    else:
        print(f"Adding {current_user.title()} to the list...")

print("\nUser list completed!")