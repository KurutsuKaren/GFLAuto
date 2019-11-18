# GFLAuto
At the moment it just completes and start Logistic Support missions. Scripts from `util` folder and `GFLAuto.py` (modified version of `ALAuto.py`) are copies from [ALAuto](https://github.com/Egoistically/ALAuto).  

**This bot was made for EN server, other servers won't work with current assets.**

## Requirements on Windows
* Python 3.X installed and added to PATH.
* Latest [ADB](https://developer.android.com/studio/releases/platform-tools) added to PATH.
* ADB debugging enabled emulator with **1920x1080 resolution** and **Android 5 or newer**.

Tested and used on Windows 10 with Nox 6.3.0.2, Android 5.1 @ 60fps. If it does not work with your emulator please use Nox.

## Installation and Usage
1. Clone or download this repository.
2. Install the required packages via `pip3` with the command `pip3 install -r requirements.txt`.
3. Enable adb debugging on your emulator, on Nox you might also need to enable root; or phone.
4. Change config.ini's IP:PORT to 127.0.0.1 and your emulator's adb port, then change the rest to your likings. If you are using your own phone/device for the bot, enable debbuging on your device and change IP:PORT to PHONE.
5. Run `GFLAuto` using the command `python GFLAuto.py`.