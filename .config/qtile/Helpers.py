from QTheme import Colors

from subprocess import check_output
from datetime import datetime

import os

class Helpers:

    @staticmethod
    def update_kbd_layout():
        def f(qtile):
            qtile.widgets_map["textbox"].update(text=Helpers.get_kbd_layout())

        return f

    @staticmethod
    def get_kbd_layout():
        home = os.path.expanduser('~')
        out = check_output(['sh', 'getKeyLayout']).decode("utf-8").replace('\n', '')
        if out != "US":
          out = Helpers.format_text(out)

        return out

    @staticmethod
    def get_time():
        now = datetime.now()
        out1 = Helpers.format_text(now.strftime("%a").upper())
        out2 = now.strftime("%d %H:%M")
        out3 = out1 + " " + out2

        return out3

    @staticmethod
    def get_vpn_status():
        home = os.path.expanduser('~')
        out = check_output(['sh', 'checkNetworkLink', 'tun0']).decode("utf-8").replace('\n', '')
        out2 = Helpers.format_text("VPN")

        if out == 'up':
            out = out2 + " UP"
        else:
            out = out2 + " DOWN"

        return out

    @staticmethod
    def format_text(text):
        out = "<span color='"+ Colors.grey[0] +"'>"+ text +"</span>"

        return out
