import time
from display import image_file

# defines titles to be written on images
category_titles = (
    "Total Queries",
    "Queries Blocked",
    "Percentage Blocked",
    "Domains on Blocklist",
)
# defines image background colors
bg_colors = ("green", "blue", "orange", "red")
keys = range(4)

while True:
    from display import stats

    all_stats = stats()
    for n in keys:
        stat = all_stats[n]
        if bg_colors[n] == "green":
            f_name = "image1"  # sets filename
            rgb_color = "rgb(0, 166, 90)"  # sets actual rgb color
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
            stat = "{:,}".format(stat)  # places commas where they should be
        image_file(category_titles[n], stat, rgb_color, f_name)
    time.sleep(60)

