#!/bin/bash

# merge Xresources
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources

# @TODO test if works
#disable screensaver and blank screen
xset -dpms; xset s off

# Monitor
#xrandr --output HDMI-1 --primary
#xrandr --output HDMI-1 --mode 1920x1080 --rate 60
#xrandr --output VGA-1 --right-of HDMI-1

# Keyboard
setxkbmap -option caps:none
setxkbmap -layout "us,ru,ge"
setxkbmap -option "grp:alt_shift_toggle"

# Activate num lock on boot
numlockx &

# Background (@TODO not really a config, sadme xo ar gavitano)
#feh --bg-fil '~/bg.png'
~/.config/fehbg &

# Start Desktop
exec i3
