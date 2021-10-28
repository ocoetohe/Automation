usernames = ['admin', 'barry', 'robin', 'maurice']

for username in usernames:
    if 'admin' in username:
        print(f"Hello {username.title()}, would you like to see a status report?.")
    else:
        print(f"Hello {username.title()}, thank you for logging again!")
