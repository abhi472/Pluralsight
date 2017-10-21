listNum = reversed(range(1, 9))
result = 0
for i in listNum:
    for j in listNum:
        for k in listNum:
            num = 9091 * i + 910 * j + 100 * k
            for l in reversed(range(10, 90)):
                if (num % l) == 0:
                    if (num / l) > 999:
                        break
                    else:
                        result = num * 11
                        print(result)
                else:
                    break
