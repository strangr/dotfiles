from libqtile.config import Screen, Key
from libqtile.lazy import lazy
from libqtile import bar, widget

from subprocess import check_output

from groups import left_groups, right_groups
from keys import keys, mod

bar_config = dict(
    background = '282425',
    margin = [0,0,0,0],
    opacity = 1
)

groupbox_defaults = dict(
    disable_drag=True,
    center_aligned=True,

    fontsize=14,
    padding_x=0,
    padding_y=0,
    margin_x=0,
    spacing=0,

    highlight_method='text',
    urgent_alert_method='text',

    urgent_text='FF0000',
    foreground='34ebeb',
    
    #1e9ea9
    #e1d1af
    #this_current_screen_border="F3825A", #focused group
    this_current_screen_border="1e9ea9", #focused group
    active="e1d1af", #unfocused gorup
    inactive="766a5a" #empty group
)

def get_kbd_layout():
    out = check_output(['sh', '/home/st/.config/qtile/blocks/key_layout.sh']).decode("utf-8").replace('\n', '')

    return out

def update_kbd_layout():
    def f(qtile):
        qtile.widgets_map["textbox"].update(text=get_kbd_layout())

    return f

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
                widget.CurrentLayout(),
                widget.CurrentLayoutIcon(),
                widget.CurrentScreen(),
                widget.CapsNumLockIndicator(),

                widget.Prompt(),


                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),


                widget.TextBox(text=get_kbd_layout()),
                widget.Sep(),
                widget.Memory(format="MEM {MemPercent: .0f}% {SwapPercent: .0f}%"),
                widget.Sep(),
                widget.DF(format='ROOT {f}{m}', visible_on_warn=False),
                widget.Sep(),
                widget.Volume(fmt="<span color='#ff0000'>VOL</span> {}"),
                widget.Sep(),
                widget.Clock(format='%d %a %H:%M'),
                widget.Sep(),
                widget.Systray(),
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
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            26,
            **bar_config
        ),
    ),
]

keys.extend([
    Key([], "ISO_Next_Group", lazy.function(update_kbd_layout())),
])