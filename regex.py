
def generate_variations(word):
    variations = [word]  # Start with the original word


    return variations


def main():
    # Read email addresses from file
    file_path = 'emails.txt'
    try:
        with open(file_path, 'r') as file:
            emails = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Define hacker variations including substitutions for 'a' and 'i'
    variations = ["admin"]
    for a in ('a', 'A', '4', '@'):
        for d in ('d', 'D',):
            for m in ('m', 'M'):
                for i in ('i', 'I', '1', '|'):
                    for n in ('n', 'N'):
                        new_word = ''.join([a, d, m, i, n])
                        variations.append(new_word)

    # Print all variations
    """     for variation in variations:
        print(variation) """

    # Filter email addresses that contain variations of "admin" before the "@" character
    filtered_emails = [email for email in emails if any(variation in email.lower().split('@')[0] for variation in variations)]

    # Filter variations to keep only those with 1 to 6 characters before '@' and 3 characters after '@'
    filtered_emails = [var for var in filtered_emails if len(var.split('@')[0]) in range(1, 7) and len(var.split('@')[1]) == 3]


    # Print all email addresses
    for email in filtered_emails:
        print(email)

    """ 
    Support_admiN@example.com
    office.admin@corporate-domain.com
    webadmin@web-domain.org
    aDm1n@email.org
    web.admin2@web-service.net
    admin@admin.com
    developer.aDmIn@example.net
    AdMin_spokane@company.org 
    
    44dm1n_su@server.com
    web.admin144@web-service.net
    123456AdMin123@company.org
    """

        # List of email addresses
    emails = [
        "44dm1n_su@server.com",
        "web.admin144@web-service.net",
        "123456AdMin123@company.org"
    ]

    # Calculate ASCII sum of email addresses
    total_sum = 0
    for email in emails:
        for char in email:
            total_sum += ord(char)

    print("ASCII sum of email addresses:", total_sum)

    total_sum = 0
    for email in emails:
        email_ascii_sum = sum(ord(char) for char in email)
        total_sum += email_ascii_sum
    
    print("ASCII sum of email addresses:", total_sum)

if __name__ == "__main__":
    main()