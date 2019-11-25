import sys
import argparse
from datetime import datetime, timedelta
from util.adb import Adb
from util.config import Config
from util.utils import Utils, Region
from modules.combat import Combat
from modules.factory import Factory
from util.logger import Logger

# check run-time args
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config',
                    metavar=('CONFIG_FILE'),
                    help='Use the specified configuration file instead ' +
                         'of the default config.ini')
parser.add_argument('-d', '--debug',
                    help='Enables debugging logs.', action='store_true')
parser.add_argument('-l', '--legacy',
                    help='Enables sed usage.', action='store_true')
parser.add_argument('-e', '--enhance', help='Auto-enhance', action='store_true')
args = parser.parse_args()

# check args, and if none provided, load default config
if args:
    if args.config:
        config = Config(args.config)
    else:
        config = Config('config.ini')
    if args.debug:
        Logger.log_info("Enabled debugging.")
        Logger.enable_debugging(Logger)
    if args.legacy:
        Logger.log_info("Enabled sed usage.")
        Adb.enable_legacy(Adb)

Adb.service = config.network['service']
Adb.device = '-d' if (Adb.service == 'PHONE') else '-e'
adb = Adb()
if adb.init():
    Logger.log_msg('Sucessfully connected to the service.')
else:
    Logger.log_error('Unable to connect to the service.')
    sys.exit()

if args.enhance:
    Factory.factory()
    Factory.enhance()
    sys.exit()

def CheckLogistic():
    Utils.script_sleep(3)

    if Utils.find("ls_completed"):
        Utils.touch_randomly()
        Logger.log_msg("Logistic Mission finished")
    if Utils.find_and_touch("ls_ok_restart"):
        Logger.log_msg("Restarting Logistic Mission")
        CheckLogistic()

def CombatManager():
    clears = config.times

    while clears > 0:
        Logger.log_msg("{} clears to finish.".format(clears))
        combat = Combat(config.operation)
        if combat.goToOperation() == 0: clears -= 1
        if config.logistic: CheckLogistic()
    Logger.log_success("Finished all clears. Closing program.")

if config.combat: CombatManager()

def LogisticManager():
    while True:
        Utils.update_screen()

        if Utils.find("ls_completed"):
            Utils.touch_randomly()
            Logger.log_msg("Logistic Mission finished")
        if Utils.find_and_touch("ls_ok_restart"):
            Logger.log_msg("Restarting Logistic Mission")
    
if config.logistic: LogisticManager()
    
