import bpy
from bpy.types import Menu

# ------------------------------------------------------------------------
#    PIE MENU CLASS
# ------------------------------------------------------------------------

class VIEW3D_MT_mode_switch_pie(Menu):
    bl_label = "Mode Switch Pie Menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        # LEFT
        pie.operator("object.mode_set", text="Weight Paint", icon="WPAINT_HLT").mode = 'WEIGHT_PAINT'
        # RIGHT
        pie.operator("object.mode_set", text="Sculpt Mode", icon="SCULPTMODE_HLT").mode = 'SCULPT'
        # BOTTOM
        pie.operator("wm.pie_select_mode", text="Edge Select", icon="EDGESEL").mode = 'EDGE'
        # TOP
        pie.operator("object.mode_set", text="Object Mode", icon="OBJECT_DATAMODE").mode = 'OBJECT'
        # TOP LEFT
        pie.operator("object.mode_set", text="Vertex Paint", icon="VPAINT_HLT").mode = 'VERTEX_PAINT'
        # TOP RIGHT
        pie.operator("object.mode_set", text="Texture Paint", icon="TPAINT_HLT").mode = 'TEXTURE_PAINT'
        # BOTTOM LEFT
        pie.operator("wm.pie_select_mode", text="Vertex Select", icon="VERTEXSEL").mode = 'VERT'
        # BOTTOM RIGHT
        pie.operator("wm.pie_select_mode", text="Face Select", icon="FACESEL").mode = 'FACE'

def register():
    bpy.utils.register_class(VIEW3D_MT_mode_switch_pie)

def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_mode_switch_pie)
