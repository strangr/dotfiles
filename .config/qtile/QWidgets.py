from Helpers import Helpers

from libqtile import widget

sep_defaults = dict(
    linewidth=5,
    foreground='#282425'
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

class QWidgets:

    def separator(self):
        return widget.Sep(**sep_defaults)
    
    def group_box(self, groups):
        return widget.GroupBox(visible_groups=groups, **groupbox_defaults)

    def current_layout_did(self):
        return widget.CurrentLayout(fontsize='22')

    def current_screen(self):
        return widget.CurrentScreen(
            padding=0,
            #font='hack',
            fontsize='22',
            active_color='d8c9aa',
            active_text='',
            inactive_color='766a5a',
            inactive_text='')

    def kbd_layout(self):
        return widget.TextBox(text=Helpers.get_kbd_layout())

    def memory(self):
        return widget.Memory(format=Helpers.format_text("MEM") + " {MemPercent: .0f}% {SwapPercent: .0f}%")

    def disk(self):
        return widget.DF(format=Helpers.format_text("ROOT") + " {f}{m}", visible_on_warn=False)

    def volume(self):
        return widget.Volume(fmt=Helpers.format_text("VOL") + " {}")
    
    def datetime_poll(self):
        return widget.TextBox(text=Helpers.get_time())

    def spacer(self):
        return widget.Spacer()

    def datetimePoll(self):
        return widget.GenPollText(
            func=Helpers.get_time(),
            update_interval=20,
            foreground="#000000")

    def system_tray(self):
        return widget.Systray()

# vpn on/off
#widget.Spacer(),
#widget.WindowName(),
#widget.Notify(),
#widget.Wallpaper(),
#widget.CheckUpdates(distro='Arch'),
#widget.Chord(),
#widget.Prompt(),
# widget.CapsNumLockIndicator(
#     background="#484142"
# ),
# widget.Chord(
#     chords_colors={
#         'launch': ("#ff0000", "#ffffff"),
#     },
#     name_transform=lambda name: name.upper(),
# ),
# widget.GroupBox(
#     visible_groups=right_groups,
#     **groupbox_defaults
# ),
# widget.CurrentLayout(),
# widget.Prompt(),

# widget.Chord(
#     chords_colors={
#         'launch': ("#ff0000", "#ffffff"),
#     },
#     name_transform=lambda name: name.upper(),
# ),
#widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#widget.Systray(),
#widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
#widget.QuickExit(),
