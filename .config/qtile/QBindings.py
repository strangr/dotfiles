from Helpers import Helpers

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

import os

class QKeys:

    home = os.path.expanduser('~')

    def init_keys(self, mod, terminal):
        return [

            # Window Controls
            Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
            Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
            Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle Floating"),

            # Qtile Controls
            Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
            Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
            Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

            # Switch between windows
            Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
            Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
            Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
            Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

            # @TODO new method to swith between floating and stacked
            # @TODO write new next method, when reached the end of the screen, move to next
            #Key([mod], 'Tab', lazy.layout.next()),

            # Move windows
            Key([mod, "shift"], "h", lazy.layout.swap_left()),
            Key([mod, "shift"], "l", lazy.layout.swap_right()),
            Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
            Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

            # Grow windows.
            Key([mod, "control"], "l", lazy.layout.grow()),
            Key([mod, "control"], "h", lazy.layout.shrink()),
            Key([mod], "x", lazy.layout.normalize()),
            # @TODO (bug) this resets to default ration instead of one set by me
            Key([mod, "shift"], "x", lazy.layout.reset()),

            Key([mod], "o", lazy.layout.maximize()),
            Key([mod, "shift"], "space", lazy.layout.flip()),

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

            # ROFI
            Key([mod], "p", lazy.spawn("rofi -show run"), desc="Application Launcher"),
            Key([mod], "g", lazy.spawn("rofimoji --prompt=Type"), desc="Insert Emoji"),

            # Screenshots
            Key([], "Print", lazy.spawn("scrot " + self.home + "/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png"), desc="Screenshot"),
            Key(["shift"], "Print", lazy.spawn("scrot -s " + self.home + "/Pictures/screens/'%Y-%m-%d-%H-%M-%s'.png"), desc="Screenshot Rectangle"),

            # Redshift
            Key([mod], "z", lazy.spawn("redshift -x"), lazy.spawn("redshift -O 4000"), desc="Redshift 4000"),
            Key([mod, "shift"], "z", lazy.spawn("redshift -x"), desc="Redshift Reset"),

            # TODO win+n new firefox window
        ]

class QMouse:
    
    def init_mouse(self, mod):
        return [
            Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
            Click([mod], "Button2", lazy.window.bring_to_front())
        ]
