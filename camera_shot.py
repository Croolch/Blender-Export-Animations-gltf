# shot clothes and hair in different camera using blender

import bpy
import os

# export to blend file location
basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

# export folder under basedir
export_folder = basedir + "\\glbs"

# if export_folder does not exist, create it
if not os.path.exists(export_folder):
    os.makedirs(export_folder)

# define the armature and body parts colloction corresponding to its camera
armature = "Armature"
body_camera_col = {
    "m_hair": "m_hair_camera",
    "m_top": "m_top_camera",
    "m_bottom": "m_bottom_camera",
    "m_shoes": "m_shoes_camera",
}

# this function render all clothes and hairs using corresponding camera
# parameters:
#  basedir: the folder of blend file
#  export_folder: the folder to export glb files

def renderCamera(basedir, export_folder, col_camera_set):
    # 清除已选择的object
    bpy.ops.object.select_all(action="DESELECT")
    # for each
