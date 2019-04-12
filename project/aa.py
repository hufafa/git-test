def main():
    while True:
        i = input("运算开始0结束，1开始：")
        if i == "0":
            break
        num1 = int(input("请输入第一个数字："))
        operator = input("请输入+、-、*、/：")
        num2 = int(input("请输入第二个数字："))
        if operator == "+":
            print(f"你进行了加发运算，拼命运算中...{num1 + num2}")
        elif operator == "-":
            print(f"你进行了减法运算，拼命运算中...{num1 - num2}")
        elif operator == "*":
            print(f"你进行了乘法运算，拼命运算中...{num1 * num2}")
        elif operator == "/":
            print(f"你进行了除法运算，拼命运算中...{num1 / num2}")
        else:
            print("请好好输入运算符~")


if __name__ == '__main__':
    main()
    print("where are you from")
