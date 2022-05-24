name = input()
password = input()

current_password = password
while current_password != password:
    password = input()

print(f"Welcome {name}!")
