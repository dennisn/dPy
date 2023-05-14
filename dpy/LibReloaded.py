"""
.. module:: LibReloaded
   :synopsis: Snippets on how to setup reloading of a library in developemnt
   
Module: LibReloaded

Snippets on how to setup reloading of a library, especially in development
"""
import importlib
import sys
from pathlib import Path

# make sure the root of the developing library is in the path
module_path=r"C:\Dev\Github\dPy"
if module_path not in sys.path:
    sys.path.append(module_path)

# normal import
from dpy import LogHelper

#### If want to reload the module after changed
importlib.reload(LogHelper)
