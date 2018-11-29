#!/usr/bin/env python
import sys
import time
import subprocess

from daemon import Daemon


def get(cmd): return subprocess.check_output(cmd).decode("utf-8")


def count_screens(monitors): return monitors.count(" connected ")


def run_command(cmd): subprocess.Popen(["/bin/bash", "-c", cmd])


class AutoXRandrDaemon(Daemon):
    def run(self):
        print('Auto XRandr Daemon started')
        monitor_count = None
        while True:
            time.sleep(1)
            new_monitor_count = count_screens(get(["xrandr"]))
            if new_monitor_count != monitor_count:
                print('Monitor count: %s' % new_monitor_count)
                run_command("~/.screenlayout/default_%s.sh" % new_monitor_count)
                run_command("~/.wallpaper/wall_%s" % new_monitor_count)
                run_command("~/.config/polybar/launch.sh")
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
