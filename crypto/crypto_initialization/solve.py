known_plaintext = 'This is some public information that can be read out loud.'
encrypted_text = bytes.fromhex('76ca21043b5e471169ec20a55297165807ab5b30e588c9c54168b2136fc97d147892b5e39e9b1f1fd39e9f66e7dbbb9d8dffa31b597b53a648676a8d4081a20b')
encrypted_flag = bytes.fromhex('6af60a0c6e5944432af77ea30682076509ae0873e785c79e026b8c1435c566463d8eadc8cecc0c459ecf8e75e7cdfbd88cedd861771932dd224762854889aa03')

# Convert known_plaintext to bytes
known_plaintext_bytes = known_plaintext.encode()

# Perform XOR operations
result = bytes(x ^ y ^ z for x, y, z in zip(known_plaintext_bytes, encrypted_text, encrypted_flag))

# Print the result as a hexadecimal string
result_hex = result.hex()
print(bytes.fromhex(result_hex))
