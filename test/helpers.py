import ecdsa, codecs, hashlib, binascii
import base58

def hex_to_wif(hex_private_key, compressed=False):
    """
    Convert a hexadecimal private key to Wallet Import Format (WIF).
    """
    prefix = "80"
    suffix = "01" if compressed else ""
    extended_key = prefix + hex_private_key + suffix

    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
    final_key = extended_key + second_sha256[:8]

    wif = base58.b58encode(binascii.unhexlify(final_key)).decode('ascii')
    return wif

def wif_to_hex(wif_key):
    """
    Convert a compressed wif key to hexadecimal
    """
    decoded = base58.b58decode(wif_key).hex()
    hex_key = decoded[2:-10]
    return hex_key

def pvkhex_to_address_uncompressed(z):
    zk = ecdsa.SigningKey.from_string(codecs.decode(z, 'hex'), curve=ecdsa.SECP256k1)
    # zk_verify = zk.verifying_key

    z_public_key = b'\x04' + zk.verifying_key.to_string()

    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(z_public_key).digest())
    ripemd160_result = ripemd160.hexdigest()
    step3 = '00' + ripemd160_result

    second_sha256 = hashlib.sha256(binascii.unhexlify(step3)).hexdigest()

    third_sha256 = hashlib.sha256(binascii.unhexlify(second_sha256)).hexdigest()

    step6 = third_sha256[:8]

    step7 = step3 + step6

    btc_uncompressed_address_std = base58.b58encode(binascii.unhexlify(step7)).decode('utf-8')
    return btc_uncompressed_address_std


def pvkhex_to_address_compressed(z):
    pvk_to_bytes = codecs.decode(z, 'hex')

    key = ecdsa.SigningKey.from_string(pvk_to_bytes, curve=ecdsa.SECP256k1).verifying_key
    key_bytes = key.to_string()
    key_hex = codecs.encode(key_bytes, 'hex').decode('utf-8')

    if ord(bytearray.fromhex(key_hex[-2:])) % 2 == 0: public_key_compressed = '02' + key_hex[0:64]
    else:  public_key_compressed = '03' + key_hex[0:64]

    # Making SHA-256 of pubkey compressed and making RIPEMD-160 of this
    public_key_in_bytes = codecs.decode(public_key_compressed, 'hex')
    sha256_public_key_compressed = hashlib.sha256(public_key_in_bytes)
    sha256_public_key_compressed_digest = sha256_public_key_compressed.digest()

    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_public_key_compressed_digest)
    ripemd160_digest = ripemd160.digest()
    ripemd160_hex = codecs.encode(ripemd160_digest, 'hex')

    # Adding network bytes 0x00
    public_key_compressed_btc_network = b'00' + ripemd160_hex
    public_key_compressed_btc_network_bytes = codecs.decode(public_key_compressed_btc_network, 'hex')

    # Making Checksum for MainNet, this is SHA-256 2x turns and get the firsts 4 bytes
    sha256_one = hashlib.sha256(public_key_compressed_btc_network_bytes)
    sha256_one_digest = sha256_one.digest()
    sha256_two = hashlib.sha256(sha256_one_digest)
    sha256_two_digest = sha256_two.digest()
    sha256_2_hex = codecs.encode(sha256_two_digest, 'hex')
    checksum = sha256_2_hex[:8]
    btc_compressed_address_hex = (public_key_compressed_btc_network + checksum).decode('utf-8')

    btc_compressed_address = base58.b58encode(binascii.unhexlify(btc_compressed_address_hex)).decode(
            'utf-8')
    return btc_compressed_address
