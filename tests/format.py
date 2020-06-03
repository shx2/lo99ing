#! /usr/bin/env python3

import lo99ing
import os
import pathlib


def main():

    logdir = os.path.splitext(__file__)[0] + '_output'
    pathlib.Path(logdir).mkdir(exist_ok=True)

    logger = lo99ing.get_logger('LOGGER1')

    try:
        dict()[6]
    except Exception as e:
        logger.error('1 this prints exception type and value=6 (no traceback):   %s', e)

    try:
        dict()[6]
    except Exception:
        logger.exception('2 this prints traceback')

    try:
        dict()[6]
    except Exception as e:
        e.ATTR1 = 'VALUE1'
        e.ATTR2 = 'VALUE2'
        logger.exception('3 this prints traceback and exc attributes')

    logger.info('4 next message fails formatting, and should cause a "Logged from" line')
    logger.info('does not print %s %s %s %s', 0, 1, 2)

    logger.info('5 done')


if __name__ == '__main__':
    main()
