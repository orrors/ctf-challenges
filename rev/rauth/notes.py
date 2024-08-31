from Crypto.Cipher import Salsa20

key = b'ef39f4f20e76e33bd25f4db338e81b10'
nonce = b'd4c270a3'

# testing
# plaintext = b'aaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb'
# cipher = Salsa20.new(key=key, nonce=nonce)
# msg = cipher.encrypt(plaintext)
# print(msg)

# target ciphertext
msg = bytes.fromhex('05055fb1a329a8d558d9f556a6cb31f324432a31c99dec72e33eb66f62ad1bf9')
cipher = Salsa20.new(key=key, nonce=nonce)
plaintext = cipher.decrypt(msg)
print(plaintext)

