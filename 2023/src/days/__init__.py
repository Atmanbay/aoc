import os
import importlib

__globals = globals()

for file in os.listdir(os.path.dirname(__file__)):
    mod_name = file[:-3]   # strip .py at the end
    if mod_name != "__pycach" and mod_name != "__init__":
        __globals[mod_name] = importlib.import_module('.' + mod_name, package=__name__)