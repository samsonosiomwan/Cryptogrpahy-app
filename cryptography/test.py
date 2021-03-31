from art import art




  
#algotithm to encrypt and decript
#keys: d_e_code:decrypt_encrypt_code, e_text:encrypt_text
def cryptography(d_e_code,e_text,key):
    '''
    encrypt function
    d_e_code:decrypt_encrypt_code, e_text:encrypt_text,key
    '''
    transverse = ''

    for text in e_text:
        if ord(text) > 122 or ord(text) < 96:
            transverse += text
        else: 
            if d_e_code == "encode":
                transverse_text = ord(text) + int(key)
                if transverse_text > 122:
                    transverse_text = (transverse_text % 122) + 96
                transverse += chr(transverse_text)
            elif d_e_code == "decode":
                transverse_text = ord(text) - int(key)
                if transverse_text < 97:
                    transverse_text = 122 - (96 - transverse_text)
                transverse += chr(transverse_text)
    return f'this is your entry message: {transverse}' 
        
while True:
    print(art)
    decode_encode = input("do you want to encode or decode: ")
    try:
        
        if decode_encode == 'encode' and decode_encode == 'decode':
          continue
          
          
    except ValueError:
        print('please type use \'encode\' to encode and \'decode\' to decode ')
        # else:
        #     break
        
            # decode_encode = input("Error:")
    # enter_text = input("enter text: ")
    enter_key = input('enter key: ')
    if enter_key == "":
        enter_key = 0


    print(cryptography(decode_encode,enter_text,enter_key))

    yes_no = input("enter yes to encript again or no to exit: ")
    if yes_no == 'yes':
        continue
    elif yes_no == 'no':
        break

  
# cryptography()
