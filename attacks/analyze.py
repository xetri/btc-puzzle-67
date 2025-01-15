import base58
import hashlib
import config
import helpers as hs

# comp_addr = config.metas[0][2][0]

#8:f 0000000000000000000000000000000000000000000000000000000000000008 
exHex = 0x8
exAddr = "1EhqbyUMvvs7BfL8goY6qcPbD6YKfPqb7e" 

exPvKeyComp = "KwDiBf89QgGbjEhKnhXJuH7LrciVrZi3qYjgd9M7rFU77MfhviY5"
hex_key = hs.num_to_hex64(exHex)
exPubKeyComp = hs.pvhex_to_comp_pubkey(hex_key)

print(exPubKeyComp)


# Decode the base58 address
raw_bytes = base58.b58decode(exAddr)

# Extract the version byte and public key hash
version_byte = raw_bytes[0]
public_key_hash = raw_bytes[1:-4]

# Construct the full hex representation
full_hex = f"0x{version_byte:02x}{''.join(f'{b:02x}' for b in public_key_hash)}"

print(f"Full hex representation: {full_hex}")


# Decode the base58 address
# raw_bytes = base58.b58decode(comp_addr)

# Extract the version byte and public key hash
# version_byte = raw_bytes[0]
# public_key_hash = raw_bytes[1:-4]

# Construct the full hex representation
# full_hex = f"{version_byte}x{''.join(f'{b:02x}' for b in public_key_hash)}"

# print(f"Full hex representation: {full_hex}")
