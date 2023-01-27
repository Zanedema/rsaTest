import numpy
import random as r

def mmi(x, y):  # modular multiplicative inverse
    for i in range(0, y):
        d = (x * i) % (y)
        if (d % y == 1):
            return i
    return -1

def primeDecide():
    solutionNotFound = True
    while solutionNotFound:
        n = r.randrange(3, 1000, 2) #odd numbers
        if (2**n-1)%n == 1:
            solutionNotFound = False
        else:
            n - 2

    return n

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


def encrypt(msg, e, n):
    enc = []
    for i in range(0, len(msg)):
        enc.append(pow(msg[i], e) % n)
    return enc


def decrypt(msg, d, n):
    dec = []
    for i in range(0, len(msg)):
        dec.append(pow(msg[i], d) % n)
    return dec


message = "Hello, world! I can send really long messages, or really short messages! No matter the size, three clever primes shall keep me safe!"
a = proc(message)

e = 65537  # public prime
p = primeDecide()  # two primes, private.
q = primeDecide()

n = p * q  # public
Φ = numpy.lcm(p - 1, q - 1)  # Carmichael's toitent, private. if gcd(Φ, e) != 1, pick a different p or q
d = mmi(e, Φ)  # private

encrypted = encrypt(a, e, n)
decrypted = decrypt(encrypted, d, n)
dS = procInverse(decrypted)

print("message = " + message)
# print("encoded = " + str(a))
# print("encrypted = " + str(encrypted))
# print("decrypted = " + str(decrypted))
#print("decrypted message = " + dS)
