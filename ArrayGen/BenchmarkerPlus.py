# -*- coding: utf-8 -*-

import sys
from benchmarker import Benchmarker, Reporter, _get_cpu_model

__version__ = '$Release: 4.0.1 $'.split()[1]

class BenchmarkerPlus(Benchmarker):
    def __init__(self, loop=1, width=35, cycle=1, extra=0, filter=None,
                 outfile=None, argv=None, reporter=None):
        self.reporter = reporter or ReporterPlus(width)
        super(BenchmarkerPlus, self).__init__(loop, width, cycle, extra, filter, outfile, argv, self.reporter)

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
            ("parameters"       , dict(loop=b.loop, cycle=b.cycle, extra=b.extra)),
        ]
        self.json_data["Environment"] = dict(items)
        #
        buf = []; add = buf.append
        for k, v in items:
            if k == "parameters":
                v = "loop=%s, cycle=%s, extra=%s" % (v['loop'], v['cycle'], v['extra'])
            add("## %-20s %s\n" % (k+":", v))
        add("\n")
        return "".join(buf)

