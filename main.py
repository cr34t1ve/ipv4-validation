while True:
    # Prompt a user to enter an IPv4 address in dotted decimal notation or “quit” to exit
    ip_address = input("Enter an IPv4 address in dotted decimal notation or 'quit' to exit: ")

    if ip_address.lower() == "quit":
        break

    # Use the split() method to split the IP address into octets
    octets = ip_address.split(".")

    # Check that the IP address is valid (it must be 4 octets and each octet must be between 0 and 255)
    if len(octets) != 4:

    # Print out the following information:
        print("Invalid IP address. It must contain 4 octets.")
        continue
    valid = True
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            valid = False
            break
    if not valid:
        print("Invalid IP address. Each octet must be between 0 and 255.")
        continue
    print("IP address:", ip_address)
    print("Octets:", octets)