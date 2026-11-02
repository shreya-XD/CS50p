cc=input('camelCase:' )

for c in cc:
    if c.isupper():
        print('_' + c.lower(), end="")
    else:
        print(c, end="")
print()
