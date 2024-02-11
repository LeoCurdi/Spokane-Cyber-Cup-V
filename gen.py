import bip32utils
import random

# Create the public key 
def generate_key(seed):
    bytes_seed = seed.to_bytes(32, 'big')
    key = bip32utils.BIP32Key.fromEntropy(bytes_seed)
    return key 

def find_private_key(target_address):
    seed = 0
    while True:
        key = generate_key(seed)
        address = key.Address()
        if address == target_address:
            return key.WalletImportFormat()
        seed += 1

target_address = '1PZE7KHa1Ujwd4jhUKNgUrjjtQeg7buSbM'
private_key = find_private_key(target_address)
print("Private Key:", private_key)
