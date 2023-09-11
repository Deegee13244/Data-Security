import os
import random

def KeyGeneration(keyLength):
    #check if key length is valid (1-128)
    if (keyLength >= 1) and (keyLength <= 128):
        # make a random string of desired length with each value being 0 or 1
        key = ''.join(random.choice('01') for i in range(keyLength))
        #output key and save to newkey.txt
        print(key)
        newKeyFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'newkey.txt')
        f = open(newKeyFilePath, 'w')
        f.write(key)
        f.close()
    else:
        print('Invalid key length given')
        
    
if __name__ == '__main__':
    keyLength = input('Enter key length: ')
    KeyGeneration(int(keyLength))