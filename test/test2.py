import helpers as hs

privhex = "0000000000000000000000000000000000000000000000000000000017e2551e"

wif_key = hs.hex_to_wif(privhex)

print(wif_key)
