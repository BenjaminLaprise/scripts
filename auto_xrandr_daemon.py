#!/usr/bin/env python3
import sys
import time
import subprocess

from daemon import Daemon


def get(cmd): return subprocess.check_output(cmd).decode("utf-8")


def count_screens(monitors): return monitors.count(" connected ")


def run_command(cmd): subprocess.Popen(["/bin/bash", "-c", cmd])

def get_vertical_monitors():
    output = subprocess.run(["bash", "-c", "~/scripts/get_vertical_monitors.sh"], capture_output=True)
    output = output.stdout.decode('utf-8')
    return output.strip().split()

def set_wallpapers(monitor_count):
    vertical_monitors = get_vertical_monitors()
    for monitor in range(monitor_count):
        if str(monitor) in vertical_monitors:
            run_command("~/scripts/random_vertical_wp.sh %s" % monitor)
        else:
            run_command("~/scripts/random_wp.sh %s" % monitor)

class AutoXRandrDaemon(Daemon):
    def run(self):
        print('Auto XRandr Daemon started')
        monitor_count = None
        while True:
            time.sleep(1)
            new_monitor_count = count_screens(get(["xrandr"]))
            if new_monitor_count != monitor_count:
                print('Monitor count: %s' % new_monitor_count)
                run_command("~/.screenlayout/.set_screen_layout_dir.sh" % new_monitor_count)
                run_command("~/.screenlayout/current.sh" % new_monitor_count)
                set_wallpapers(new_monitor_count)
            monitor_count = new_monitor_count

if __name__ == "__main__":
    daemon = AutoXRandrDaemon('/tmp/auto-xrandr-daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
            run_command('killall polybar')
        elif 'run' == sys.argv[1]:
            daemon.restart()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
