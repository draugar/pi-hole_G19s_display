import time
from pi_hole_G19s_display import (
    pi_hole_api,
    arial_black_font,
    image_dir,
    stats,
    image_file,
)

category_titles = (
    "Total Queries",
    "Queries Blocked",
    "Percentage Blocked",
    "Domains on Blocklist",
)
bg_colors = ("green", "blue", "orange", "red")
all_stats = stats()
keys = range(4)

while True:
    for n in keys:
        stat = all_stats[n]
        if bg_colors[n] == "green":
            f_name = "image1"
            rgb_color = "rgb(0, 166, 90)"
        elif bg_colors[n] == "blue":
            f_name = "image2"
            rgb_color = "rgb(0, 192, 239)"
        elif bg_colors[n] == "orange":
            f_name = "image3"
            rgb_color = "rgb(243, 156, 18)"
        elif bg_colors[n] == "red":
            f_name = "image4"
            rgb_color = "rgb(221, 75, 57)"
        if bg_colors[n] in ("green", "blue", "red"):
            stat = "{:,}".format(stat)
        image_file(category_titles[n], stat, rgb_color, f_name)
    time.sleep(60)

