"""
Definition of logger handlers, and tools for manipulating logger handlers.
"""

import logging
import logging.handlers
import sys
import traceback

from .formatter import formatter


################################################################################

class _ErrorHandlerMixin:
    """
    A mixin to improve error handling.
    The improved error handler prints the location (file, line num) of the logging call
    which failed.
    """

    def handleError(self, record):
        if not logging.raiseExceptions:
            return

        output_stream = getattr(self, 'stream')
        if not output_stream:
            output_stream = sys.stderr
        try:
            ei = sys.exc_info()
            traceback.print_exception(ei[0], ei[1], ei[2], None, output_stream)
            output_stream.write('Logged from %s:%s\n' % (record.pathname, record.lineno))
            # NOTE: if output stream is self.stream, the output might be buffered, but we avoid
            # flushing for threadsafety
        except (AttributeError, IOError):
            pass


class StreamHandler(_ErrorHandlerMixin, logging.StreamHandler):
    """
    Same as ``logging.StreamHandler``, but with an improved error-handler.
    """
    pass


class FileHandler(_ErrorHandlerMixin, logging.FileHandler):
    """
    Same as ``logging.FileHandler``, but with an improved error-handler.
    """
    pass


################################################################################
# globals

stderr_handler = StreamHandler(sys.stderr)
stderr_handler.setFormatter(formatter)


################################################################################
# add/remove handlers

def enable_stderr(logger=None):
    """ Adds a stderr StreamHandler to root logger (if not already there). """
    if logger is None:
        logger = logging.root

    # Don't add if it already has one
    if any(_is_stderr_handler(h) for h in logger.handlers):
            return

    logger.addHandler(stderr_handler)


def disable_stderr(logger=None):
    """ Removes the stderr StreamHandler from root logger (if there). """
    if logger is None:
        logger = logging.root

    for h in list(logger.handlers):
        if _is_stderr_handler(h):
            logger.removeHandler(h)


def _is_stderr_handler(handler):
    return isinstance(handler, logging.StreamHandler) and handler.stream == sys.stderr


def enable_file(filename, logger=None, file_handler=None, **kwargs):
    """ Adds a FileHandler to root logger, to enable logging to ``filename``. """
    if file_handler is None:
        file_handler = FileHandler(filename=filename, **kwargs)
    return _add_logging_handler(file_handler, logger=logger)


def _add_logging_handler(handler, logger=None):
    if logger is None:
        logger = logging.root
    if handler.formatter is None:
        handler.setFormatter(formatter)
    logger.addHandler(handler)


################################################################################
