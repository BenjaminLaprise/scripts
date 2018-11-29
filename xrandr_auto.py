#!/usr/bin/env python3
import subprocess
import time

connect_command = "xrandr_auto"
disconnect_command = ""


def get(cmd): return subprocess.check_output(cmd).decode("utf-8")


def count_screens(monitors): return monitors.count(" connected ")


def run_command(cmd): subprocess.Popen(["/bin/bash", "-c", cmd])


def main():
    monitor_count = None
    while True:
        time.sleep(1)
        new_monitor_count = count_screens(get(["xrandr"]))
        if new_monitor_count != monitor_count:
            time.sleep(2)
            run_command("~/.screenlayout/default_%s.sh" % new_monitor_count)
            run_command("~/.wallpaper/wall_%s" % new_monitor_count)
            run_command("~/.config/polybar/launch.sh")
        monitor_count = new_monitor_count

if __name__ == '__main__':
    time.sleep(1)
    main()
