bl_info = {
    "name": "Custom addon",
    "author": "Hari",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Adds randomly placed sphere",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from random import randint
from bpy.types import (Operator, Panel)

class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "random.1"
    bl_label = "Simple Random Operator"

    def execute(self, context):
        for i in range(100):
            randomscale = randint(0,3)
            x = randint(-50, 50); y = randint(-50, 50); z = randint(-50, 50)
            bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(randomscale, randomscale, randomscale))
            bpy.ops.object.shade_smooth()
        
        return {'FINISHED'}

class CustomPanel(bpy.types.Panel):
    bl_label = "Random Panel"
    bl_idname = "OBJECT_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "random spheres"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='SPHERE')

from bpy.utils import register_class, unregister_class

_classes = [
    ButtonOperator,
    CustomPanel
]

def register():
    for cls in _classes:
        register_class(cls)
    
    
def unregister():
    for cls in _classes:
        unregister_class(cls)

if __name__ == "__main__":
    register()
