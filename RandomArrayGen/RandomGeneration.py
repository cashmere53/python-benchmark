# -*- corging: utf-8 -*-

import os
import re
import sys
import random
import numpy as np
from benchmarker import Benchmarker, Reporter, CommandOptionError, _get_cpu_model, _usage, _parse_filter

__version__ = '$Release: 4.0.1 $'.split()[1]

python2 = sys.version_info[0] == 2
python3 = sys.version_info[0] == 3

if python3:
    xrange = range

def _main(benchmarker, argv=None):
    if argv is None:
        argv = sys.argv
    try:
        script, short_opts, long_opts, args = _parse_cmdopts(argv)
    except CommandOptionError as ex:
        sys.stderr.write(str(ex))
        sys.stderr.write("\n")
        sys.exit(1)
    if 'h' in short_opts:
        sys.stdout.write(_usage(script, benchmarker))
        sys.exit(0)
    if 'v' in short_opts:
        sys.stdout.write(__version__)
        sys.stdout.write("\n")
        sys.exit(0)
    if 'n' in short_opts:
        benchmarker.loop = int(short_opts['n'])
    if 'c' in short_opts:
        benchmarker.cycle = int(short_opts['c'])
    if 'x' in short_opts:
        benchmarker.extra = int(short_opts['x'])
    if 's' in short_opts:
        benchmarker.size = int(short_opts['s'])
    if 'o' in short_opts:
        benchmarker.outfile = short_opts['o']
    if 'f' in short_opts:
        benchmarker.filter = short_opts['f']
    benchmarker.properties = long_opts

def _parse_cmdopts(argv=None):
    if argv is None:
        argv = sys.argv
    argv = argv[:]
    short_opts = {}
    long_opts = {}
    script = os.path.basename(argv[0])
    args = sys.argv[1:]
    while args and args[0].startswith("-"):
        arg = args.pop(0)
        if arg == "--":
            break
        if arg.startswith("--"):
            m = re.match(r'^(\w[-\w]*)(?:=(.*))?', arg[2:])
            if not m:
                raise CommandOptionError("%s: invalid option." % arg)
            key, val = m.groups()
            if val is None:
                val = True
            long_opts[key] = val
        else:
            for i in xrange(1, len(arg)):
                ch = arg[i]
                if ch in "hv":
                    short_opts[ch] = True
                elif ch in "ncxsof":
                    optarg = arg[i+1:]
                    if not optarg:
                        if not args:
                            raise CommandOptionError("-%s: argument required." % ch)
                        optarg = args.pop(0)
                    if ch in "ncxs" and not optarg.isdigit():
                        raise CommandOptionError("-%s %s: integer expected." % (ch, optarg))
                    if ch == "f" and not _parse_filter(optarg):
                        raise CommandOptionError("-%s %s: invalid argument." % (ch, optarg))
                    short_opts[ch] = optarg
                    break
                else:
                    raise CommandOptionError("-%s: unknown option." % ch)
    #
    return script, short_opts, long_opts, args

class BenchmarkerPlus(Benchmarker):
    def __init__(self, size=10, loop=1, width=35, cycle=1, extra=0, filter=None,
                 outfile=None, argv=None, reporter=None):
        self.size = size
        self.reporter = reporter or ReporterPlus(width)
        super(BenchmarkerPlus, self).__init__(loop, width, cycle, extra, filter, outfile, argv, self.reporter)

    def __enter__(self):
        argv = self.argv
        if argv is None or argv is True:
            argv = sys.argv
        if argv is not False:
            _main(self, argv)
        return self

class ReporterPlus(Reporter):
    def __init__(self, width):
        super(ReporterPlus, self).__init__(width)

    def report_environment(self, benchmarker):
        b = benchmarker
        import platform
        items = [
            ("benchmarker"      , "release %s (for python)" % __version__),
            ("python version"   , platform.python_version()),
            ("python compiler"  , platform.python_compiler()),
            ("python platform"  , platform.platform()),
            # ("python executable", sys.executable),
            ("cpu model"        , _get_cpu_model() or "-"),
            ("parameters"       , dict(loop=b.loop, size=b.size, cycle=b.cycle, extra=b.extra)),
        ]
        self.json_data["Environment"] = dict(items)
        #
        buf = []; add = buf.append
        for k, v in items:
            if k == "parameters":
                v = "loop=%s, size=%s, cycle=%s, extra=%s" % (v['loop'], v['size'], v['cycle'], v['extra'])
            add("## %-20s %s\n" % (k+":", v))
        add("\n")
        return "".join(buf)


with BenchmarkerPlus(100, 10000, cycle=3, extra=1) as bench:
    @bench('for: random.uniform')
    def _(bm):
        array = []
        append = array.append
        ran = random.uniform
        for i in bm:
            child = []
            c_append = child.append
            for j in range(bench.size):
                c_append(ran(-0.1, 0.1))
            append(child)
        np.array(array)

    @bench('numpy.random.uniform')
    def _(bm):
        array = []
        append = array.append
        ran = np.random.uniform
        for i in bm:
            rarray = ran(-0.1, 0.1, bench.size)
            append(rarray)
