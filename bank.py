from SaveManager import SaveManager
from datetime import datetime
import sys

saveManager = SaveManager()

account = saveManager.Load()

money = account["money"]

def SetMoney(value):
    global money 
    money += value

def MainMenu():
    print("프로그램 실행 시 아래와 같은 메뉴를 출력한다.\n\n")
    print("========================\n은행 계좌 관리 프로그램\n========================\n\n")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액 내역")
    print("4. 거래 내역 조회")
    print("5. 종료\n")

def IsInput(value):
    if value.strip() == "":
        return False

    elif not value.isdigit():
        return False

    return True

def IsInputRange(value):
    value = int(value)
    return 0 < value <= 5

def Menu(value):
    value = int(value)
    match value:
        case 1:
            Deposit()
        case 2:
            Withdrawal()
        case 3:
            BalanceInquiry()
        case 4:
            History()
        case 5:
            Exit()

def Deposit():
    print("입금 금액을 적어 주세요.")
    deposit = input()

    if IsInput(deposit) and int(deposit) > 0:
        print(f"입금 금액 : {deposit}")
        deposit = int(deposit)
        SetMoney(deposit)

        account["money"] = money

        AddHistory("입금", deposit)

        saveManager.Save(account)

        print(format(deposit,',') + "원이 압금되었습니다.")

    else :
        print("잘못 입력 됬습니다.")

def Withdrawal():
    print("출금 금액을 적어 주세요.")
    Withdrawal = input()
    if IsInput(Withdrawal) and int(Withdrawal) > 0:
        Withdrawal = int(Withdrawal)
        if IsWithdrawal(Withdrawal) :
            print(f"출금 금액 : {Withdrawal}")
            SetMoney(-Withdrawal)

            account["money"] = money

            AddHistory("출금", Withdrawal)

            saveManager.Save(account)

            print(format(Withdrawal,',') + "원이 출금되었습니다.")

        else :
            print("현재 잔액이 부족합니다.")
    else :
        print("잘못 입력 됬습니다.")

def BalanceInquiry():
    print("현재 잔액")
    print(format(money,',') + "원")

def History():
    print("거레 내역 조회")
    print("----------------------------")
    for history in account["history"]:
        print(f"[{history["day"]}]")
        print(history["menu"])
        print(format(history["amount"],','))
        print("----------------------------")

def Exit():
    saveManager.Save(account)
    sys.exit()

def IsWithdrawal(value):
    return value <= money

def AddHistory(menu, amount):
    account["history"].append({
        "day": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "menu": menu,
        "amount": amount
    })

    
while True:
    MainMenu()
    userInput = input()

    if IsInput(userInput) and IsInputRange(userInput):
        Menu(userInput)
    else :
        print("잘못된 입력입니다.")