from util.utils import Region, Utils
from util.logger import Logger

regions = {
    'factory': Region(1700, 530, 0, 0),
    'ok': Region(1800, 930  , 0, 0),
    'enhance': Region(150, 500, 0, 0),
    'return': Region(50, 50, 0, 0)
}

class Factory(object):

    @staticmethod
    def factory():
        Utils.touch_randomly(regions["factory"])
        Utils.wait_till_find("factory")

    @staticmethod
    def enhance():
        Utils.wait_till_find("factory")
        Utils.touch_randomly(regions["enhance"])
        Utils.wait_till_find_touch("select_character")
        Utils.script_sleep(1)
        gun = None
        gun = Utils.find("enhance_1_l")
        if not gun: gun = Utils.find("enhance_1")
        if not gun: gun = Utils.find("enhance_2_l")
        if not gun: gun = Utils.find("enhance_2")
        if not gun: gun = Region(150, 400, 0, 0)
        Utils.touch_randomly(gun)
        Utils.wait_till_find_touch("select_character_2")
        Utils.wait_till_find_touch("smart_select")
        Utils.script_sleep(2)
        if not Utils.find("smart_select"):
            Utils.touch_randomly(regions["ok"])
            Utils.script_sleep(1)
            Utils.touch_randomly(regions["ok"])
            Utils.script_sleep(1)
            Utils.touch_randomly(regions["ok"])
            Utils.script_sleep(1)
            Factory.enhance()
        else:
            Utils.touch_randomly(regions["return"])
            Utils.touch_randomly(regions["return"])
            Utils.wait_till_find("test")
