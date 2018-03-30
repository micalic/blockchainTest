import hashlib
md5 = hashlib.md5()
md5.update('Python rocks!')
Traceback (most recent call last):
File "<pyshell#5>", line 1, in <module>
md5.update('Python rocks!')
TypeError: Unicode-objects must be encoded before hashing
md5.update(b'Python rocks!')
md5.digest()
b'\x14\x82\xec\x1b#d\xf6N}\x16*+[\x16\xf4w'