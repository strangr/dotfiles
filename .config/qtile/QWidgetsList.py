from QWidgets import QWidgets

class QWidgetsList:

    widgets = QWidgets()

    def left_widgets_list(self, groups):
        widgets_list = [
            self.widgets.group_box(groups),
            self.widgets.current_layout(),
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
            self.widgets.separator(),
            self.widgets.system_tray(),
        ]

        return widgets_list

    def right_widgets_list(self, groups):
        widgets_list = [
            self.widgets.group_box(groups),
            self.widgets.current_layout(),
            self.widgets.window_name(),
        ]

        return widgets_list
