import os
from subprocess import check_output
from datetime import datetime

homeDir = os.path.expanduser('~')

class Helpers:

    @staticmethod
    def update_kbd_layout():
        def f(qtile):
            qtile.widgets_map["textbox"].update(text=Helpers.get_kbd_layout())

        return f

    @staticmethod
    def get_kbd_layout():
        out = check_output(['sh', homeDir + '/.config/qtile/blocks/key_layout.sh']).decode("utf-8").replace('\n', '')

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
    def format_text(text):
        out = "<span color='#766a5a'>"+ text +"</span>"

        return out
