#! /usr/bin/env python3

import logging


def pre_lo99ing():
    # this runs before importing lo99ing
    L = logging.getLogger('stranger11')
    assert L.level == logging.NOTSET, L.level
    L = logging.getLogger('stranger12')
    assert L.level == logging.NOTSET, L.level
    L = logging.getLogger('stranger21')
    L.setLevel(logging.ERROR)
    L = logging.getLogger('stranger22')
    L.setLevel(logging.ERROR)


def test_lo99ing():
    import lo99ing  # late import
    from lo99ing.logger import Lo99er
    from lo99ing.level import log_level_manager

    ########################################
    # TEST STRANGERS

    # not set, no explicit level -- leave as notset
    L = lo99ing.get_logger('stranger11')
    assert not isinstance(L, Lo99er), L
    assert L.level == logging.NOTSET, L.level
    assert log_level_manager.get_effective_level('stranger11') is None

    # not set, explicit level -- use it
    L = lo99ing.get_logger('stranger12', level='info')
    assert not isinstance(L, Lo99er), L
    assert L.level == logging.INFO, L.level
    assert log_level_manager.get_effective_level('stranger12') == logging.INFO

    # set, no explicit level -- set existing level as initial
    L = lo99ing.get_logger('stranger21')
    assert not isinstance(L, Lo99er), L
    assert L.level == logging.ERROR, L.level
    assert log_level_manager.get_effective_level('stranger21') == logging.ERROR

    # set, explicit level -- ignore explicit level, set existing level as initial
    L = lo99ing.get_logger('stranger22', level='info')
    assert not isinstance(L, Lo99er), L
    assert L.level == logging.ERROR, L.level
    assert log_level_manager.get_effective_level('stranger22') == logging.ERROR

    ########################################
    # TEST LO99ERS

    # no explicit level, set default level as initial
    L = lo99ing.get_logger('mine11')
    assert isinstance(L, Lo99er), L
    assert L.level == logging.INFO, L.level
    assert log_level_manager.get_effective_level('mine11') == logging.INFO
    assert log_level_manager.get_initial('mine11') == logging.INFO

    # with explicit level, set it as initial
    L = lo99ing.get_logger('mine12', level='error')
    assert isinstance(L, Lo99er), L
    assert L.level == logging.ERROR, L.level
    assert log_level_manager.get_effective_level('mine12') == logging.ERROR
    assert log_level_manager.get_initial('mine12') == logging.ERROR

    # no explicit level, but with pre-existing override
    lo99ing.set_log_level_override('mine21', 'debug')
    L = lo99ing.get_logger('mine21')
    assert isinstance(L, Lo99er), L
    assert L.level == logging.DEBUG, L.level
    assert log_level_manager.get_effective_level('mine21') == logging.DEBUG
    assert log_level_manager.get_initial('mine21') == logging.INFO

    # with explicit level, but with pre-existing override
    lo99ing.set_log_level_override('mine22', 'debug')
    L = lo99ing.get_logger('mine22', level='error')
    assert isinstance(L, Lo99er), L
    assert L.level == logging.DEBUG, L.level
    assert log_level_manager.get_effective_level('mine22') == logging.DEBUG
    assert log_level_manager.get_initial('mine22') == logging.ERROR


def main():
    pre_lo99ing()
    test_lo99ing()


if __name__ == '__main__':
    main()
