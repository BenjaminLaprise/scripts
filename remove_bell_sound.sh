# Disable PC speaker (Beep sound)
sudo rmmod pcspkr
sudo echo "blacklist pcspkr" > /etc/modprobe.d/nobeep.conf
sudo echo "setterm -blength 0" > /etc/profile
sudo echo "set bell-style none" > /etc/inputrc
echo "xset -b" > ~/.xprofile

