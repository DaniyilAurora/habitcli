import messages
import parser
from database import Database

# Initialise database
db = Database()

command = input(messages.input)

while command != "-1" and command != "exit":
    command = parser.parse(command)
    print(command)

    # Check if command is valid
    if command[0] == "":
        print(messages.invalid_command)
    
    # Add a habit
    if command[0] == "add" and len(command) > 1:
        print(messages.add_habit)
    elif command[0] == "help":
        print("Help: \n - add '<habit>' <time> <how often>, Example: add 'Do Sport' 12:00 1d")
    else:
        print(messages.invalid_command)

    # ask for a new command
    command = input(messages.input)

print(messages.exit)