# Qtile config
# for rangr

from QBindings import QKeys, QChords, QMouse
from QScreen import QScreen
from QGroups import QGroups
from QGroup import QGroup, LayoutType, MatchType
from QScratchPad import QScratchPad
from QTheme import QDefaults
from QRules import QRules
from Helpers import Helpers

from libqtile.layout import Floating
from libqtile import hook, qtile

from Xlib import display as xdisplay
from typing import List  # noqa: F401

import os
import subprocess
import logging

logging.basicConfig(filename='/home/st/qtile.log',
                    format='%(levelname)s %(asctime)s :: %(message)s',
                    level=logging.DEBUG)

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred and monitor.crtc > 0:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

# @TODO try catch
if __name__ in ["config", "__main__"]:

    mod = "mod4"
    terminal = "urxvt"

    num_monitors = get_num_monitors()

    # @TODO next
    left_monitor_index = 0
    right_monitor_index = 1 # if numofmons is >= 2 then 1 else 0
    extra_monitor_index = 2 # if numofmons is >= 3 then 2 else 0
    
    extra_groups = [
        QGroup("1"),
        QGroup("2"),
        QGroup("3"),
        QGroup("4"),
        QGroup("grave")
    ]

    left_groups = [
        QGroup("q"),
        QGroup("w"),
        QGroup("e"),
        QGroup("r"),
        QGroup("t")
    ]

    right_groups = [
        QGroup("a"),
        QGroup("s", layout=LayoutType.SPACER, match=MatchType.CHAT),
        QGroup("d", layout=LayoutType.SPACER, match=MatchType.WORKCHAT),
#        QGroup("ISO_Next_Group")
    ]

    keys = []
    screens = []
    groups = []
    mouse = []

    qScreen = QScreen()
    qGroups = QGroups()
    qScratchPad = QScratchPad()
    qKeys = QKeys()
    qChords = QChords()
    qMouse = QMouse()
    qRules = QRules()

    #qtile.cmd_screens()

    if num_monitors == 3 :
        screens += qScreen.init_triple_screen_bar(left_groups, right_groups, extra_groups)
    elif num_monitors == 2 :
        screens += qScreen.init_dual_screen_bar(left_groups + extra_groups, right_groups)
        extra_monitor_index = 0
    else:
        screens += qScreen.init_single_screen_bar(left_groups + right_groups + extra_groups)
        right_monitor_index = 0
        extra_monitor_index = 0

    groups += qGroups.init_group(right_groups + left_groups + extra_groups)
    groups += qScratchPad.init_scratchpads(terminal)

    keys += qKeys.init_keys(mod, terminal)
    keys += qChords.init_cords(mod)

    keys += qGroups.init_keys(mod, left_groups, left_monitor_index)
    keys += qGroups.init_keys(mod, right_groups, right_monitor_index)
    keys += qGroups.init_keys(mod, extra_groups, extra_monitor_index)

    keys += qScratchPad.init_keys(mod)
    keys += qScreen.init_keys(mod)

    mouse += qMouse.init_mouse(mod)

    widget_defaults = QDefaults.widget_defaults
    extension_defaults = QDefaults.extension_defaults
    floating_layout = Floating(
        float_rules=qRules.init_floating_rules(),
        **QDefaults.floating_layout
    )

    auto_fullscreen     = True
    cursor_warp         = True
    follow_mouse_focus  = False 
    reconfigure_screens = True
    auto_minimize       = False
    bring_front_click   = "floating_only"
    wmname              = "LG3D"

#subscribe.client_urgent_hint_changed(func)
#this should help me with teams

def update_sticky_group():
    pass
    # Helpers.log_text("update_sticky_group")
    # windows = qtile.windows_map.values()
    # for window in windows:
    #     if 'sticky' not in window.cmd_hints():
    #         continue

    #     screen_id = window.hints["sticky"]
    #     if qtile.current_screen.index != screen_id:
    #         continue

    #     cw = qtile.groups.index(qtile.current_group)
    #     window.togroup(qtile.groups[cw].name)

def update_sticky_focus():
    pass
    # Helpers.log_text("update_sticky_focus")
    # windows = qtile.windows_map.values()
    # for window in windows:
    #     if 'sticky' not in window.cmd_hints():
    #         continue

    #     screen_id = window.hints["sticky"]
    #     if qtile.current_screen.index != screen_id:
    #         continue

    #     window.cmd_bring_to_front()

def update_group_labels():
    #●雷綠祿
    #Helpers.log_text("update_group_labels")

    for group in qtile.groups:
        number_of_windows = len(group.windows)
        current_groups = [screen.group.name for screen in qtile.screens if screen.group]
        label = ""
        if number_of_windows > 0 or group.name in current_groups:
            label = ""

        if group.label != label:
            group.set_label(label)

# dont like bash for init
# make startuponce my own method
@hook.subscribe.startup_once
def startup_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

@hook.subscribe.startup
def startup():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/everystart.sh'])

@hook.subscribe.setgroup
def setgroup():
    #Helpers.log_text("subscribe.setgroup")
    update_sticky_group()
    update_group_labels()

# @todo group_window_add - maybe this hook is better
@hook.subscribe.client_managed
def client_managed(window):
    #Helpers.log_text("subscribe.setgroup")
    update_group_labels()

@hook.subscribe.focus_change
def focus_change():

    update_sticky_focus()

@hook.subscribe.screens_reconfigured
def screens_reconfigured():
    logging.debug("Screens Reconfigured")
    qtile.cmd_reload_config();