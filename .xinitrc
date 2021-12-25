#!/bin/bash

# merge Xresources
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources

# disable screensaver and blank screen
xset -dpms; xset s off

# Monitor
xrandr --output DVI-D-0 --primary
xrandr --output DVI-D-0 --mode 2560x1440 --rate 75

xrandr --output HDMI-0 --mode 2560x1440 --rate 75
xrandr --output HDMI-0 --right-of DVI-D-0

xrandr --output DP-1 --mode 1920x1080 --rate 60
xrandr --output DP-1 --left-of DVI-D-0

# Keyboard
setxkbmap -layout "us,ge"
setxkbmap -option "grp:caps_toggle"
# TODO ru-s rame calke mapperi
# https://faq.i3wm.org/question/2569/set-mod-key-only-as-left-mod-key.1.html
# 1. cpslck shd toggle between us,ge and alt+cpslck between us,ru
# 2. disable/remap win_r

# Activate num lock on boot
numlockx &

# Set mouse cursor and background colour
xsetroot -cursor_name left_ptr -solid '#CCCC00' &

# Wallpaper
~/bin/fehbg &

# Start compositioning
picom -b

# Start Desktop
#exec i3
exec qtile start
