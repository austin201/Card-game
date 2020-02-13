import random
class Player(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.isAlive = True

    def shoot(self, target):
        miss = random.randint(0,1)
        if miss == 1:
            print("miss")
        else:
            target.takedmg()

    def takedmg(self):
        dmg_zone = random.randint(0,2)
        if dmg_zone == 0:
            print("Hit a limb")
            self.health -= 10
        elif dmg_zone == 0:
            print("Body Shot")
            self.health -= 50
        else:
            print("Head Shot")
            self.health -= 100
        if self.health <= 0:
            self.die()

    def die(self):
        print("You have died")
        self.isAlive = False
    def __str__(self):
        rep = self.name+" has "+str(self.health)+" health left."
        return rep

class Alien(Player):
    def __init__(self):
        super(Alien, self).__init__("Alien")
    def die(self):
        print("The alien gasps and says, 'oh, this is it. This is the big on. \n"\
              "Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them... \,"\
              "Good-bye, cruel universe.'")
        self.isAlive = False

def main():
    us = Player("Austin")
    alien = Alien()
    us.shoot(alien)
    print(alien)
main()