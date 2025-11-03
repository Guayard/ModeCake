import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty

class ModeSwitchPiePreferences(AddonPreferences):
    bl_idname = __package__  # use package name, not __name__

    hotkey: StringProperty(
        name="Pie Menu Hotkey",
        description="Keyboard key to open the pie menu",
        default="TAB"
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hotkey Settings:")
        layout.prop(self, "hotkey")

def register():
    bpy.utils.register_class(ModeSwitchPiePreferences)

def unregister():
    bpy.utils.unregister_class(ModeSwitchPiePreferences)
