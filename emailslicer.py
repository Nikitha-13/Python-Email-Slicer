# Code to take input(Email) from user
email = input("Enter Your Email: ").strip()

# Slicing the Email
username = email[ :email.index("@")]
domain_name = email[email.index("@")+1:]

# Formatting the sliced Email in understandable way
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")

# Printing the output
print(format_)
