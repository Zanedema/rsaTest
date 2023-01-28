import numpy
import random as r
from multiprocessing import Pool

def mmi(x, y):  # modular multiplicative inverse
    for i in range(0, y):
        d = (x * i) % (y)
        if (d % y == 1):
            return i
    return -1

def primeAuditor(vector, e):
    if numpy.gcd(numpy.lcm(vector[0] - 1, vector[1] - 1), e) != 1:
        print("prime decide again")
        return primeAuditor(primeDecide())
    else:
        return vector

def primeDecide():
    solutionVector = []
    for i in range(2):
        solutionNotFound = True
        while solutionNotFound:
            n = r.randrange(3, 1000, 2) #odd numbers
            if (2**n-1)%n == 1:
                solutionNotFound = False
                solutionVector.append(n)
            else:
                n - 2
    return solutionVector

def proc(a):
    split = list(a)
    for i in range(0, len(split)):
        split[i] = ord(split[i])
    return split


def procInverse(a):
    undone = ""
    for i in range(0, len(a)):
        undone += (chr(a[i]))
    return undone

def encryptWorker(a):
    if __name__ == '__main__':
        with Pool(5) as p:
            v = p.map(encrypt, a)
            p.close()
            p.join()
            return v

def decryptWorker(a):
    if __name__ == '__main__':
        with Pool(5) as p:
            v = p.map(decrypt, a)
            p.close()
            p.join()
            return v

def encrypt(v):
    return pow(v, e) % n

def decrypt(v):
    return pow(v, d) % n


message = "Hello, world! I can send really long messages, or really short messages! No matter the size, three clever primes shall keep me safe!"
a = proc(message)

e = 65537  # public prime
p, q = primeAuditor(primeDecide(), e) #two primes, private

n = p * q  # public
Φ = numpy.lcm(p - 1, q - 1)  # Carmichael's toitent, private. if gcd(Φ, e) != 1, pick a different p or q
d = mmi(e, Φ)  # private

encrypted = encryptWorker(a)

if(encrypted!=None):
    #decrypted = decryptWorker(encrypted)
    #dS = procInverse(decrypted)

    #print("message = " + message)
    print(p, q, d, n)
    print("encoded = " + str(a))
    print("encrypted = " + str(encrypted))
    #print("decrypted = " + str(decrypted))
    #print("decrypted message = " + dS)
