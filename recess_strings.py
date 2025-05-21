import re
x = 2
y = "pencils"
z = (f"I have {x} total {y}")
print(z)

txt = "  Hello,   Uganda!   "
#txt = txt.strip().replace(" ", " ")
txt = re.sub(r'\s+', '', txt)
print(txt)
txt = txt.upper()
print(txt)
txt = txt.replace("U", "V")
print(txt)

Y = "I am proudly Ugandan"
print(Y[2:5])

X = 'All "Data Scientists" are cool!'
print(X)