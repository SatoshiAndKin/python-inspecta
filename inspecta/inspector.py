
# =========================================
#       IMPORTS
# --------------------------------------

import rootpath

rootpath.append()

import re
import pprint

from os import environ as env
from pygments import highlight, lexers, formatters
from termcolor import colored as color


# =========================================
#       CONSTANTS
# --------------------------------------

DEFAULT_INSPECTOR_INDENT = 4
DEFAULT_INSPECTOR_DEPTH = None
DEFAULT_INSPECTOR_COLORS = True


# =========================================
#       FUNCTIONS
# --------------------------------------

def inspect(
    data,
    indent = None,
    depth = None,
    colors = False,
):
    if indent is None:
        indent = DEFAULT_INSPECTOR_INDENT

    depth = env.get('INSPECTOR_DEPTH', None)

    if depth is None:
        depth = DEFAULT_INSPECTOR_DEPTH

    if depth == False:
        depth = None

    if depth:
        depth = int(depth)

    colors = env.get('INSPECTOR_COLORS', None)
    colors = colors or env.get('COLORS', None)

    if colors is None:
        colors = DEFAULT_INSPECTOR_COLORS

    colors = re.search(r'^true|1$', str(colors), flags = re.IGNORECASE)

    result = None

    try:
        if isinstance(data, dict):
            data = dict(data)

        result = pprint.pformat(data,
            indent = indent,
            depth = depth,
        )

        if colors:
            lexer = lexers.PythonLexer()
            formatter = formatters.TerminalFormatter()

            result = highlight(result, lexer, formatter)

    except Exception as error:
        pass

    return result

_print = print

def print(*args, **kwargs):
    _print(inspect(*args, *kwargs))
