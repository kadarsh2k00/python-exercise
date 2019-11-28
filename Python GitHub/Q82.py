import zlib
s="hello world!hello world!hello world!hello world!"
s1=zlib.compress(s.encode())
print(s1)
print(zlib.decompress(s1))
