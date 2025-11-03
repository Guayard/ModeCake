bl_info = {
    "name": "ModeCake",
    "author": "Your Name",
    "version": (1, 2),
    "blender": (4, 0, 0),
    "description": "Pie menu for quick mode and selection switching",
    "category": "3D View",
}

import importlib
import bpy

# Import local modules
from . import preferences, keymap, menus, operators

# Reload during development (useful when reloading addons)
importlib.reload(preferences)
importlib.reload(keymap)
importlib.reload(menus)
importlib.reload(operators)

# Registration
def register():
    preferences.register()
    menus.register()
    operators.register()
    keymap.register()

def unregister():
    keymap.unregister()
    operators.unregister()
    menus.unregister()
    preferences.unregister()
