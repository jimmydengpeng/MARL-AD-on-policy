from asyncio import FastChildWatcher
from enum import Enum
from gc import collect
from operator import le
from typing import Any, Callable, Optional

class Color(Enum):
    GRAY       = 30,
    RED        = 31,
    GREEN      = 32,
    YELLOW     = 33,
    BLUE       = 34,
    MAGENTA    = 35,
    CYAN       = 36,
    WHITE      = 37,
    CRIMSON    = 38

color2num = dict(
    gray=30,
    red=31,
    green=32,
    yellow=33,
    blue=34,
    magenta=35,
    cyan=36,
    white=37,
    crimson=38
)

def colorize(string: str, color: Color = Color.WHITE, bold=False, highlight=False) -> str:
    attr = []
    # num = color2num[color]
    num = color.value[0]
    if highlight: num += 10
    attr.append(str(num))
    if bold: attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

class LogLevel(Enum):
    DEBUG = Color.MAGENTA
    INFO = Color.GREEN
    WARNING = Color.YELLOW
    ERROR = Color.RED

def debug_msg(
        msg: str,
        level: LogLevel = LogLevel.DEBUG,
        color : Optional[Color] = None,
        bold=True,
        inline=False
    ):
    def colored_prompt(prompt: str) -> str:
        return colorize("[")+colorize(prompt, color=level.value, bold=True)+colorize("]")

    prompt = colored_prompt("DEBUG")
    if level == LogLevel.INFO:
        prompt = colored_prompt("INFO")
    if level == LogLevel.WARNING:
        prompt = colored_prompt("WARNING")
    if level == LogLevel.ERROR:
        prompt = colored_prompt("ERROR")

    end = " " if inline else "\n"
    if color == None:
        # print(colorize(prompt, bold=True), colorize(msg, color=level.value, bold=bold))
        print(prompt, colorize(msg, color=Color.GRAY, bold=bold), end=end)
    else:
        print(colorize(">>>", bold=True), colorize(msg, color=color, bold=bold), end=end)


def debug_print(msg: str, level: LogLevel = LogLevel.DEBUG, args=Any, inline=False):
    debug_msg(msg, level, inline=inline)
    print(args)


if __name__ == "__main__":
    debug_msg("DEBUG", LogLevel.DEBUG)
    debug_msg("INFO", LogLevel.INFO)
    debug_msg("WARNING", LogLevel.WARNING)
    debug_msg("ERROR", LogLevel.ERROR)

    debug_msg("BLUE", color=Color.BLUE)
    debug_msg("CYAN", color=Color.CYAN)
    debug_msg("GREEN", color=Color.GREEN)
    debug_msg("MAGENTA", color=Color.MAGENTA)


    debug_print("hello", args="world")

    print("plain")
    print("plain")