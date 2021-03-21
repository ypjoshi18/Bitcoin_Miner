import hashlib

NONCE_LIMIT = 100000000

zeroes = 6
# print(hashlib.sha256("Hello World".encode()).hexdigest())

def mine(block_number, transcations, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transcations + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f"Found Hash With Nonce: {nonce}")
            return hash_try
    return -1

block_number = 24
transcations = "76123fcc2142"
previous_hash = "876de875b967c87"

# mine(block_number, transcations, previous_hash)

combined_text = str(block_number) + transcations + previous_hash + str(19504164)

print(hashlib.sha256(combined_text.encode()).hexdigest())
