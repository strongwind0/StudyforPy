import math
import random


# 电磁炮（玩家视角）
class RailGun:
    def __init__(self, name='', life_value=1000, attack_power=100):
        self.name = name
        self.life_value = life_value
        self.attack_power = attack_power
        self.max_life = life_value

    def attack(self, fighter):
        if isinstance(fighter, Fighter):
            fighter.life_value -= self.attack_power
            print("你攻击了{:>}，对其造成{:>}伤害,{:>}剩余生命值{:>}".
                  format(fighter.id, self.attack_power, fighter.id, fighter.life_value))

    def select_object(self, fighters):
        fighters_id = list()
        for fighter in fighters:
            fighter.parameter()
            fighters_id.append(fighter.id)
        select = ""
        while select not in fighters_id:
            select = input("请选择你的攻击对象:")
            if select not in fighters_id:
                print("对象不存在或已击落")
        for fighter in fighters:
            if fighter.id == select:
                self.attack(fighter=fighter)
                break
        if fighter.life_value <= 0:
            print("你已击落", fighter.id)
            fighters.remove(fighter)

    def level_up(self):
        while True:
            print("等级提升，请选择加点(1.生命,0.攻击):", end='')
            choose = input()
            if choose == '0':
                self.attack_power += 100
                self.life_value = self.max_life
                print("攻击力提升100，现在攻击力{:}".format(self.attack_power))
                break
            elif choose == '1':
                self.max_life += 200
                self.life_value = self.max_life
                print("生命值提升200，现在生命值", self.life_value)
                break


# 敌人（基类）
class Fighter:
    def __init__(self, fighter_id='', life_value=500, attack_power=20):
        self.id = fighter_id
        self.life_value = life_value
        self.attack_power = attack_power

    def attack(self, rail_gun):
        if isinstance(rail_gun, RailGun):
            rail_gun.life_value -= self.attack_power
            print("你被{:>}攻击了，对你造成伤害{:>}，剩余生命值{:>}".
                  format(self.id, self.attack_power, rail_gun.life_value))

    def parameter(self):
        print("{:>},攻击力{:>}，生命值{:>}".
              format(self.id, self.attack_power, self.life_value))


# 侦察机（攻击低，血量偏低）
class Reconnaissance(Fighter):
    def __init__(self, fighter_id='', life_value=200, attack_power=5):
        self.id = fighter_id
        self.life_value = life_value
        self.attack_power = attack_power

    def attack(self, rail_gun):
        if isinstance(rail_gun, RailGun):
            rail_gun.life_value -= self.attack_power
            print("你被侦察机{:>}攻击了，对你造成伤害{:>}，剩余生命值{:>}".
                  format(self.id, self.attack_power, rail_gun.life_value))

    def parameter(self):
        print("侦察机{:>},攻击力{:>}，生命值{:>}".
              format(self.id, self.attack_power, self.life_value))


# 歼击机(中等)
class FighterPlane(Fighter):
    def __init__(self, fighter_id='', life_value=300, attack_power=50):
        self.id = fighter_id
        self.life_value = life_value
        self.attack_power = attack_power

    def attack(self, rail_gun):
        if isinstance(rail_gun, RailGun):
            rail_gun.life_value -= self.attack_power
            print("你被歼击机{:>}攻击了，对你造成伤害{:>}，剩余生命值{:>}".
                  format(self.id, self.attack_power, rail_gun.life_value))

    def parameter(self):
        print("歼击机{:>},攻击力{:>}，生命值{:>}".
              format(self.id, self.attack_power, self.life_value))


# 轰炸机(高攻击，低生命)
class Bomber(Fighter):
    def __init__(self, fighter_id='', life_value=150, attack_power=100):
        self.id = fighter_id
        self.life_value = life_value
        self.attack_power = attack_power

    def attack(self, rail_gun):
        if isinstance(rail_gun, RailGun):
            rail_gun.life_value -= self.attack_power
            print("你被轰炸机{:>}攻击了，对你造成伤害{:>}，剩余生命值{:>}".
                  format(self.id, self.attack_power, rail_gun.life_value))

    def parameter(self):
        print("轰炸机{:>},攻击力{:>}，生命值{:>}".
              format(self.id, self.attack_power, self.life_value))


# 场景
class Scenes:
    difficulty = 0  # 难度

    def __init__(self):
        self.game_start()

    # 胜负判断
    def win_or_lose(self, fighters, rail_gun):
        if rail_gun.life_value <= 0:
            return -1  # 游戏结束
        elif not fighters:
            self.difficulty += 1
            return 1  # 难度提升
        else:
            return 0  # 游戏继续

    # 生成飞机群
    def number_of_aircraft(self):
        number = math.ceil(self.difficulty*math.log(self.difficulty+1))+1
        fighters = list()
        for i in range(number):
            generate = random.random()
            fighter_id = '00' + str(i)
            if generate > 0.4:
                fighters.append(FighterPlane(fighter_id=fighter_id[-3::],
                                             life_value=250+50*self.difficulty,
                                             attack_power=25))
            elif generate < 0.1:
                fighters.append(Bomber(fighter_id=fighter_id[-3::],
                                       life_value=150+50*self.difficulty,
                                       attack_power=75+5*self.difficulty))
            else:
                fighters.append(Reconnaissance(fighter_id=fighter_id[-3::],
                                               life_value=200+50*self.difficulty,
                                               attack_power=5))
        return fighters

    def game_start(self):
        rail_gun = RailGun(name=input("请为你的大炮起名:"))
        while True:
            print("{:}请做好准备，当前生命值{:}，攻击力{:}".format(rail_gun.name,
                                                    rail_gun.life_value,
                                                    rail_gun.attack_power))
            print("当前难度:", self.difficulty)
            fighters = self.number_of_aircraft()
            print("敌机来袭，开始战斗")
            judgment = 0  # 胜负判断
            while judgment != -1:
                rail_gun.select_object(fighters=fighters)
                for fighter in fighters:
                    fighter.attack(rail_gun=rail_gun)
                judgment = self.win_or_lose(fighters=fighters, rail_gun=rail_gun)
                if judgment == 1:
                    rail_gun.level_up()
                    break
            if judgment == -1:
                print("游戏结束")
                print("到达难度:{:}".format(self.difficulty))
                break


scenes = Scenes()
