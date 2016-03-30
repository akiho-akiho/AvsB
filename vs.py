# -*- coding: utf-8 -*-
import random
import time
import threading
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

class timer(threading.Thread):
# 多线程测试
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print 'Thread Object (%d), Time: %s \n' % (self.thread_num, time.ctime())

    def stop(self):
        self.thread_stop = True

flag = 1
lock = threading.Lock()
# 控制两个进程同时结束
class chatic_fight(threading.Thread ):
    def __init__(self, fighter, accepter):
        self.fighter = fighter
        self.accepter = accepter
        threading.Thread.__init__(self)
        # self.thread_player = player
        self.thread_stop = False

    def run(self):
        global flag
        while(self.accepter.health_point > 0 and flag == 1):
            time.sleep(1)
            attack = random.randint(0, 599)
            self.accepter.health_point = self.accepter.health_point - attack
            print self.fighter.name +' causes ' + str(attack) + ' point damage to' + self.accepter.name + '. The remain hp is about ' + str(self.accepter.health_point)
        if lock.acquire():
            if(flag == 1):
                print '='*10 + self.fighter.name + ' wins!'
                flag = 0
            else:
                print 'QAQ!~'
            lock.release()
            self.thread_stop()

    def stop(self):
        self.thread_stop = True


def fight(player_1,player_2):
# 你打我一下，我打你一下的最基本攻击模式
    while(player_1.health_point > 0 and player_2.health_point > 0):
        attack = random.randint(0, 599)
        print player_1.name + ' causes ' + str(attack) + ' point damage to ' + player_2.name
        player_2.health_point = player_2.health_point - attack
        if (player_2.health_point < 0):
            break
        attack = random.randint(0, 599)
        print player_2.name + ' causes ' + str(attack) + ' point damage to ' + player_1.name
        player_1.health_point = player_2.health_point - attack
    if player_1.health_point < 0:
        return player_2
    if player_2.health_point < 0:
        return player_1

def test():
    thread1 = timer(1)
    thread2 = timer(2)
    thread1.start()
    thread2.start()
    time.sleep(10)
    thread1.stop()
    thread3.stop()

def chatic_fight_test():
    p1 = raw_input("Player1:")
    p2 = raw_input("Player2:")
    player_1 = Person()
    player_2 = Person()
    player_1.set_name(p1)
    player_2.set_name(p2)
    player_1.get_health_point()
    player_2.get_health_point()
    thread1 = chatic_fight(player_1, player_2)
    thread2 = chatic_fight(player_2, player_1)
    thread1.start()
    thread2.start()

def simple_fight():
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
    winner = fight(player_1, player_2)
    print winner.name + ' wins!! The ramaining blood is ' + str(winner.health_point)


if __name__ == "__main__":
    chatic_fight_test()

