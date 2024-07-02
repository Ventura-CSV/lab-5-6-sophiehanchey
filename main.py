def printfunction1(*str):
    print(str)
    for v in str:
        print(v, end=' ')
    print()


def printfunction2(str):
    print(str)
    for v in str:
        print(v, end='')
    print()


def main():
    str = 'Python Programming'
    print('1')
    printfunction1(*str)
    print('2')
    printfunction1(str)
    print('3')
    printfunction2(str)

    print('4')
    morestr = 'C++ Programming'
    printfunction1(str, morestr)
    #printfunction2(str, morestr)  # Error


if __name__ == '__main__':
    main()
