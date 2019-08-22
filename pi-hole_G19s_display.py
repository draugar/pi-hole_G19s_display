import json
from requests_html import HTMLSession
from PIL import Image, ImageDraw, ImageFont
import time

# scrapes statistics from website hosted on my Raspberry pi running pi-hole
def stats():
    session = HTMLSession()
    r = session.get("http://rpi-hole/admin/api.php")
    json_string = r.text
    parsed_json = json.loads(json_string)
    total_queries = parsed_json["dns_queries_today"]
    queries_blocked = parsed_json["ads_blocked_today"]
    percent_blocked = "%.2f%%" % (parsed_json["ads_percentage_today"])
    domains_blocklist = parsed_json["domains_being_blocked"]
    return total_queries, queries_blocked, percent_blocked, domains_blocklist


# creates images, with statistics on them, for display
def image_file(category_title, stat, rbg_color, f_name):
    W, H = (320, 240)
    img = Image.new("RGB", (W, H), color=rgb_color)
    fnt_small = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\ariblk.ttf", 25)
    fnt_big = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\ariblk.ttf", 60)
    d = ImageDraw.Draw(img)
    category_title_w, category_title_h = d.textsize(category_title, font=fnt_small)
    d.text(
        ((W - category_title_w) / 2, (H - category_title_h) / 4),
        category_title,
        font=fnt_small,
        fill="black",
    )
    stat_w, stat_h = d.textsize(stat, font=fnt_big)
    d.text(((W - stat_w) / 2, (H - stat_h) / 2), stat, font=fnt_big, fill="black")
    img.save("E:\\Users\\draugr\\Downloads\\Pi-Hole\\" + f_name + ".jpg")


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

