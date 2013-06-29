import sys
import spack
from spack.color import cprint

indent = "  "

def msg(message, *args):
    cprint("@*b{==>} @*w{%s}" % str(message))
    for arg in args:
        print indent + str(arg)


def info(message, *args, **kwargs):
    format = kwargs.get('format', '*b')
    cprint("@%s{==>} %s" % (format, str(message)))
    for arg in args:
        print indent + str(arg)


def verbose(message, *args):
    if spack.verbose:
        info(message, *args, format='*g')


def debug(*args):
    if spack.debug:
        info(message, *args, format='*c')


def error(message, *args):
    info(message, *args, format='*r')


def warn(message, *args):
    info(message, *args, format='*Y')


def die(message, *args):
    error(message, *args)
    sys.exit(1)


def pkg(message):
    """Outputs a message with a package icon."""
    import platform
    from version import Version

    mac_ver = platform.mac_ver()[0]
    if mac_ver and Version(mac_ver) >= Version('10.7'):
        print u"\U0001F4E6" + indent,
    else:
        cprint('@*g{[+]} ')
    print message
