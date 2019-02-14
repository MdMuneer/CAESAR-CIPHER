Max_key_size=26
def getMode():
      while True:
          print('Do you wish to encrypt or decrypt a message?')
          mode=input().lower()
          if mode in 'encrypt d'.split():
              return mode
          else:
              print('Enter either "encrypt"  or "e" or "decrypt" or "d".')
def getMessage():
    print('enter your message:')
    return input()
def getkey():
    key=1
    while True:
        print('Enter the key number (1-%s)' % (Max_key_size))
        Key=int(input())
        if (key >= 1 and key <= Max_key_size):
            return key

def  getTranslatedMessage(mode,message,key):
    if mode[0]=='d':
        key = -key
    translated=' '

    for symbol in message:
        if symbol.isalpha():
            num=ord(symbol)
            num+=key

            if symbol.isupper():
                if num>ord('z'):
                    num-=26
                elif num < ord('A'):
                    num+=26
            elif symbol.islower():
                if num>ord('z'):
                    num-=26
                elif num < ord('a'):
                    num +=26
            translated += chr(num)
        else:
            translated +=symbol
    return  translated

mode =getMode()
message=getMessage()
key=getkey()

print('your translated text is :')
print(getTranslatedMessage(mode, message, key))
