
squre = 0
result = 1

print("Ikkining kvatrati 2 dan oshmagan holati\n")
while squre < 1000:
    squre = squre + 1
    result = 2 ** squre 
    if result < 1000:
        print(result)