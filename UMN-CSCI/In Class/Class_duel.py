
class Adventurer:
    def  __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = level
        self.strength = strength
        self.speed = speed
        self.power = power
        self.HP = self.level * 6
        self.hidden = False
    def __repr__(self):
        return str(self.name) + ' - HP: ' + str(self.HP)
    def attack(self,target):
        if target.hidden == True:
            print(str(self.name) + " can't see " + str(target.name))
        else:
            target.HP -= self.strength + 4
            print(str(self.name) + ' attacks ' + str(target.name) + ' for ' + str(self.strength + 4) + ' damage')
    def __lt__(self,other):
        if self.HP < other.HP:
            return True
        else:
            return False



class Fighter(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP *= 2

    def attack(self, target):
        if target.hidden == True:
            print(str(self.name) + " can't see " + str(target.name))
        else:
            target.HP -= 2 * self.strength + 6
            print(str(self.name) + ' attacks ' + str(target.name) + ' for ' + str(self.strength + 4) + ' damage')




class Thief(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True

    def attack(self, target):
        if self.hidden == True:
            if target.hidden == True:
                if self.speed > target.speed:
                    target.HP -= 5 * (self.speed + self.level)
                    print(str(self.name) + ' sneak attacks ' + str(target.name) + ' for ' + str(5 * (self.speed + self.level)) + ' damage')
                else:
                    print(str(self.name) + " can't see " + str(target.name))
            else:
                target.HP -= 5 * (self.speed + self.level)
                print(str(self.name) + ' sneak attacks ' + str(target.name))
            self.hidden = False
        else:
            Adventurer.attack(self, target)




class Wizard(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.fireballs_left = power
    def attack(self, target):
        if self.fireballs_left == 0:
            Adventurer.attack(self, target)
        else:
            target.hidden = False
            target.HP -= self.level * 3
            self.fireballs_left -= 1
            print(str(self.name) + ' casts fireball on ' + str(target.name) + ' for ' + str(self.level * 3) + ' damage')




def duel(adv1, adv2):
    while adv1.HP > 0 and adv2.HP > 0:
        print(adv1,adv2,sep='\n')
        adv1.attack(adv2)
        if adv2.HP > 0:
            adv2.attack(adv1)
            if adv1.HP < 1:
                print(adv1,adv2,str(adv2.name) + ' wins!', sep='\n')
                return False
        else:
            print(adv1,adv2,str(adv1.name) + ' wins!', sep='\n')
            return True
    if adv1.HP == 0 and adv2.HP == 0:
        print('Everyone loses!')
        return False





def tournament(adv_list):
    if len(adv_list) == 0:
        return None
    if len(adv_list) == 1:
        return adv_list[0]
    else:
        adv_list = sorted(adv_list)
        if duel(adv_list[-2],adv_list[-1]) == True:
            del(adv_list[-1])
        else:
            del(adv_list[-2])

    return tournament(adv_list)


