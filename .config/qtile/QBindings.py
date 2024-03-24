from Helpers import Helpers

from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy

import os

class QKeys:

    home = os.path.expanduser('~')

    def init_keys(self, mod, terminal):
        return [
            
            # Window Controls
            Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
            Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
            
            # @TODO split into several sizes + sticky goes here
            #Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),
            Key([mod, "shift"], "f", self.toggle_floating(), desc="Toggle Floating"),

            # Qtile Controls
            Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
            Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
            Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

            # Switch between windows
            Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
            Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
            Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
            Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

            #Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
            # @TODO try lazy.function(
            Key([mod], "Left", self.move_focus_left()),
            #Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
            Key([mod], "Right", self.move_focus_right(), desc="Move focus to right"),
            Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
            Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),


            # + shift + -> - next group (cycle on screen)
            # + shift + <- = prev group

            # + -> - next item (if reached numOfGroupsPerScreen : next screen group)
            # + <= = prev item

            # period -> focus next
            # comma -> focus prev

            # @TODO new method to swith between floating and stacked

            # Move windowsV
            Key([mod, "shift"], "h", lazy.layout.swap_left()),
            Key([mod, "shift"], "l", lazy.layout.swap_right()),
            Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
            Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

            Key([mod, "shift"], "Left", self.move_window_left()),
            #Key([mod, "shift"], "Right", lazy.layout.swap_right()),
            Key([mod, "shift"], "Right", self.move_window_right()),
            Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
            Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),


            # Grow windows.
            Key([mod, "control"], "l", lazy.layout.grow()),
            Key([mod, "control"], "h", lazy.layout.shrink()),
            
            Key([mod, "control"], "period", lazy.layout.grow()),
            Key([mod, "control"], "comma", lazy.layout.shrink()),


            # Window Helpers
            Key([mod], "x", lazy.layout.normalize()),
            Key([mod], "o", lazy.layout.maximize()),
            Key([mod, "shift"], "space", lazy.layout.flip()),
            # @TODO (bug) this resets to default ration instead of one set by me
            Key([mod, "shift"], "x", lazy.layout.reset()),

            # System
            Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
            Key([], "ISO_Next_Group", lazy.function(Helpers.update_kbd_layout()), desc="Switch Language Layout"),

            # Utils
            # @TODO maybe make them into chords (<> vol, m -> <> mute vol/mic)
            Key([mod, "shift"], "period", lazy.spawn("changeVolume plus"), desc="Increase Sound"),
            Key([mod, "shift"], "comma", lazy.spawn("changeVolume minus"), desc="Decrease Sound"),
            Key([mod, "shift"], "m", lazy.spawn("changeVolume mute"), desc="Mute"),
            Key([mod, "shift"], "n", lazy.spawn("changeVolume 120"), desc="120"),
            Key([mod, "shift"], "b", lazy.spawn("changeVolume mutemic"), desc="Mute Mic"),

            # @TODO dunstctl
            Key(["control"], "Escape", lazy.spawn("dunstctl history-pop"), desc="Dunst show recent"),
            Key(["control"], "space", lazy.spawn("dunstctl close"), desc="Dunst close recent"),
            Key(["control", "shift"], "space", lazy.spawn("dunstctl close-all"), desc="Dunst close all recent"),
            Key([mod], "n", lazy.spawn("dunstPause"), desc="Pause Dunst"),
            # ctrl + shift + period
            #   dunstctl context

            # ROFI
            Key([mod], "p", lazy.spawn("rofi -show run"), desc="Applition Launcher"),
            Key([mod], "g", lazy.spawn("rofimoji --prompt=Type"), desc="Insert Emoji"),

            # Screenshots
            Key([], "Insert", lazy.spawn("scrot " + self.home + "/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png"), desc="Screenshot"),
            Key(["shift"], "Insert", lazy.spawn("scrot -s " + self.home + "/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png"), desc="Screenshot Rectangle"),

            # Redshift
            Key([mod], "z", lazy.spawn("redshift -x"), lazy.spawn("redshift -O 4000"), desc="Redshift 4000"),
            Key([mod, "shift"], "z", lazy.spawn("redshift -x"), desc="Redshift Reset"),

            # @TODO win+n new firefox window
        ]

    def move_focus_left(self):
        @lazy.function
        def f(qtile):
            # @TODO check what if null
            # @TODO when max layout dont have cmd_left()
            # @TODO if fullscreem should count as clients = 1
            if qtile.current_window == qtile.current_layout.clients[0]:
                #@TODO test method qtile.cmd_next_screen() (and prev)
                if qtile.current_screen.index == 0 :
                    qtile.to_screen(len(qtile.screens) - 1)
                else:
                    qtile.to_screen(qtile.current_screen.index - 1)

                if(len(qtile.current_group.windows) > 0):
                    nxt = qtile.current_group.windows[-1]
                    nxt.group.focus(nxt)

            else:
                qtile.current_layout.left()

        return f

    def move_focus_right(self):
        @lazy.function
        def f(qtile):
            # @TODO check what if current_window is null
            if len(qtile.current_layout.clients) > 1 and qtile.current_window == qtile.current_layout.clients[0]:
                qtile.current_layout.right()
            else:
                if len(qtile.screens) - 1 == qtile.current_screen.index :
                    qtile.to_screen(0)
                else:
                    qtile.to_screen(qtile.current_screen.index + 1)
 
                if(len(qtile.current_group.windows) > 0):
                    nxt = qtile.current_group.windows[0]
                    nxt.group.focus(nxt)
            
        return f

    def move_window_left(self):
        @lazy.function
        def f(qtile):
            # @TODO check what if null
            # @TODO when max layout dont have cmd_left()
            # @TODO if fullscreem should count as clients = 1
            # @TODO if new screen, always insert as last window in group
            if qtile.current_window == qtile.current_layout.clients[0]:
                if qtile.current_screen.index == 0 :
                    screen = qtile.screens[len(qtile.screens) - 1]
                    qtile.current_window.togroup(screen.group.name)
                    qtile.to_screen(len(qtile.screens) - 1)
                else:
                    # @TODO make this into func
                    screen = qtile.screens[qtile.current_screen.index - 1]
                    qtile.current_window.togroup(screen.group.name)
                    qtile.to_screen(qtile.current_screen.index - 1)

                #qtile.current_window.group.focus(qtile.current_window)
            else:
                qtile.current_layout.cmd_swap_left()

        return f

    def move_window_right(self):
        @lazy.function
        def f(qtile):
            # @TODO check what if current_window is null
            # @TODO if new screen, always insert as master pane in group
            if len(qtile.current_layout.clients) > 1 and qtile.current_window == qtile.current_layout.clients[0]:
                qtile.current_layout.cmd_swap_right()
            else:
                # current window sometimes null?
                if len(qtile.screens) - 1 == qtile.current_screen.index :
                    # qtile.to_screen(0)
                    screen = qtile.screens[0]
                    qtile.current_window.togroup(screen.group.name)
                    qtile.to_screen(0)
                else:
                    screen = qtile.screens[qtile.current_screen.index + 1]
                    qtile.current_window.togroup(screen.group.name)
                    qtile.to_screen(qtile.current_screen.index + 1)

                #qtile.current_window.group.focus(qtile.current_window)

                # if(len(qtile.current_group.windows) > 0):
                #     nxt = qtile.current_group.windows[0]
                #     nxt.group.focus(nxt)
            
        return f

    def toggle_floating(self):
        @lazy.function
        def f(qtile):

            float_width = 500
            float_height = 360
            float_gap = 15
            float_x = qtile.current_screen.width - float_width - float_gap
            float_y = qtile.current_screen.height - float_height - float_gap
            #@TODO gap right should be number_of_floating_windows_in_current_group * (gap+float_width)

            qtile.current_window._float_width = float_width
            qtile.current_window._float_height = float_height
            qtile.current_window.float_x = float_x
            qtile.current_window.float_y = float_y

            qtile.current_window.cmd_toggle_floating()
        return f

class QChords:
    def init_cords(self, mod):
        return [
            KeyChord([mod], "u", [
                Key([], "1", lazy.spawn("aka-update-screen 1")),
                Key([], "2", lazy.spawn("aka-update-screen 2")),
                Key([], "3", lazy.spawn("aka-update-screen 3"))
            ])
        ]

class QMouse:
    
    def init_mouse(self, mod):
        return [
            Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
            Click([mod], "Button2", lazy.window.bring_to_front())
        ]
