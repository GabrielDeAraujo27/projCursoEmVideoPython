def maior(*list):
    if list[0]>list[1]:
        m = list[0]
    else:
        m = list[1]
    print(f'O maior número entre {list[0]} e {list[1]} é {m}')


maior(24,9)
maior(89, 4)
maior(4,5)
maior(-8,-2)
maior(-2,17)