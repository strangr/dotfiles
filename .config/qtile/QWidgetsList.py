from QWidgets import QWidgets
from libqtile import widget

left_groups = ["1","2","3","4","grave"]
right_groups = ["q","w","e","r","t"]

class QWidgetsList:

	widgets = QWidgets()

	def left_widgets_list(self):
	    widgets_list = [
	        self.widgets.left_group_box(left_groups),
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
#	        self.widgets.datetimePoll(),
	        self.widgets.separator(),

	        widget.Sep(linewidth=2, foreground='#282425'),
	        self.widgets.system_tray(),
	    ]
	    return widgets_list

	def right_widgets_list(self):
	    widgets_list = [
	        self.widgets.right_group_box(right_groups),
	        self.widgets.current_layout_did(),
	        widget.WindowName(),
	    ]
	    return widgets_list
