from util.utils import Region, Utils
from util.logger import Logger
from modules.factory import Factory
from util.order import Order

gen_regions = {
    'combat': Region(1400, 700, 0, 0),
    'com': Region(950, 550, 0, 0),
    'ok': Region(1800, 1000, 0, 0),
    'planning_mode': Region(100, 880, 0, 0),
    'return': Region(50, 50, 0, 0)
}

regions = {
    'starting_point': Region(1200, 250, 0, 0),
    'start0': Region(1800, 950, 0, 0),
    'enemy': Region(700, 400, 0, 0)
}

class Combat(object):
    operation = []

    def __init__(self, operation):
        Logger.log_info("Starting combat on {} chapter {} operation {}.".format(operation[0], operation[1], operation[2]))
        self.operation = operation

    def goToOperation(self):
        Logger.log_info("Going to {}.".format(self.operation[0]))
        Order(self.operation[0])
        combat = Order(self.operation[0] + self.operation[1] + self.operation[2])
        return combat.result