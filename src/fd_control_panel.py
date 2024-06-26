import src.fd_render_lib as rlib
import src.fd_entity as en
import src.fd_camera as cam
import src.fd_units as un
import src.fd_config as conf

def set_selected(e):
    en.get_entity("control_panel")["selected_entity"] = e

def setup_ctl_panel():
    ctl = en.create_entity("control_panel",{
        "ui_trans": [
            (1, 1),
            (0, 0),
            (325, 300)
        ],

        # button transforms

        "build_ui_trans": [
            (1, 1),
            (35 + conf.ctl_selected_tag_margin, 25 + 90 + 30),
            (325 - 35, 25 + 90 + 30 + 30)
        ],

        "dock_ui_trans": [
            (1, 1),
            (35 + conf.ctl_selected_tag_margin, 25 + 90 + 30 - 40),
            (325 - 35, 25 + 90 + 30 - 40 + 30)
        ],

        "depart_ui_trans": [
            (1, 1),
            (35 + conf.ctl_selected_tag_margin, 25 + 90 + 30),
            (325 - 35, 25 + 90 + 30 + 30)
        ],

        "on_ui_frame": rlib.ctl_renderer,
        "on_click": ctl_on_click,
        "tick": ctl_tick,


        "selected_entity": None,

        "panel_data": {}
    })

    bsel = en.create_entity("build_select", {
        "ui_trans": [
            (2, 1),
            (-250, 0),
            (250, 100)
        ],

        "transceiver_ui_trans": [
            (2, 1),
            (-250 + 15, 15),
            (-250 + 470 // 2 + 15, 100 - 15),
        ],

        "substation_ui_trans": [
            (2, 1),
            (-250 + 470 // 2 + 15, 15),
            (-250 + 470 // 2 * 2 + 15, 100 - 15),
        ],

        # "detector_ui_trans": [
        #     (2, 1),
        #     (-250 + 470 // 3 * 2 + 15, 15),
        #     (-250 + 470 // 3 * 3 + 15, 100 - 15),
        # ],

        "on_ui_frame": rlib.ctl_build_renderer,
        "on_click": ctl_build_on_click,

        "selected_index": 0,
    })

def ctl_on_click(e: dict, click):
    if not rlib.ui_mode == 0:
        return

    if e["panel_data"]["type"] == 0:
        if e["panel_data"]["lost_signal"]:
            return

        # build button
        if cam.is_click_on_ui(e["build_ui_trans"], click):
            rlib.ui_mode = 1
            return True

        # dock button
        elif cam.is_click_on_ui(e["dock_ui_trans"], click):
            un.add_dock_task(e["selected_entity"], False)
            return True
    elif e["panel_data"]["type"] == 1:
        # depart button
        if cam.is_click_on_ui(e["depart_ui_trans"], click) and e["selected_entity"]["units_undocked"] == 0:
            un.game_over_trigged = 2
            return True

    # block click on level
    return cam.is_click_on_ui(e["ui_trans"], click)

def ctl_tick(e: dict):
    sel = e["selected_entity"]
    data = e["panel_data"]

    data["materials"] = sel.get("stored_materials")

    unit = sel.get("unit_index")
    if not unit == None:
        data["selected_title"] = (sel["unit_index"] - 1, sel["pretty_name"])
        data["selected_index"] = sel["unit_index"] - 1
        data["type"] = 0

        if un.has_signal(sel):
            data["lost_signal"] = False

            busy_task = sel.get("busy_with")
            if not busy_task == None:
                if busy_task[0] == 0:
                    data["status"] = "Mining..."
                elif busy_task[0] == 1:
                    if not sel.get("path_target_mine") == None:
                        data["status"] = "Mining..."
                    elif not sel.get("path_target_dock", -1) == -1:
                        data["status"] = "Travelling To Dock..."
                    else:
                        data["status"] = "Travelling..."

                elif busy_task[0] == 2:
                    data["status"] = "Transfering..."
                elif busy_task[0] == 3:
                    data["status"] = "Building..."
                else:
                    raise ValueError("unknown busy task type in ctl_tick")
            elif sel["already_idle"]:
                data["status"] = "Idle"
        else:
            data["lost_signal"] = True
            data["status"] = "Signal lost!"
        
        data["materials"] = sel["stored_materials"]
    else:
        data["selected_title"] = sel["pretty_name"]
        data["selected_index"] = 6
        data["type"] = 1
        data["lost_signal"] = False

        data["status"] = "Online"

def ctl_build_on_click(e: dict, click):
    if not rlib.ui_mode == 1:
        return

    if cam.is_click_on_ui(e["transceiver_ui_trans"], click):
        e["selected_index"] = 0
        return True
    
    elif cam.is_click_on_ui(e["substation_ui_trans"], click):
        e["selected_index"] = 1
        return True

    # elif cam.is_click_on_ui(e["detector_ui_trans"], click):
    #     e["selected_index"] = 2
    #     return True

    # block click on level
    return cam.is_click_on_ui(e["ui_trans"], click)