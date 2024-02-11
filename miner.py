import requests
from hashlib import sha256
import random
import string

ip = "binary1.spokane-ctf.com"
port = "10001"

# Hash an arbitrary string for us
def hash_data(string):
	return sha256(string.encode('utf-8')).hexdigest()

def only_zeros(hash, amount):
	
	for i in range(amount):
		if(hash[i] != "0"):
			return False
	return True

def get_attempt():
	response = requests.get("http://{}:{}/question".format(ip,port)).json()
	return response

def send_attempt(req_id, nonce):	
	response = requests.get("http://{}:{}/answer?proof_id={}&nonce={}".format(ip,port,req_id,nonce))
	return response.json()

'''
Modify THIS function. 
Everything else is already done for you

Goal is to find a hash with lots of zeros at the front by prepending data to it. 
For instance, we have the string 'AAAA'. 
Hash the string 'AAAA' to have 7 zeros at the front. 
To do this, add a string to the beginning of it. 
For instance, '11111' + 'AAAA' = '11111AAAA' as the string being hashed. 
Eventually, the hashed string will have enough zeros. Exit at this point, since 
the work has been done.
'''
def calc_hash(data, diff):
    while True:
        nonce = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))  # Generate a random 5-character string
        hash_result = hash_data(nonce + data)  # Prepend nonce to data and hash
        if only_zeros(hash_result, diff):  # Check if the hash has the required number of leading zeros
            return nonce
		

# Get the information from the server for us to prove
proof_data = get_attempt()
difficulty = proof_data['difficulty']
data_to_prove = proof_data['data']
req_id = proof_data['proof_id']

# TODO - find hash here
nonce = calc_hash(data_to_prove, difficulty) 

# Makes a request to the server to send the nonce
print(send_attempt(req_id, nonce))

