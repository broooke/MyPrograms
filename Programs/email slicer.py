email = input("Enter the mail: ")

name = email[:email.index("@")]
domain = email[email.index("@")+1:]
print(f"You name is {name}, domain {domain}")