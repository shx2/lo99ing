
0.1.0
-----
* Initial release.
* log level defaults to WARNING for installed modules and INFO for the rest
* `logger.exception()`` automatically extracts and prints exception attributes
* when logging an exception object, automatically adds exception type
* if logging messages fails formatting, also logs the location of the problematic call
* daily log rotation
* ``get_logger``
* ``enable_file``, ``get_file_logger``
* ``enable_stderr``, ``disable_stderr``
* ``use_utc``, ``use_clock``
* log-level overrides
* ``prefixed``
* ``logger.TRACE``
