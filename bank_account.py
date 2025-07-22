from datetime import datetime
import random

class Account:
    bank_name = "SC은행" # 은행 이름 선언 
    account_count = 0

    def __init__(self, owner, balance): #계좌 정보 저장
        self.owner = owner
        self.balance = balance
        self.account_number = self._make_account_number()
        self.deposit_count = 0
        self.deposit_history_list = []
        self.withdraw_history_list = []
        Account.account_count += 1

    def _make_account_number(self): # 계좌 번호 랜덤 생성 함수
        return f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(100000,999999)}"

    @classmethod #계좌 갯수 확인 함수
    def get_account_num(cls): 
        print(f"\n계좌 수: {cls.account_count}")

    def deposit(self, amount): #입금 함수
        if amount < 1:
            print("1원 이상만 가능합니다.")
            return
        self.balance += amount
        self.deposit_count += 1
        self.deposit_history_list.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount))
        if self.deposit_count % 5 == 0:
            self.balance += self.balance * 0.01

    def withdraw(self, amount): #출금 함수
        if amount > self.balance:
            print("잔액이 부족합니다.")
            return
        self.balance -= amount
        self.withdraw_history_list.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount))

    def display_info(self): #계좌 정보 출력 함수
        print("\n[계좌 정보]")
        print(f"은행: {self.bank_name}")
        print(f"예금주: {self.owner}")
        print(f"계좌번호: {self.account_number}")
        print(f"잔고: {int(self.balance):,}원")

    def deposit_history(self):# 입금 내역 출력 함수
        print(f"\n[{self.owner}의 입금 내역]")
        for dt, amt in self.deposit_history_list:
            print(f"{dt} - {amt:,}원")


    def withdrawal_history(self): # 출금 내역 출력 함수
        print(f"\n[{self.owner}의 출금 내역]")
        for dt, amt in self.withdraw_history_list:
            print(f"{dt} - {amt:,}원")



# 계좌 정보 입력
a1 = Account("a", 50000)
a2 = Account("b", 1200000)
a3 = Account("c", 990000)

accounts = [a1, a2, a3]

#입출금 입력
a1.deposit(10000)
a1.deposit(20000)
a1.deposit(30000)
a1.deposit(40000)
a1.deposit(50000)
a2.deposit(90000)
a3.deposit(80000)

a1.withdraw(100000)
a2.withdraw(100)
a3.withdraw(100000)

#100만원 이상 고객 출력
Account.get_account_num()

print("\n[잔고 100만원 이상 고객]")
for acc in accounts:
        if acc.balance >= 1000000:
            acc.display_info()

#입출금 내역 출력
a1.deposit_history()
a2.deposit_history()
a3.deposit_history()

a1.withdrawal_history()
a2.withdrawal_history()
a3.withdrawal_history()