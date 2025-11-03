import bpy
from bpy.types import Operator

class WM_OT_pie_select_mode(Operator):
    bl_idname = "wm.pie_select_mode"
    bl_label = "Pie Select Mode"
    bl_options = {'UNDO'}

    mode: bpy.props.EnumProperty(
        items=[
            ('VERT', "Vertex", ""),
            ('EDGE', "Edge", ""),
            ('FACE', "Face", ""),
        ],
        name="Select Mode"
    )

    def execute(self, context):
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type=self.mode)
        return {'FINISHED'}

class WM_OT_call_mode_pie(Operator):
    bl_idname = "wm.call_mode_pie"
    bl_label = "Call Mode Switch Pie Menu"

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_mode_switch_pie")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(WM_OT_pie_select_mode)
    bpy.utils.register_class(WM_OT_call_mode_pie)

def unregister():
    bpy.utils.unregister_class(WM_OT_call_mode_pie)
    bpy.utils.unregister_class(WM_OT_pie_select_mode)
