from Helpers import Helpers
from QTheme import Colors
# @TODO import each widget separatly instead of whole widget
from libqtile import widget

class QWidgets:

    colors = Colors()

    def separator(self):
        return widget.Sep(
            linewidth=5,
            foreground=self.colors.black
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

            urgent_text=self.colors.red,
            foreground=self.colors.yellow,
            this_current_screen_border=self.colors.green, #focused group
            active=self.colors.yellow, #unfocused gorup
            inactive=self.colors.grey #empty group
        )

    def current_layout(self):
        return widget.CurrentLayout(fontsize='22')

    def current_screen(self):
        return widget.CurrentScreen(
            padding=0,
            fontsize='22.3',
            active_color=self.colors.yellow,
            active_text='',
            inactive_color=self.colors.grey,
            inactive_text=''
        )

    # @TODO current window icon
    # subscribe.net_wm_icon_change(func)


    def window_name(self):
        return widget.WindowName()

    def kbd_layout(self):
        return widget.TextBox(text=Helpers.get_kbd_layout())

    def num_lock(self):
        return widget.GenPollText(
            func=lambda: Helpers.get_num_lock(),
            update_interval=0.5,
            fontsize='21.7',
            padding=3
        )

    def memory(self):
        return widget.Memory(
            measure_mem='G',
            format=Helpers.format_text("MEM") + " {MemFree: .0f}G")

    def disk(self):
        return widget.DF(format=Helpers.format_text("ROOT") + " {uf}{m}", visible_on_warn=False)

    def volume(self):
        return widget.Volume(fmt=Helpers.format_text("VOL") + " {}")
    
    def spacer(self):
        return widget.Spacer()

    def datetime_poll(self):
        return widget.GenPollText(
            func=lambda: Helpers.get_time(),
            update_interval=60
        )

    def vpn_status(self):
        return widget.GenPollText(
            func=lambda: Helpers.get_vpn_status(),
            update_interval=5
        )

    def system_tray(self):
        return widget.Systray()

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
