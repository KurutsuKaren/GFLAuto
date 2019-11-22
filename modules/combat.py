from util.utils import Region, Utils
from util.logger import Logger

gen_regions = {
    'combat': Region(1400, 700, 0, 0),
    'com': Region(950, 550, 0, 0),
    'ok': Region(1800, 1000, 0, 0),
    'planning_mode': Region(100, 880, 0, 0)
}

regions = {
    'starting_point': Region(1200, 250, 0, 0),
    'start0': Region(1800, 950, 0, 0),
    'enemy': Region(700, 400, 0, 0)
}

class Combat(object):

    clears = 0

    @staticmethod
    def swipe_top_left():
        Utils.swipe(50, 200, 850, 1000, 1000)
        Utils.swipe(50, 200, 850, 1000, 1000)

    @staticmethod
    def singularity(map, count):
        Combat.clears = count
        Utils.touch_randomly(gen_regions["combat"])
        Utils.wait_till_find_touch("singularity_menu")
        Utils.wait_till_find("singularity_in")
        Logger.log_info("Inside Singularity")
        Combat.swipe_top_left()

        Logger.log_msg("Starting {} clears on {}".format(count, map))
        if map == 0:
            Combat.map0()

    @staticmethod
    def deploy(com, start=False):
        Utils.touch_randomly(com)
        Utils.wait_till_find("echelon_formation")
        Utils.touch_randomly(gen_regions["ok"])
        Logger.log_msg("Echelon deployed")
        if start:
            Utils.touch_randomly(gen_regions["ok"])
            Logger.log_msg("Comencing operation")
            Utils.script_sleep(2)

    @staticmethod
    def map0():
        Logger.log_info("{} clears left".format(Combat.clears))
        Utils.swipe(1600, 700, 700, 700, 1000)
        Utils.touch_randomly(regions["starting_point"])
        Utils.touch_randomly(regions["start0"])
        Utils.wait_till_find("select_operation")
        Logger.log_msg("Deploying echelon")
        Combat.deploy(gen_regions["com"], True)
        Utils.touch_randomly(gen_regions["com"])
        Utils.touch_randomly(gen_regions["planning_mode"])
        Utils.swipe(314, 150, 950, 1050, 1000)
        Utils.swipe(314, 150, 314, 500, 1000)
        Utils.touch_randomly(regions["enemy"])
        Utils.touch_randomly(gen_regions["ok"])
        Utils.script_sleep(5)
        Utils.wait_till_find("planning_mode")
        Logger.log_msg("Map finished")
        Combat.clears -= 1  
        Utils.touch_randomly(gen_regions["ok"])
        Utils.wait_till_find_touch("result_screen")
        Utils.script_sleep(2)
        Utils.touch_randomly(gen_regions["ok"])
        Utils.script_sleep(1)
        Utils.touch_randomly(gen_regions["ok"])
        Utils.script_sleep(1)
        Utils.touch_randomly(gen_regions["ok"])
        Utils.wait_till_find("singularity_in")
        Combat.swipe_top_left()
        if Combat.clears > 0: Combat.map0()
        else: Logger.log_success("Clears done!")