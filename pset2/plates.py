def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if not s.isalnum():
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_started=False
    first_number=None

    for ch in s:
        if ch.isalpha():
            if number_started:
                return False
        else:
            if not number_started:
                number_started=True
                first_number=ch
            else:
                first_number+=ch

    if number_started and first_number[0]=='0':
        return False

    return True





main()
