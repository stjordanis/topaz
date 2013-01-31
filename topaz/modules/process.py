from __future__ import absolute_import

import os
import sys

from topaz.module import Module, ModuleDef


if sys.platform.startswith("win"):
    def geteuid():
        return 0 # MRI behaviour on windows
else:
    def geteuid():
        return os.geteuid()


class Process(Module):
    moduledef = ModuleDef("Process", filepath=__file__)

    @moduledef.function("euid")
    def method_euid(self, space):
        return space.newint(geteuid())

    @moduledef.function("pid")
    def method_pid(self, space):
        return space.newint(os.getpid())

    @moduledef.function("exit", status="int")
    def method_exit(self, space, status=0):
        raise space.error(space.w_SystemExit, "exit", [space.newint(status)])
