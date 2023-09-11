import os

def Decrypt():
    #specifying relative file paths
    keyFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'key.txt')
    plainTextFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'result.txt')
    cipherTextFilePath = os.path.join(os.path.dirname(__file__), '..', 'data', 'ciphertext.txt')
    #read key and ciphertext
    sk = open(keyFilePath).read()
    c = open(cipherTextFilePath).read()
    #if the length of the ciphertext and secret key don't match, throw error
    if len(sk) != len(c):
        print("Error: Length is Incorrect")
    else:
        part1 = ''
        part2 = ''
        part3 = ''
        part4 = ''
        #XOR operation, similar to ecryption function
        x = [abs(int(sk[i]) - int(c[i])) for i in range(len(sk))]
        #binary string is split up into 4 parts
        for i in range(len(x)):
            if i < 8:
                part1 += str(x[i])
            elif i < 16:
                part2 += str(x[i])
            elif i < 24:
                part3 += str(x[i])
            elif i < 32:
                part4 += str(x[i])
        #translate into plain text and concatinate parts of binary string
        m = chr(int(part1, 2)) + chr(int(part2, 2)) + chr(int(part3, 2)) + chr(int(part4, 2))
        #output plain text and write to appropriate file
        print('Plain text is: ' + m)
        f = open(plainTextFilePath, 'w')
        f.write(m)
        f.close()
        
if __name__ == '__main__':
    Decrypt()