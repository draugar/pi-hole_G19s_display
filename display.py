import json
from requests_html import HTMLSession
from PIL import Image, ImageDraw, ImageFont
import configparser

# scrapes statistics from website hosted on my Raspberry pi running pi-hole
def stats():
    session = HTMLSession()
    r = session.get(pi_hole_api)
    json_string = r.text
    parsed_json = json.loads(json_string)
    total_queries = parsed_json["dns_queries_today"]
    queries_blocked = parsed_json["ads_blocked_today"]
    percent_blocked = "%.2f%%" % (parsed_json["ads_percentage_today"])
    domains_blocklist = parsed_json["domains_being_blocked"]
    return total_queries, queries_blocked, percent_blocked, domains_blocklist


# creates images, with statistics on them, for display
def image_file(category_title, stat, rgb_color, f_name):
    W, H = (320, 240)
    img = Image.new("RGB", (W, H), color=rgb_color)
    fnt_small = ImageFont.truetype(arial_black_font, 25)
    fnt_big = ImageFont.truetype(arial_black_font, 60)
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
    img.save(image_dir + f_name + ".jpg")


# uses config file
config = configparser.ConfigParser()
config.read("config.ini")
pi_hole_api = config.get("Paths", "PiHoleApi")
arial_black_font = config.get("Paths", "ArialBlackFont")
image_dir = config.get("Paths", "ImageDir")

