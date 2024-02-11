def decode_command_code(command):
    # Extract the bytes representing the command code
    command_code_bytes = command[9:12]

    # Convert the bytes to a single integer (command code)
    command_code = int.from_bytes(command_code_bytes, byteorder='big')

    # Format the command code as 'TPM_CC_XXXXXXX'
    command_code_name = f'TPM_CC_{command_code:07X}'

    return command_code_name

def main():
    # Command data
    command = [0x80, 0x1, 0x0, 0x0, 0x0, 0xC, 0x0, 0x0, 0x1, 0x7b, 0x0, 0x4]

    # Decode the command code
    command_code_name = decode_command_code(command)

    # Print the command code name (the flag)
    print("Command Code Name:", command_code_name)

if __name__ == "__main__":
    main()