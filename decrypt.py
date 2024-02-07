# script to decrypt the congratulations message
# key would be everything in your gmail before the '@'


import base64

# pass in the message
message=b'H0YBBwYNCwAaSUdSREYVAAAPGlRFTkALCw0eFwQJGxZOTl1IQwQBBgALAxYNSUtIQwQUFAocGgBO\nTl1IQwgcERcLChoLAgJPSEFVEwYGBxYfCwoNChVVUl9OSQYHAggLDwQWVUlOSQEIDAUBEBJVUl9O\nSQAICAJPSEFVFAoBSVNTTkAfDQ9TVRg='

# everything in your gmail before the @
key='your_username'

# list to store the decrypted message
decrypted_message=[]

# decode the key to base64 bytes
dec_bytes=base64.b64decode(message)

# XOR with key
for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

# print message
print("".join(decrypted_message))