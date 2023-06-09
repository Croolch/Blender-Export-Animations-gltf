# function: export all actions in blender file to glb
# date: 2023-6-9
# author: ivan and github copilot
# blender version: 3.4.1
# bug: please make sure there is no animation data in armature

import bpy
import os

# 解决windows和macos路径分隔符不同的问题, 默认macos方式
# if in windows, change split_char to "\\"
split_char = "/"
if os.name == "nt":
    split_char = "\\"

# export to blend file location
basedir = os.path.dirname(bpy.data.filepath)

if not basedir:
    raise Exception("Blend file is not saved")

# export folder under basedir
export_folder = basedir + split_char +"glbs"

# if export_folder does not exist, create it
if not os.path.exists(export_folder):
    os.makedirs(export_folder)

# 要导出的骨架名称
# armature name to export
armature_name = "Armature"

# 清除已选择的object
bpy.ops.object.select_all(action="DESELECT")

# select the armature object according to armature name
bpy.ops.object.select_pattern(pattern=armature_name)

# 请手动确保armature下没有动画数据，因为我写不出来清楚动画数据的代码

# create animation data container
bpy.context.object.animation_data_create()

# push down each action to NLA tracks to export
for action in bpy.data.actions:
    track = bpy.context.object.animation_data.nla_tracks.new()
    strip = track.strips.new(name=action.name, start=0, action=action)

    # export according to output settings
    bpy.ops.export_scene.gltf(
        filepath=export_folder+split_char+action.name+".glb",
        check_existing=True,
        export_format="GLB",
        ui_tab="ANIMATION",
        export_force_sampling=False,
        export_nla_strips=True,
        export_anim_single_armature=False,
        will_save_settings=False,
    )

    # 向控制台输出完整的文件名
    print("written:", action.name+".glb")

    # 清除刚加入的NLA track
    bpy.context.object.animation_data.nla_tracks.remove(track)

