def main():
    time=convert(input('What is the time?'))

    if 7<=time<=8:
        print('Breakfast Time')
    elif 12<=time<=13:
        print('Lunch Time')
    elif 18<=time<=19:
        print('Dinner Time')
    else:
        print('')

def convert(t):
    hours, mins=t.split(":")
    return float(hours)+float(mins)/60


if __name__ == "__main__":
    main()
