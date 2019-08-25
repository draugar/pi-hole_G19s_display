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


# creates images, with text on them, for display
def image_file(header_text, main_text, footer_text, rgb_color, f_name):
    W, H = (320, 240)
    img = Image.new("RGB", (W, H), color=rgb_color)
    fnt_header = ImageFont.truetype(arial_black_font, 25)
    fnt_main = ImageFont.truetype(arial_black_font, 60)
    fnt_footer = ImageFont.truetype(arial_font, 25)
    d = ImageDraw.Draw(img)

    header_text_w, header_text_h = d.textsize(header_text, font=fnt_header)
    d.text(
        # horizontally centers header text and places it above main text
        ((W - header_text_w) / 2, (H - header_text_h) / 4),
        header_text,
        font=fnt_header,
        fill="black",
    )
    main_text_w, main_text_h = d.textsize(main_text, font=fnt_main)
    # centers main text
    d.text(
        ((W - main_text_w) / 2, (H - main_text_h) / 2),
        main_text,
        font=fnt_main,
        fill="black",
    )

    footer_text_w, footer_text_h = d.textsize(footer_text, font=fnt_footer)
    # centers footer text and places it under main text
    d.text(
        ((W - footer_text_w) / 2, (H - footer_text_h * 1.4)),
        footer_text,
        font=fnt_footer,
        fill="black",
    )

    img.save(image_dir + f_name + ".jpg")


# uses config.ini file
config = configparser.ConfigParser()
config.read("config.ini")
pi_hole_api = config.get("Paths", "PiHoleApi")
arial_font = config.get("Paths", "ArialFont")
arial_black_font = config.get("Paths", "ArialBlackFont")
image_dir = config.get("Paths", "ImageDir")

