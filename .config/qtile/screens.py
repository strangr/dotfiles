from libqtile.config import Screen, Key
from libqtile.lazy import lazy
from libqtile import bar, widget

import os
from subprocess import check_output
from datetime import datetime

from groups import left_groups, right_groups
from keys import keys, mod

homeDir = os.path.expanduser('~')

bar_config = dict(
    background = '282425',
    margin = [0,0,0,0],
    opacity = 1
)

groupbox_defaults = dict(
    disable_drag=True,
    center_aligned=True,

    fontsize=18,

    padding=0,
    padding_x=2,
    padding_y=0,

    #margin=2,
    margin_x=2,
    margin_y=4,

    spacing=0,
    borderwidth=0,

    highlight_method='text',
    urgent_alert_method='text',
    rounded=False,

    urgent_text='FF0000',
    foreground='34ebeb',
    
    #1e9ea9
    #e1d1af
    #99b9ac
    #this_current_screen_border="F3825A", #focused group
    #this_current_screen_border="1e9ea9", #focused group
    this_current_screen_border="99b9ac", #focused group
    active="d8c9aa", #unfocused gorup
    inactive="766a5a" #empty group
)

sep_defaults = dict(
    linewidth=5,
    foreground='#282425'
)

def get_kbd_layout():
    out = check_output(['sh', '/home/st/.config/qtile/blocks/key_layout.sh']).decode("utf-8").replace('\n', '')

    return out

def update_kbd_layout():
    def f(qtile):
        qtile.widgets_map["textbox"].update(text=get_kbd_layout())

    return f

def get_time():
    now = datetime.now()
    out1 = now.strftime("%a").upper()
    out2 = "<span color='#766a5a'>" + out1 + "</span>"
    out3 = now.strftime("%d %H:%M")
    out4 = out2 + " " + out3

    return out4

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.TextBox(
                #     "DELOS",
                #     #background="#FFFFFF",
                #     foreground="#F3825A",
                # ),
                # vpn on/off
                #widget.Spacer(),
                #widget.WindowName(),
                #widget.Notify(),
                #widget.Spacer(),
                #widget.Wallpaper(),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#F3825A"),
                #widget.WidgetBox(widgets=[
                #    widget.TextBox(text="This widget is in the box"),
                #    widget.Memory()
                #    ]
                #),
                #widget.CheckUpdates(distro='Arch'),
                #widget.Chord(),

                widget.GroupBox(
                    visible_groups=left_groups,
                    **groupbox_defaults
                ),

                #widget.CurrentLayout(),
                #[homeDir + '/.config/qtile/icons']
                widget.CurrentLayout(
                    fontsize='22',
                    ),

                # widget.CurrentLayoutIcon(
                #     custom_icon_paths=[homeDir + '/.config/qtile/icons'],
                #     scale=0.5,
                #     padding=0,
                #     foreground="#0000FF"),

                widget.CurrentScreen(
                    padding=0,
                #    font='hack',
                    fontsize='22',
                    active_color='d8c9aa',
                    active_text='',
                    inactive_color='766a5a',
                    inactive_text=''
                ),

                # widget.TextBox(
                #     "",
                #     padding=2,
                #     font='hack',
                #     fontsize='22',
                #     foreground="#d8c9aa",
                # ),



                # widget.CapsNumLockIndicator(
                #     background="#484142"
                # ),

                #widget.Prompt(),


                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),

                widget.TextBox(text=get_kbd_layout()),
                widget.Sep(**sep_defaults),
                widget.Memory(format="<span color='#766a5a'>MEM</span> {MemPercent: .0f}% {SwapPercent: .0f}%"),
                widget.Sep(**sep_defaults),
                widget.DF(format="<span color='#766a5a'>ROOT</span> {f}{m}", visible_on_warn=False),
                widget.Sep(**sep_defaults),
                widget.Volume(fmt="<span color='#766a5a'>VOL</span> {}"),
                widget.Sep(**sep_defaults),
                #widget.Clock(format='%d %a %H:%M'),
                widget.TextBox(text=get_time()),
                widget.Sep(**sep_defaults),
                widget.Systray(),
                widget.Sep(linewidth=2, foreground='#282425'),
            ],
            26,
            **bar_config
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    visible_groups=right_groups,
                    **groupbox_defaults
                ),
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Systray(),
                #widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                #widget.QuickExit(),
            ],
            26,
            **bar_config
        ),
    ),
]

keys.extend([
    Key([], "ISO_Next_Group", lazy.function(update_kbd_layout())),
])
