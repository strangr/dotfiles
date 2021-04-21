from QWidgets import QWidgets
from libqtile import widget

class QWidgetsList:

    widgets = QWidgets()

    def left_widgets_list(self, groups):
        widgets_list = [
            self.widgets.group_box(groups),
            self.widgets.current_layout_did(),
            self.widgets.current_screen(),
            self.widgets.spacer(),
            #widget.Chord

            self.widgets.kbd_layout(),
            self.widgets.separator(),
            self.widgets.memory(),
            self.widgets.separator(),
            self.widgets.disk(),
            self.widgets.separator(),
            self.widgets.volume(),
            self.widgets.separator(),
            self.widgets.datetime_poll(),
            #self.widgets.datetimePoll(),
            self.widgets.separator(),

            #widget.Sep(linewidth=0, foreground='#282425'),
            self.widgets.system_tray(),
        ]

        return widgets_list

    def right_widgets_list(self, groups):
        widgets_list = [
            self.widgets.group_box(groups),
            self.widgets.current_layout_did(),
            widget.WindowName(),
        ]

        return widgets_list
