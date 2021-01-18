#!/bin/bash

# merge Xresources
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources

# disable screensaver and blank screen
xset -dpms; xset s off

# Monitor
#xrandr --output HDMI-1 --primary
#xrandr --output HDMI-1 --mode 1920x1080 --rate 60
#xrandr --output VGA-1 --right-of HDMI-1

# Keyboard
#setxkbmap -option caps:escape
#setxkbmap -option "grp:alt_shift_toggle"
setxkbmap -layout "us,ge,ru"
setxkbmap -option "grp:caps_toggle"

# Activate num lock on boot
numlockx &

# Background
~/bin/fehbg &

# Start Desktop
exec i3
