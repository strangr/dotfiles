from QBindings import QKeys, QMouse
from QScreen import QScreen
from QGroups import QGroups
from QScratchPad import QScratchPad
from QTheme import QDefaults
from QRules import QRules

from typing import List  # noqa: F401

from libqtile.layout import Floating
from libqtile import hook

import os
import subprocess

#僧
#类﩯舘麗
#ﰧﳶ
#﵁恵頻侀𤋮全充

# @TODO groups w,e will have gaps
# @TODO try catch
if __name__ in ["config", "__main__"]:

    mod = "mod4"
    terminal = "urxvt"
    
    #TODO make them into dicts with basic configs
    # ex: name,
    #     label,
    #       layout_style=spacer
    #       layout_match=chat

    left_groups = ["1","2","3","4","grave"]
    right_groups = ["q","w","e","r","t"]

    keys = []
    screens = []
    groups = []
    mouse = []

    qScreen = QScreen(left_groups, right_groups)
    qGroups = QGroups(left_groups, right_groups)
    qScratchPad = QScratchPad()
    qKeys = QKeys()
    qMouse = QMouse()
    qRules = QRules()

    screens += qScreen.init_dual_screen_bar()
    
    groups += qGroups.init_left_groups()
    groups += qGroups.init_right_groups()
    groups += qScratchPad.init_scratchpads(terminal)

    keys += qKeys.init_keys(mod, terminal)
    keys += qGroups.init_keys(mod)
    keys += qScratchPad.init_keys(mod)

    mouse += qMouse.init_mouse(mod)

    widget_defaults = QDefaults.widget_defaults
    extension_defaults = QDefaults.extension_defaults
    floating_layout = Floating(
        float_rules=qRules.init_floating_rules(),
        **QDefaults.floating_layout
    )

    auto_fullscreen     = True
    cursor_warp         = False
    follow_mouse_focus  = False
    reconfigure_screens = False
    auto_minimize       = False
    bring_front_click   = "floating_only"
    wmname              = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

def main(qtile):
    
    #●雷綠祿
    def update_group_labels():
        for group in qtile.groups:
            number_of_windows = len(group.windows)
            current_groups = [screen.group.name for screen in qtile.screens if screen.group]
            if number_of_windows > 0 or group.name in current_groups:
                group.cmd_set_label("")
            else:
                group.cmd_set_label("")

    @hook.subscribe.setgroup
    def group_change():
        update_group_labels()

    @hook.subscribe.client_managed
    def func(window):
        update_group_labels()
