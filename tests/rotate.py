#! /usr/bin/env python3

import lo99ing
import logging
import time
import datetime
import os
import pathlib
from pprint import pprint


def main():

    logdir = os.path.splitext(__file__)[0] + '_output'
    pathlib.Path(logdir).mkdir(exist_ok=True)

    logger = lo99ing.get_logger('LOGGER1')

    lo99ing.enable_file(pathlib.Path(logdir) / 'a_*_b.log', rotate=True)

    pprint(datetime.datetime.utcnow())
    pprint(logging.root.handlers[-1].stream)
    while True:
        logger.info('x')
        pprint(datetime.datetime.utcnow())
        pprint(logging.root.handlers[-1].stream)
        time.sleep(1 * 60)


if __name__ == '__main__':
    main()
