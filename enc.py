from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
from ast import literal_eval
import numpy
import scipy.io.wavfile
#import math
d={"a":[],"b":[],"c":[],"d":[]}
rate, data = scipy.io.wavfile.read('cartoon008.wav')
print type(data[0])
leng=len(data)
key="dcab"
plaintext=''
o=0
j=121
for i in data:
        d[key[o%4]].append(str(i^j))
        o+=1
dat=";".join(d["a"])+";"+";".join(d["b"])+";"+";".join(d["c"])+";"+";".join(d["d"])
plaintext+=";".join(d["a"])+"#"+";".join(d["b"])+"#"+";".join(d["c"])+"#"+";".join(d["d"])
transdat=numpy.int16(numpy.array(map(int,filter(None,dat.split(";")))))
scipy.io.wavfile.write('trans.wav',rate,transdat)
plaintext+=";"+str(rate)
bs = Blowfish.block_size
key = b'DSAA PROJECT'
iv = Random.new().read(bs)
cipher = Blowfish.new(key, Blowfish.MODE_CBC,iv)
plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = iv + cipher.encrypt(plaintext + padding)
k=msg.encode('hex')
g=open("en.txt",'w')
g.write(k)
g.close()

