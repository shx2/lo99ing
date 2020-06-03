#! /usr/bin/env python3

import lo99ing
import os
import pathlib


def main():

    logdir = os.path.splitext(__file__)[0] + '_output'
    pathlib.Path(logdir).mkdir(exist_ok=True)

    logger = lo99ing.get_logger('xxx')
    flogger = lo99ing.get_file_logger('flogger', logdir + '/f.log')

    logger.info('1 this prints to stderr only')
    flogger.info('1 this prints to file only')
    logger.info('2 done')
    flogger.info('2 done')


if __name__ == '__main__':
    main()
