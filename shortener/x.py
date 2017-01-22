import string, random

print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)
print(string.printable)

a = ''.join(random.choice(string.hexdigits) for x in range(7))
print(a)
for i in range(8):
    a = ''.join(random.choice('super') for x in range(5))
    print(a)
