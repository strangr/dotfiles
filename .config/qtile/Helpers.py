from QTheme import Colors

import subprocess
from subprocess import check_output
from datetime import datetime

import os
import re

class Helpers:

    home = os.path.expanduser('~')

    @staticmethod
    def update_kbd_layout():
        def f(qtile):
            qtile.widgets_map["textbox"].update(text=Helpers.get_kbd_layout())

        return f

    @staticmethod
    def get_kbd_layout():
        out = check_output(['sh', 'getKeyLayout']).decode("utf-8").replace('\n', '')
        if out != "US":
          out = Helpers.format_text(out)

        return out

    @staticmethod
    def get_num_lock():
        try:
            output = subprocess.check_output(['xset', 'q']).decode("utf-8")
        except subprocess.CalledProcessError as err:
            output = err.output.decode()
        if output.startswith("Keyboard"):
            indicators = re.findall(r"Num\sLock:\s+(\w*)", output)

            if len(indicators) > 0 and indicators[0] == "on":
                return ""

        return ""

    @staticmethod
    def get_time():
        now = datetime.now()
        out1 = Helpers.format_text(now.strftime("%a").upper())
        out2 = now.strftime("%d %H:%M")
        out3 = out1 + " " + out2

        return out3

    @staticmethod
    def get_vpn_status():
        out = check_output(['sh', 'checkNetworkLink', 'tun0']).decode("utf-8").replace('\n', '')
        out2 = Helpers.format_text("VPN")

        if out == 'up':
            out = out2 + " UP"
        else:
            out = out2 + " DOWN"

        return out

    @staticmethod
    def format_text(text):
        out = "<span color='"+ Colors.grey +"'>"+ text +"</span>"

        return out

    @staticmethod
    def log_text(text):
        fh = open(home + "/.config/qtile/log.txt", "a")
        log = str(datetime.now()) + "|" + text + "\n"
        fh.write(log)
        fh.close()