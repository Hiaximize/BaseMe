#!/usr/bin/env/ python 

import base64;
import re

#ANSII escape sequences for corresponding color
class bgColors:
    ok='\033[92m'
    ENDC='\033[0m'
    fail='\033[91m'
    warning='\033[93m' 

encodeDecode = input("Do you want to encode or decode? E or D> ")
print('\033c')

if encodeDecode == 'E' or encodeDecode == 'e': 

    encodeThis = input("what do you want to encode?> ")
    encoded_bytes = encodeThis.encode('ascii')

    #Base16 encode
    base16Encoded = base64.b16encode(encoded_bytes)

    #Base32 encode
    base32Encoded = base64.b32encode(encoded_bytes)

    #Base64 encode
    base64Encoded = base64.b64encode(encoded_bytes)

    #BaseA85 encode
    baseA85Encoded = base64.a85encode(encoded_bytes)

    #BaseB85 encode
    baseB85Encoded = base64.b85encode(encoded_bytes)

    #What are we encoding
    print('\n')
    print("Encoding: \n")
    print(" ", encodeThis,'\n')

    print('-'*70)
    print("encoded in base 16 is: \n\n", base16Encoded.decode('utf-8'))
    print('-'*70)
    # print('\n')
    print("encoded in base 32 is: \n\n", base32Encoded.decode('utf-8'))
    # print('\n')
    print('-'*70)
    print("endcoded in base 64 is: \n\n", base64Encoded.decode('utf-8'))
    # print('\n')
    print('-'*70)
    print("endcoded in base A85 is: \n\n", baseA85Encoded.decode('utf-8'))
    # print('\n')
    print('-'*70)
    print("endcoded in base B85 is: \n\n", baseB85Encoded.decode('utf-8'))
    # print('\n\n')
    print('-'*70)

elif encodeDecode == 'D' or encodeDecode == 'd':

    decodeThis = input("What to decode> ")

    try:

        #Base16 decode
        base16Decoded = base64.b16decode(decodeThis)
        print('-'*70)
        print('\n')
        print(f'Decoded in base16 is: \n\n{bgColors.ok}{base16Decoded}{bgColors.ENDC}\n')
        # print('Decoded in base 16 is: \n\n', base16Decoded, '\n')
        print('-'*70)
        print('\n')
    except:
        print(f"{bgColors.fail}It wasn't Base16{bgColors.ENDC}")
    
    try:

        #Base32 decode
        base32Decoded = base64.b32decode(decodeThis)
        print('-'*70)
        print('\n')
        print(f'Decoded in base32 is: \n\n{bgColors.ok}{base32Decoded}{bgColors.ENDC}\n')
        # print('Decoded in base 32 is: \n\n', base32Decoded, '\n')
        print('-'*70)
        print('\n')
    except:
        print(f"{bgColors.fail}It wasn't Base32{bgColors.ENDC}")

    try:

        #Base64 decode
        base64Decoded = base64.b64decode(decodeThis)
        print('-'*70)
        print('\n')
        print(f'Decoded in base64 is: \n\n{bgColors.ok}{base64Decoded}{bgColors.ENDC}\n')
        # print('Decoded in base 64 is: \n\n', base64Decoded.decode('utf-8'), '\n')
        print('-'*70)
        print('\n')
    except:
        print(f"{bgColors.fail}It wasn't Base64{bgColors.ENDC}")

    try:

        #BaseA85 decode
        baseA85Decoded = base64.a85decode(decodeThis)
        print('-'*70)
        print('\n')
        print(f'Decoded in baseA85 is: \n\n{bgColors.ok}{baseA85Decoded}{bgColors.ENDC}\n')
        # print('Decoded in baseA85 is: \n\n', baseA85Decoded, '\n')
        print('-'*70)
        print('\n')
    except:
        print(f"{bgColors.fail}It wasn't BaseA85{bgColors.ENDC}")

    try:
    
        #BaseB85 decode
        baseB85Decoded = base64.b85decode(decodeThis)
        print('-'*70)
        print('\n')
        print(f'Decoded in baseB85 is: \n\n{bgColors.ok}{baseB85Decoded}{bgColors.ENDC}\n')
        print('-'*70)
        print('\n')
    except:
        print(f"{bgColors.fail}It wasn't BaseB85{bgColors.ENDC}")