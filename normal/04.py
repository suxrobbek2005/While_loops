# 1 dan 100 gacha bo'lgan sonlarni kvadratlarini chiqaring.

# Natija: 1, 4, 9, 16, ..., 10000
securrence = 0
result = 1

print("1 dan 100 gacha bo'lgan sonlarning kvatrati\n")
while securrence < 100:
    securrence = securrence + 1
    result = securrence ** 2
    print(result, end=" ")
