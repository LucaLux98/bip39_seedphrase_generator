# This is a tool to convert your entrophy in a secret phrase (24 words) for BTC;
import sys
import secrets
import hashlib

print("Welcome to the Seed Phrase Generator BIP-39!")
print("Attention! Before you begin, make sure that your device is disconected from the internet!")

def on_off_checks():       # ONLINE/OFFLINE CHECKS
    print("Did you start this program OFFLINE?")
    while True:
        A = int(input("1 = Yes, 0 = No: "))
        if A == 1:
            print("Perfect! Safety is guaranteed.\n")
            return True
        elif A == 0:
            print("ATTENTION: Turn OFF the internet before continue!")
            print("TURN OFF INTERNET AND TRY AGAIN!")
            print("Program closed \n")
            sys.exit()
        else:
            print("ERROR: Wrong input, try again:")
    
on_off_checks()     # CHECK LUNCH

def load_wordlist(filepath):       # LOADING WORDLIST BIP-39
    with open(filepath, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
        return words
    
wordlist = load_wordlist("wordlist/english.txt")
print(f"WORD LOADED: {len(wordlist)}\n")

def entropy_generator(bit=256):     # ENTROPY GENERATOR
    return secrets.token_bytes(bit//8)

entropy = entropy_generator(256)
print(f"ENTROPY:\n{entropy.hex()}\n")
print("DETAILS:")
print(f"BITs: {len(entropy)}")

def bits_conv(entropy):         # ENTROPY TO BITS CONVERSION
    return bin(int.from_bytes(entropy, "big"))[2:].zfill(len(entropy)*8)

entropy_bits = bits_conv(entropy)
print(f"\nBits conversion:\n{entropy_bits} \n")
print(f"Lenght: {len(entropy_bits)} bit")

def sha256_bits(data):      # SHA-256
    h = hashlib.sha256(data).digest()
    return bin(int.from_bytes(h, "big"))[2:].zfill(256)

hash_hex = hashlib.sha256(entropy).hexdigest()      # HEX HASH FROM SHA256
hash_bytes = hashlib.sha256(entropy).digest()       # BYTES HASH FROM SHA256
hash_bits = bin(int.from_bytes(hash_bytes, "big"))[2:].zfill(256)
print(f"SHA-256: {hash_hex}")
print(f"SIZE: {len(hash_hex)} char\n")

def get_checksum(hash_bits, entropy_bits):  # GETTING CHECKSUM
    checksum_length = len(entropy_bits) // 32
    return hash_bits[:checksum_length]

checksum = get_checksum(hash_bits, entropy_bits)
full_bits = entropy_bits + checksum
len(full_bits) == 264       # CHECKING LENGTH

chunks = [full_bits[i:i+11] for i in range(0, len(full_bits), 11)]
len(chunks) == 24

indices = [int(chunk, 2) for chunk in chunks]
all(0 <= i < 2048 for i in indices)

mnemonic = [wordlist[i] for i in indices]
phrase = " ".join(mnemonic)

input("\n Press ENTER to view your seed phrase.\n")
print(f"SEED PHRASE:\n \n {phrase} \n")
input("\n Press ENTER to end the program.\n")
