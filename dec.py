from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
from ast import literal_eval
import numpy
import scipy.io.wavfile
import re
#Decryption
bs=8
key=b'DSAA PROJECT'
f=open('en.txt','r')
k=f.read()
f.close()
ciphertext=k.decode('hex')
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]
cipher = Blowfish.new(key, Blowfish.MODE_CBC,iv)
msg = cipher.decrypt(ciphertext)
last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
rate=int(msg[len(msg)-msg[::-1].index(";")+1:])
msg=msg[:len(msg)-msg[::-1].index(";")]
#converting message to audio
l=map(str,filter(None,msg.split("#")))
p=[]
for i in range(len(l)):
    print filter(None,l[i].split(";"))
    p.append(map(int,filter(None,l[i].split(";"))))
l=map(None,p[3],p[2],p[0],p[1])
final=[]
m=121
for i in l:
    for j in i:
        if j!=None:
            final.append(j)
l=numpy.int16(numpy.array(final))
scipy.io.wavfile.write('dec.wav',rate,l)
