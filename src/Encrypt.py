import os

def Encrypt():
    #specifying relative file paths
    keyFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'key.txt')
    plainTextFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'plaintext.txt')
    cipherTextFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'ciphertext.txt')
    #read key and plaintext
    sk = open(keyFilePath).read()
    m = open(plainTextFilePath).read()
    mbinary = ""
    #convert plain text to binary
    for i in range(len(m)):
        mbinary += (bin(ord(m[i])).replace("b", ""))
    #ensure length is same as secret key
    if len(mbinary) == len(sk):
        #get absoulte value of difference between each character of the secret key and binary string, essentially XOR
        x = [abs(int(sk[i]) - int(mbinary[i])) for i in range(len(sk))]
        #assemble into a string of ciphertext
        cipherText = ''.join(map(str, x))
        #output ciphertext and write to appropriate file
        print('Ciphertext: '+ cipherText)
        f = open(cipherTextFilePath, 'w')
        f.write(cipherText)
        f.close()
    else:
        #length was not the same as secret key, clear any contents of ciphertext.txt
        print('Error: Length is Incorrect')
        f = open(cipherTextFilePath, 'w')
        f.write('')
        f.close()
        
if __name__ == '__main__':
    Encrypt()