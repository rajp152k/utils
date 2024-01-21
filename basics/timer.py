from pprint import pprint
import subprocess
from pathlib import Path
import argparse
import time
import asyncio

aper = argparse.ArgumentParser("Basic Alarm")
NOTIF = Path("/usr/share/sounds/sound-icons/canary-long.wav")

aper.add_argument("-H", "--hours", type=int,
                  default=0, help="time in hours")
aper.add_argument("-M", "--minutes", type=int,
                  default=0, help="time in minutes")
aper.add_argument("-S", "--seconds", type=int,
                  default=0, help="time in seconds")
aper.add_argument("-R", "--ring", type=str,
                  default=NOTIF, help="path to notification sound")


RED_BACKGROUND = '\033[41m'
RESET_FORMATTING = '\033[0m'
DELETE_LINE = '\x1b[2K'


def notify_text(message: str | None = None):
    message = "notification triggered" if message is None else message
    print(RED_BACKGROUND)
    pprint(message)


def notify_alarm(interval: int = 1, ring=NOTIF):
    try:
        print("Hit C-c to stop alarm")
        while True:
            print("RINGING", end="\r")
            subprocess.run(['/usr/bin/aplay', '-q', str(ring)])
            time.sleep(interval)
            print(DELETE_LINE)
    except KeyboardInterrupt:
        print(RESET_FORMATTING)
        print("alarm stopped")


async def sleep(time):
    await asyncio.sleep(time)


def args_handler(args: argparse.Namespace, wait_seconds: int = 0):
    if not Path(args.ring).exists():
        print("notification sound not found")
        # print help message of args
        aper.print_help()
        exit(1)

    if wait_seconds <= 0:
        print("time must be positive")
        # print help message of args
        aper.print_help()
        exit(1)


if __name__ == '__main__':
    args = aper.parse_args()
    wait_seconds = args.hours * 3600 + args.minutes * 60 + args.seconds
    args_handler(args, wait_seconds)
    print(f"alarm init  {args.hours} H, {args.minutes} M,  {args.seconds} S")
    asyncio.run(sleep(wait_seconds))
    notify_text()
    notify_alarm()
