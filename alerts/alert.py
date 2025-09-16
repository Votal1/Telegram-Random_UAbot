from cairosvg import svg2png
from PIL import Image
from io import BytesIO


def generate_map(input_svg, webp_file, current_alert):
    regions = ["UA43", "UA07", "UA05", "UA12", "UA14", "UA18", "UA21", "UA23", "UA26", "UA32", "UA30", "UA35", "UA09", "UA46", "UA48", "UA51", "UA53", "UA56", "UA40", "UA59", "UA61", "UA63", "UA65", "UA68", "UA71", "UA77", "UA74"]

    filtered_alert = "".join([ch for ch in current_alert if ch != "N"])
    filtered_regions = [val for ch, val in zip(current_alert, regions) if ch != "N"]

    with open(input_svg, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        if 'fill' in line:
            for region in filtered_regions:
                if region in line:
                    state = filtered_alert[filtered_regions.index(region)]
                    color = '6f9c76'
                    if state == 'A':
                        color = '880808'
                    elif state == 'P':
                        color = 'e3735e'
                    line = line.replace('6f9c76', color)
        updated_lines.append(line)

    updated_svg_str = "".join(updated_lines)
    png_bytes = BytesIO()

    svg2png(bytestring=updated_svg_str.encode("utf-8"), write_to=png_bytes)

    png_bytes.seek(0)

    with Image.open(png_bytes) as img:
        img.save(webp_file, format="WEBP")
