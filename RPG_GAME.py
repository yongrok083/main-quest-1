import random

class Character: #캐릭터 정보 저장
    def __init__(self, name, level, hp, atk, df):
        self.name = name
        self.level = level
        self.hp = hp
        self.atk = atk
        self.df = df

    def is_alive(self): #hp 생존 함수 
        return self.hp > 0 

    def take_damage(self, dmg):  #데미지 처리 함수 1
        real = dmg - self.df
        if real > 0:
            self.hp = self.hp - real
        else:
            real = 0
        return real

    def attack_target(self, target): # 데미지 처리 함수 2
        dmg = random.randint(1, self.atk)
        real = target.take_damage(dmg)
        return dmg, real


class Player(Character): # 플레이어 정보
    def __init__(self, name): #1레벨 초기화 함수
        super().__init__(name, 1, 100, 25, 5)
        self.exp = 0

    def gain_experience(self, exp): #경험치 올라가는 함수
        self.exp += exp

    def level_up(self): # 레벨업 처리 함수
        if self.exp >= 50:
            self.level += 1
            self.atk += 10
            self.df += 5
            self.exp -= 50
            print("레벨업! 레벨", self.level)


class Monster(Character): # 몬스터 정보
    def __init__(self, name, level): #몬스터 스펙 처리 함수
        hp = random.randint(10, 30) * level
        atk = random.randint(5, 20) * level
        df = random.randint(1, 5) * level
        super().__init__(name, level, hp, atk, df)


def battle(player, monster): # 배틀 함수
    print(f"\n{monster.name} (Lv.{monster.level}) 이(가) 나타났다!")
    while player.is_alive() and monster.is_alive():
        dmg, real = player.attack_target(monster)
        print(f"{player.name}의 공격! ({dmg} → 실제 {real}) → {monster.name} 체력: {monster.hp}")
        if monster.is_alive():
            dmg, real = monster.attack_target(player)
            print(f"{monster.name}의 반격! ({dmg} → 실제 {real}) → {player.name} 체력: {player.hp}")

    if player.is_alive(): # 전수 승리
        print("전투 승리!")
        player.gain_experience(monster.level * 20)
        player.level_up()
    else:
        print("전투 패배..") # 전투 패배


def main(): # 메인 함수
    monsters = {'슬라임': 1, '고블린': 2, '오크': 3} # 몬스터 선택 
    name = input("당신의 이름은? ") # 플레이어 이름
    player = Player(name)

    for mname, mlevel in monsters.items(): #전투 처리 
        mon = Monster(mname, mlevel)
        battle(player, mon)
        if not player.is_alive():
            print("게임오버")
            break
    if player.is_alive():
        print("모든 몬스터를 물리쳤습니다!")


main() # 프로그램 시작
