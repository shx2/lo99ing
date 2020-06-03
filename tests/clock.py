#! /usr/bin/env python3

import lo99ing
import datetime


class ManualClock:

    def __init__(self, t=None):
        self.t = t

    def now(self):
        return self.t


def main():
    logger = lo99ing.get_logger('LOGGER1')

    logger.info('<-- 1 local time')

    lo99ing.use_utc()
    logger.info('<-- 2 utc time')

    manual_clock = ManualClock()
    lo99ing.use_clock(manual_clock.now)
    logger.info('<-- 3 still utc time')
    manual_clock.t = datetime.datetime(1990, 1, 1, 2, 2, 2, 888000)
    logger.info('<-- 4 made up time in 1990')
    manual_clock.t = datetime.datetime(2222, 3, 3, 4, 4, 4, 999000)
    logger.info('<-- 5 made up time in 2222')

    logger.info('done')


if __name__ == '__main__':
    main()
