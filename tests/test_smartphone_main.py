import runpy
import sys

import pytest


def test_smartphone_main_raises_type_error():
    sys.modules.pop("src.smartphone", None)
    with pytest.raises(TypeError, match="невозможно сложить два объекта разных типов"):
        runpy.run_module("src.smartphone", run_name="__main__")
