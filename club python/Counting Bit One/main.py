
def countBitOne(num):
    count = 0;
    while (num > 0):
        if (num & 1) == 1:
            count += 1;
        num = num >> 1;
    return count



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(countBitOne(25)) # 11001
    print(countBitOne(6)) # 110
    print(countBitOne(1)) # 1
    print(countBitOne(0)) # 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
