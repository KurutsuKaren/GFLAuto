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
        gun = Utils.find("enhance_1_l")
        if not gun: gun = Utils.find("enhance_1")
        if not gun: gun = Region(150, 400, 0, 0)
        Utils.touch_randomly(gun)
        Utils.wait_till_find_touch("select_character_2")
        Utils.script_sleep(1)

        main = Utils.update_screen()
        main = Utils.crop(main, 1634, 522, 278, 218)
        
        Utils.touch_randomly(regions["ok"])
        Utils.script_sleep(2)

        Utils.update_screen()
        if not Utils.find(main, 0.95, True):
            Utils.touch_randomly(regions["ok"])
            Utils.script_sleep(0)
            Utils.touch_randomly(regions["ok"])
            Utils.script_sleep(0)
            Utils.touch_randomly(regions["ok"])
            Utils.script_sleep(1)
            Factory.enhance()
        else:
            Utils.touch_randomly(regions["return"])
            Utils.touch_randomly(regions["return"])
            Utils.wait_till_find("test")
