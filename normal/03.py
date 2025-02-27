# oddNumber = 0

# print("1 dan 100 gacha bo'lgan sonlarning faqat toqlari qatori")
# while oddNumber < 100:
#     oddNumber = oddNumber + 1
#     if oddNumber % 2 == 1:
#         print(oddNumber)


def oddNumber():
    num  = int(input("Qaysi songacha toq sonlar chiqsin "))
    number = 0
    while number < num:
        number = number + 1
        if number % 2 == 1:
            print(number)


oddNumber()
