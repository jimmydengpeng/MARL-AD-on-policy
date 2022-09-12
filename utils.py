from enum import Enum
from typing import Optional

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

def colorize(string: str, color: Color = Color.GRAY, bold=False, highlight=False) -> str:
    attr = []
    # num = color2num[color]
    num = color.value[0]
    if highlight: num += 10
    attr.append(str(num))
    if bold: attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

class WarnLevel(Enum):
    NORMAL = Color.CYAN
    WARNING = Color.YELLOW
    ERROR = Color.RED

def debug(msg: str, level: WarnLevel = WarnLevel.NORMAL, color : Optional[Color] = None, bold=True):
    if color == None:
        print(colorize(">>>", bold=True), colorize(msg, color=level.value, bold=bold))
    else:
        print(colorize(">>>", bold=True), colorize(msg, color=color, bold=bold))

if __name__ == "__main__":
    debug("hello")
    debug("hello", WarnLevel.WARNING)
    debug("hello", WarnLevel.ERROR)
    debug("world", color=Color.BLUE)


