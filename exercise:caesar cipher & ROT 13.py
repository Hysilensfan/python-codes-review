# The caecer cipher encode and decode(only upper)
t = input();g = input();shift = int(input());r = ""
for i in t:
    if 'A' <= i <= 'Z' and g == "I wanna encode":
        r += chr((ord(i) - ord('A') + shift) % 26 + ord('A')) # Ek = ( m + k ) mod 26
    elif 'A' <= i <= 'Z' and g == "I wanna decode":
        r += chr((ord(i) - ord('A') - shift) % 26 + ord('A')) # Dk = ( m + k ) mod 26
    else:
        r += i
print(f"The caecer cipher encode is {r}" if g == "I wanna encode"else f"the caecer cipher decode is {r}")


# The ROT13 encode and decode(only upper)
from codecs import encode as QQ
t = input();r = ""
r = QQ(t,'rot_13')
print(f"The caecer cipher encode and decode is {r}")
