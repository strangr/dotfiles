from Helpers import Helpers
from QTheme import Colors
from libqtile import widget

class QWidgets:

    colors = Colors()

    def separator(self):
        return widget.Sep(
            linewidth=5,
            foreground=self.colors.black[0]
        )
    
    def group_box(self, groups):
        return widget.GroupBox(
            visible_groups=groups,
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

            urgent_text=self.colors.red[0],
            foreground=self.colors.yellow[0],
            this_current_screen_border=self.colors.green[0], #focused group
            active=self.colors.yellow[0], #unfocused gorup
            inactive=self.colors.grey[0] #empty group
        )

    def current_layout_did(self):
        return widget.CurrentLayout(fontsize='22')

    def current_screen(self):
        return widget.CurrentScreen(
            padding=0,
            fontsize='22',
            active_color=self.colors.yellow[0],
            active_text='',
            inactive_color=self.colors.grey[0],
            inactive_text=''
        )

    def window_name(self):
        return widget.WindowName()

    def kbd_layout(self):
        return widget.TextBox(text=Helpers.get_kbd_layout())

    def memory(self):
        return widget.Memory(format=Helpers.format_text("MEM") + " {MemPercent: .0f}% {SwapPercent: .0f}%")

    def disk(self):
        return widget.DF(format=Helpers.format_text("ROOT") + " {f}{m}", visible_on_warn=False)

    def volume(self):
        return widget.Volume(fmt=Helpers.format_text("VOL") + " {}")
    
    def spacer(self):
        return widget.Spacer()

    def datetime_poll(self):
        return widget.GenPollText(
            func=lambda: Helpers.get_time(),
            update_interval=60
        )

    def system_tray(self):
        return widget.Systray()

# vpn on/off
# widget.Notify(),
# widget.Wallpaper(),
# widget.CheckUpdates(distro='Arch'),
# widget.Prompt(),
# widget.CapsNumLockIndicator(
#     background="#484142"
# ),
# widget.Chord(
#     chords_colors={
#         'launch': ("#ff0000", "#ffffff"),
#     },
#     name_transform=lambda name: name.upper(),
# ),