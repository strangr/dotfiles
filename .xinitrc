#!/bin/bash

# merge Xresources
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources

# disable screensaver and blank screen
xset -dpms; xset s off

# Monitor
xrandr --output DVI-I-1 --primary
xrandr --output DVI-I-1 --mode 1920x1080 --rate 60
xrandr --output VGA-0 --right-of DVI-I-1

# Keyboard
#setxkbmap -option caps:escape
#setxkbmap -option "grp:alt_shift_toggle"
setxkbmap -layout "us,ge,ru"
setxkbmap -option "grp:caps_toggle"
# https://faq.i3wm.org/question/2569/set-mod-key-only-as-left-mod-key.1.html
# 1. cpslck shd toggle between us,ge and alt+cpslck between us,ru
# 2. disable/remap win_r

# Activate num lock on boot
numlockx &

# Set mouse cursor and background colour
xsetroot -cursor_name left_ptr -solid '#CCCC00' &

# Wallpaper
~/bin/fehbg &

# System Tray
stalonetray -c ~/.config/stalonetrayrc &

# Start Desktop
#exec i3
exec xmonad
