from util.utils import Utils, Region
from modules.factory import Factory
from util.logger import Logger

class Order(object):
    filename = ''
    orders = []
    result = 0

    def __init__(self, filename):
        self.filename = "maps/" + filename + ".gfl"
        f = open(self.filename, "rt")
        for l in f:
            self.orders.append(l.rstrip().split(' '))
        self.orders.reverse()
        self.result = self.executeOrders()

    def nextOrder(self):
        if self.orders.__len__() > 0:
            return self.orders.pop()
        else:
            return -1

    def executeOrders(self):
        while True:
            n = self.nextOrder()
            if n[0] == 'end': break
            if n[0] == 'swipe':
                Utils.swipe(int(n[1]), int(n[2]), int(n[3]), int(n[4]), 1000)
                continue
            if n[0] == 'tap':
                Utils.touch_randomly(Region(int(n[1]), int(n[2]), 0, 0))
                continue
            if n[0] == 'wait':
                Utils.script_sleep(int(n[1]))
                continue
            if n[0] == 'find_touch':
                if Utils.find_and_touch(n[1]):
                    if n[1] == 'dock_full':
                        Factory.enhance()
                        return 1
                continue
            if n[0] == 'wait_find':
                Utils.wait_till_find(n[1])
                continue
            if n[0] == 'wait_find_touch':
                Utils.wait_till_find_touch(n[1])
                continue
            if n[0] == 'swipe_topleft':
                Utils.swipe_top_left()
                continue
            if n[0] == 'log_info':
                Logger.log_info(n[1].replace('_', ' '))
                continue
            if n[0] == 'deploy':
                if n[1] == 'start': self.deploy()
                else: self.deploy(False)
                continue
            print(n)
        return 0

    def deploy(self, start=True):
        Utils.touch_randomly(Region(950, 550, 0, 0))
        Utils.wait_till_find("echelon_formation")
        Utils.touch_randomly(Region(1800, 1000, 0, 0))
        Logger.log_msg("Echelon deployed")
        if start:
            Utils.touch_randomly(Region(1800, 1000, 0, 0))
            Logger.log_msg("Comencing operation")
            Utils.script_sleep(2)