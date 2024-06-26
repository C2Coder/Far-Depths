# == WARNING: These settings are not ment to be changed randomly and can cause crashes if set incorectly ==

# graphics

empty_color = (8, 8, 8)
fog_color = (2, 2, 2)

stone_color = (127, 127, 127)
oxy_color = (164, 164, 255)
goal_color = (64, 245, 64)
border_color = (100, 80, 100)

loading_status_texts = (
    "> Undocking...",
    "> Searching for a suitable location...",
    "> Traveling to location...",
    "> Landing at location...",
    "> Get ready for deployment!"
)

ui_foreground_color = (255, 255, 255)
ui_background_color = (4, 4, 4)
ui_foreground_faded_color = (127, 127, 127)

nls_log_colors = (
    (225, 225, 225),
    (200, 200, 64),
    (255, 16, 16)
)

nls_border_size = 5
nls_cursor_margin = 5
nls_log_line_size = 14
nls_outline_margin = 10
nls_outline_width = 10

ctl_border_size = 5
ctl_button_border_size = 3
ctl_selected_tag_margin = 25
ctl_selected_tag_border_size = 3

timer_border_size = 5
timer_outline_margin = 10
timer_outline_width = 10
timer_warn_at_time = 25

# level gen

level_size = (500, 500)

fill_percent = 25
border_size = 3
level_seed = None # random

num_of_oxy_deposits_min_max = (60, 70)
oxy_deposit_size_min_max = (4, 8)

num_of_goal_deposits_min_max = (20, 30)
goal_deposit_size_min_max = (6, 12)

# game behaviour

mine_times = (
    None, # air (unused)
    .8, # stone
    .4, # oxy
    2, # goal
    float('inf'), # border (infinite)
)

move_time = .2
transfer_time = .05

cam_speed = 500

unit_colors = (
    (255, 0, 0),
    (0, 255, 0),
    (0, 255, 255),
    (255, 255, 0),
    (255, 0, 255),
    (255, 127, 0),
    (127, 0, 255)
)

struct_colors = (
    (200, 200, 200),
    (225, 225, 225)
)

pipeline_color = (64, 64, 64)

oxy_to_power_time = 40
timer_eta_zero_offset = 5

initial_base_oxy_count = 80

struct_power_usages = (
    4,
    6,
)

struct_build_times = (
    5,
    8
)

struct_build_costs = (
    (5, 0),
    (10, 0)
)

base_signal_distance = 60
substation_signal_distance = 85
transceiver_signal_distance = 65

base_pipeline_distance = 75
substation_pipeline_distance = 75

# menu

secret_titles = (
    "Far Depths - Mining and stayin' alive, stayin' alive",
    "Far Depths - Never gonna mine you up",
    "Far Depths - Failing to reach centrals weekly quota",
    "Far Depths - Being a great asset for central",
    "Far Depths - Mining for Democracy",
    "Far Depths - There are no enemies in this game, right?",
    "Far Depths - Mining in an OSHA approved definitely non-lethal submersible",
    "Far Depths - Mining with only 24 new warnings per second",
    "Far Depths - Mining and ignoring all the bugs that don't exists.",
)

# dev options

dev_fastmap = False
dev_frametimes = False