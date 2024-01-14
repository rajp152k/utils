#!/home/rp152k/miniforge3/bin/python

from pprint import pprint
import subprocess
from pathlib import Path
import argparse
import time
import asyncio

aper = argparse.ArgumentParser("Basic Alarm")

aper.add_argument("-H", "--hours", type=int,
                  default=0, help="time in hours")
aper.add_argument("-M", "--minutes", type=int,
                  default=0, help="time in minutes")
aper.add_argument("-S", "--seconds", type=int,
                  default=0, help="time in seconds")

NOTIF = Path("/usr/share/sounds/sound-icons/canary-long.wav")
RED_BACKGROUND = '\033[41m'
RESET_FORMATTING = '\033[0m'


def notify_text(message: str | None = None):
    message = "notification triggered" if message is None else message
    print(RED_BACKGROUND)
    pprint(message)
    print(RESET_FORMATTING)


def notify_alarm(interval: int = 1):
    try:
        print("Hit C-c to stop alarm")
        while True:
            subprocess.run(['/usr/bin/aplay','-q', str(NOTIF)])
            time.sleep(interval)
    except KeyboardInterrupt:
        print("alarm stopped")


async def sleep(time):
    await asyncio.sleep(time)

if __name__ == '__main__':
    args = aper.parse_args()
    wait_seconds = args.hours * 3600 + args.minutes * 60 + args.seconds

    print(f"alarm init  {args.hours} H, {args.minutes} M,  {args.seconds} S")
    asyncio.run(sleep(wait_seconds))
    notify_text()
    notify_alarm()
