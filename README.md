# Cryptography Command Line Program

## Exercise 1 (Cryptography)

Cryptography is a method of protecting information and communications through the use of cypher or codes so that only those for whom the information is intended can read and process it. This involves both encryption and decryption of information. [Read more →](https://searchsecurity.techtarget.com/definition/cryptography)

### Description

This is a simple command-line program that encrypts and decrypts English alphabet letters using an integer as an encryption/decryption key.

This program can perform the following operations:

- Encrypt → convert information (plaintext) into a secret code (ciphertext)
- Decrypt → convert secret code (ciphertext) into information (plaintext)
- Accept encryption or decryption key
- Encrypt based on the encryption key provided by shifting each character forward on the English alphabet using encryption key e.g
  - encrypt “abcd” with the encryption key of  “1” should return “bcde”  
  - encrypt “abcd” with the encryption key of “5”  should return “efgh”
- Decrypt based on the decryption key provided by shifting each character backwards on the English alphabet using the decryption key e.g
  - decrypt “efgh” with the decryption key of “5” should return “abcd”
  - decrypt  “abcd” with the decryption key of “1” should return “zabc”

### How it Works

Your program is expected to behave in the following ways

- Clone repo and run this program
- Prompt user either she wants to encode (encrypt) or decode (decrypt)
- Prompt user to insert the plaintext to encode or ciphertext to decode
- Prompt user to insert the encryption/decryption key which must be an integer
- The program encodes the plaintext or decodes the ciphertext as the case may be
- Show the user the encoded text or decoded text
- Prompt the user if she want to go again
  - If user response was `No`:
    - The program should stop and thank the user for using the cryptography service
  - If user respond with `Yes`:
    - The program prompt the user either she wants to encode(encrypt) or decode (decrypt)
- The cycle continues...

### Constraints

- This program only encrypt or decrypt lowercased alphabet characters. Other characters should remain the same
- If no encryption/decryption key is provided the program defaults to zero


## Knowledge test Implementation (Dict Comprehension)

in this programe a function named `dict_comp` that takes in two integer values `stop` and `step` as arguments and returns a dictionary generated using python comprehensions is included, it has string string keys in the format `"items-#"` and values of type `list`, where each list is of length `step` and contains only integers. 

The integers within the list values will be sequentially generated, such that integers in a second list is a continuation of those in the first list and so on for others until we get to `stop` 

```python
# Expected output dictionary given that : stop = 10 and step = 4 

{
   "items-1": [ 1, 2, 3, 4 ],
   "items-2": [ 5, 6, 7, 8 ], 
}

```
