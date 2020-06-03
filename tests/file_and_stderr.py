#! /usr/bin/env python3

import lo99ing
import os
import pathlib


def main():

    logdir = os.path.splitext(__file__)[0] + '_output'
    pathlib.Path(logdir).mkdir(exist_ok=True)

    logger = lo99ing.get_logger('LOGGER1')

    logger.info('1 this prints to stderr')
    logger.error('2 this prints to stderr')
    logger.debug('NOPRINT')

    logger.set_log_level_override('error')
    logger.info('NOPRINT')
    logger.error('3 this prints to stderr')

    lo99ing.enable_file(os.path.join(logdir, 'a.log'))
    logger.info('NOPRINT')

    logger.set_log_level_override(None)
    logger.info('4 this prints to stderr and file (first line in file)')
    logger.error('5 this prints to stderr and file, next message in stderr is 7')

    lo99ing.disable_stderr()
    logger.info('6 this prints to file')

    lo99ing.enable_stderr()
    logger.info('7 this prints to stderr and file')

    # test trace
    logger.info('8 next line is a trace, with filename and linenum')
    logger.TRACE()
    logger.info('9 next line is a trace, with filename and linenum, and extra args')
    logger.TRACE(os, foo='bar')

    # test prefixed
    logger2 = logger.prefixed('AAA')
    logger2.info('10 this line includes AAA prefix')
    logger3 = logger2.prefixed('BBB')
    logger3.info('11 this line includes AAA BBB prefix')

    logger.info('12 done')


if __name__ == '__main__':
    main()
