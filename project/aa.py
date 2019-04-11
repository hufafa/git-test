def main():
    while True:
        i = input("运算开始0结束，1开始：")
        if i == "0":
            break
        num1 = int(input("请输入第一个数字："))
        num2 = int(input("请输入第二个数字："))
        sum = num1 + num2
        print("努力运算中...sum:", sum)


if __name__ == '__main__':
    main()

