import re

# 물건의 단위
unit_list = ["kg", "g", "L", "ml", "갯수"]

print('''안녕하세요! 가격 비교 프로그램 짠순봇2 입니다
사용법을 설명해드릴게요 :D

1. 구입하려는 물건의 단위를 입력합니다. (kg, g, L, ml, 갯수 중 선택)
대소문자와 한글을 구별해서 정확하게 입력해주세요!

2. 구입하려는 물건의 이름을 입력합니다.
플랫폼도 함께 입력하면 좋아요! (ex. 네이버 크림빵)

3. 구입하려는 물건의 가격을 입력합니다.
가격은 숫자만 입력 가능해요. (ex. 3000)
만약 별도의 택배비가 있다면, 합쳐서 입력해주세요!

4. 여러개의 물건을 입력하시려면 1~3번을 반복합니다.

5. 물건 입력이 끝나면, 입력하신 물건들 중에서 가장 저렴한 물건을 알려드립니다.
짠순봇2로 가장 저렴한 물건을 찾아 합리적으로 쇼핑해보세요!
''')

while True:
    
    # 물건의 단위, 이름, 가격 정보
    unit = ""
    item = []
    total_price = [] # 물건의 총 가격
    unit_price = [] # 물건의 단위당 가격

    # 물건의 단위 입력하기
    unit = input("물건의 단위는 무엇인가요? (kg, g, L, ml, 갯수 중 선택) : ")
    print("")
    while unit not in unit_list:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        unit = input("물건의 단위는 무엇인가요? (kg, g, L, ml, 갯수 중 선택) : ")
        print("")

    # 물건의 이름, 용량, 가격 입력하기
    while True:
        item.append(input("물건의 이름이 무엇인가요? : "))
        volume = float(input("물건의 용량은 어떻게 되나요? : "))
        value = int(input("물건의 가격은 얼마인가요? : "))
        print("")

        price = int(value / volume)

        if unit == "g" or unit == "ml":
            price *= 100
            unit = "100" + unit
        
        total_price.append(value)
        unit_price.append(price)

        setup = input("가격 비교할 물건을 추가로 입력하시겠습니까? (Y/N) : ")
        print("")

        while setup != "Y" and setup != "N":
            print("잘못 입력하셨습니다. 다시 입력해주세요!")
            setup = input("가격 비교할 물건을 추가로 입력하시겠습니까? (Y/N) : ")
            print("")

        if setup == "N":
            break

    # 가장 저렴한 물건의 값 / 가장 저렴한 물건은 몇 개인가?
    min_price = min(unit_price)
    min_count = unit_price.count(min(unit_price))
    min_index = unit_price.index(min_price)
    min_indexs = []

    # 가장 저렴한 물건 알려주기
    if min_count == 1:
        print("입력한 물건 중 가장 저렴한 물건은 {}로(으로)".format(item[min_index]))
        print("{}당 가격은 {}원입니다.".format(unit, unit_price[min_index]))
        print("")
    else:
        print("가장 저렴한 물건이 여러개입니다.")
        print("")
        min_indexs = list(filter(lambda x : unit_price[x] == min_price, range(len(unit_price))))
        for i in min_indexs:
            print("입력한 물건 중 가장 저렴한 물건은 {}로(으로)".format(item[i]))
            print("{}당 가격은 {}원입니다.".format(unit, unit_price[i]))
            print("")
            

    # 다른 물건의 가격 알려주기
    other = input("입력한 다른 물건의 가격도 알려드릴까요? (Y/N) : ")
    print("")

    while other != "Y" and other != "N":
        print("잘못 입력하셨습니다. 다시 입력해주세요!")
        other = input("입력한 다른 물건의 가격도 알려드릴까요? (Y/N) : ")
        print("")
    
    if other == "Y":
        if min_count == 1:
            unit_price[min_index] = -1
        else:
            for i in min_indexs:
                unit_price[i] = -1
        if len(item) >= 1:
            if unit_price.count(-1) != len(unit_price):
                for x, y in zip(item, unit_price):
                    if y > 0:
                        print("{}의 {}당 가격은 {}원입니다.".format(x, unit, y))
                    else:
                        pass
                print("소수점은 모두 제외한 금액입니다.")
                print("")
            else:
                print("입력한 다른 물건이 없습니다.")
                print("")
        else:
            print("입력한 다른 물건이 없습니다.")
            print("")

    # 계속 할건지 묻기
    edit_exit = input("가격 비교가 끝났습니다! 다른 물건도 비교해보시겠어요? (Y/N) : ")
    print("")

    while edit_exit != "Y" and edit_exit != "N":
        print("잘못 입력하셨습니다. 다시 입력해주세요!")
        edit_exit = input("가격 비교가 끝났습니다! 다른 물건의 가격도 비교해보시겠어요? (Y/N) : ")
        print("")

    if edit_exit == "N":
        print("그럼 종료하겠습니다. 이용해주셔서 감사합니다 :D")
        print("")
        break

