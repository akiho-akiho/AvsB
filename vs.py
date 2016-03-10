import random
__metacclass__ = type

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_health_point(self):
        self.health_point = random.randint(100,9999)

    def get_magic_point(self):
        pass

    def my_message(self):
        # print "Hello, I'm %s." % self.name
        # print "my HP is %s" % self.health_point
        print self.name + "'s HP is " + str(self.health_point) + "."



if __name__ == "__main__":
    p1 = raw_input("Player1:")
    p2 = raw_input("Player2:")
    player_1 = Person()
    player_2 = Person()
    player_1.set_name(p1)
    player_2.set_name(p2)
    player_1.get_health_point()
    player_2.get_health_point()
    #player_1.my_message()
    #player_2.my_message()
    while player_1.health_point > 0 and player_2.health_point > 0:
        attack = random.randint(0, 599)
        print player_1.name + ' causes ' + str(attack) + ' point damage to ' + player_2.name
        player_2.health_point = player_2.health_point - attack
        if (player_2.health_point < 0):
            break
        attack = random.randint(0, 599)
        print player_2.name + ' causes ' + str(attack) + ' point damage to ' + player_1.name
        player_1.health_point = player_2.health_point - attack
    if player_1.health_point < 0:
        print player_2.name + ' wins!! The ramaining blood is ' + str(player_2.health_point)
    if player_2.health_point < 0:
        print player_1.name + ' wins!! The ramaining blood is ' + str(player_1.health_point)

