unit_list = ["kg", "g", "L", "ml", "갯수"]

while True:
    setup = input("물건의 단위당 가격을 알아보시겠습니까? (네/아니요) : ")
    if setup == "아니요":
        print("그럼 종료하겠습니다. 이용해주셔서 감사합니다 :)")
        break
    unit = input("구입하려는 물건의 단위는 무엇인가요? (kg/g/L/ml/갯수) : ")
    while unit not in unit_list:
        print("잘못 입력하셨습니다. 다시 입력해주세요. : \n")
        unit = input("구입하려는 물건의 단위는 무엇인가요? (kg/g/L/ml/갯수) : ")
    item = float(input("구입하려는 물건의 용량은 어떻게 되나요? : "))
    price = float(input("구입하려는 물건의 가격은 얼마인가요? : "))

    total_price = price / item

    if unit == "g" or unit == "ml":
        total_price *= 100
        unit = "100" + unit

    print("\n해당 제품은 {}당 {}원입니다".format(unit, int(total_price)))
    print("소수점은 제거한 금액입니다 :)\n")


