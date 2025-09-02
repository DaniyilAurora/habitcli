def parse(command: str):
    output = command.strip().split(" ") # Remove spaces from command and split
    output[0] = output[0].lower() # Make the instruction to lower case
    return output