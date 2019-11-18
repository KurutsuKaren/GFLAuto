import sys
import argparse
from datetime import datetime, timedelta
from util.adb import Adb
from util.config import Config
from util.utils import Utils
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