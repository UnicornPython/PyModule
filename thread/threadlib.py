#!/bin/env python

import threading


def playmusic():
    print("play music")


def schedule_task():
    timer = threading.Timer(3, playmusic)
    timer.start()


def main():
    schedule_task()


if __name__ == "__main__":
    main()
