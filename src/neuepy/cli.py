"""Handle terminal graphics and IO."""

import sys
import tty
import termios

import blessings

class Term(object):
    __data = None

    def __init__(self):
        if self.__data == None:
            self.__data = self.__dict__
            self._term = blessings.Terminal()
        else:
            self.__dict__ = self.__data

    def print(self, *args, **kwargs):
        """Print something to the terminal."""
        print(*args, **kwargs)

    # Thanks:
    # <http://code.activestate.com/recipes/577977-get-single-keypress/>
    def getch(self):
        """Get a single keypress from stdin."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def __getattr__(self, name):
        try:
            return self._term.__getattribute__(name)
        except AttributeError:
            try:
                return self._term.__getattr__(name)
            except:
                raise
