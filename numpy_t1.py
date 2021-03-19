from numpy import random,mat,eye
a = random.rand(4,4)
print(type(a),a)
randmat = mat(a)
print(type(randmat),randmat)
b = randmat.I
print(b)
c = randmat * b
print(c)
d = c -eye(4)
print(d)
print(eye(4))