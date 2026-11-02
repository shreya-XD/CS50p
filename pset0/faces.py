def convert(a):
    a=a.replace(":)", "🙂")
    a=a.replace(':(', "🙁")
    return a

def main():
    b=input('enter text')
    print(convert(b))
main()

