import ecdsa
import random
import hashlib
gen=ecdsa.NIST256p.generator
rank=gen.order()
privateKey = random.randrange(1,rank-1)
publicKey = ecdsa.ecdsa.Public_key(gen,gen * privateKey)
private_key = ecdsa.ecdsa.Private_key(publicKey,privateKey)
message = "sunzehan's power."
m = int(hashlib.sha1(message.encode("utf8")).hexdigest(),16)
k = random.randrange(1,rank-1)
signature = private_key.sign(m,k)
r = signature.r
s = signature.s
