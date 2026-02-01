import runpy
import sys


def test_lawngrass_main_runs():
    sys.modules.pop("src.lawngrass", None)
    runpy.run_module("src.lawngrass", run_name="__main__")
