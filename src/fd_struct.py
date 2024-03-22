import pygame as pg

import src.fd_entity as en
import src.fd_render_lib as rlib
import src.fd_camera as cam
import src.fd_level as lvl

# == Far Depths Structure Controllers ==

next_struct_index = 1

def spawn_struct(p):
    global next_struct_index

    s = en.create_entity(f"struct_{next_struct_index}", {
        "transform": [
            None, # set on ticks
            (18, 18)
        ],

        "grid_trans": p,

        # "on_frame": rlib.struct_renderer,
        "tick": struct_tick,

        "pretty_name": (2, f"Structure #{next_struct_index}"),
    })

    next_struct_index += 1

    return s

def setup_struct_build_ghost():
    en.create_entity("struct_ghost", {
        "transform": [
            None, # set on ticks
            (18, 18)
        ],

        "on_frame": rlib.struct_ghost_renderer,
        "tick": struct_ghost_tick,
    })

def struct_tick(e: dict):
    pass

def struct_ghost_tick(e: dict):
    e["transform"][0] = lvl.grid_to_world_space(lvl.world_to_grid_space(cam.inverse_translate(pg.mouse.get_pos())))