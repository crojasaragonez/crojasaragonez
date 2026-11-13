#!/usr/bin/env python3
"""Outline Geist lettering so the profile banner renders consistently on GitHub.

Requires fonttools with WOFF2 support. Pass the website's Geist font with --font.
Edit assets/banner-source.svg, then run this script to rebuild assets/banner.svg.
"""

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)
    tree = ET.parse(root / "assets/banner-source.svg")
    source_font = TTFont(args.font)
    fonts = {}

    for group in tree.iter():
        for element in list(group):
            if element.tag != f"{{{namespace}}}text":
                continue
            weight = int(element.get("font-weight", "400"))
            if weight not in fonts:
                fonts[weight] = instantiateVariableFont(source_font, {"wght": weight})
            font = fonts[weight]
            glyphs = font.getGlyphSet()
            cmap = font.getBestCmap()
            size = float(element.get("font-size"))
            scale = size / font["head"].unitsPerEm
            spacing = float(element.get("letter-spacing", "0"))
            cursor = float(element.get("x"))
            baseline = float(element.get("y"))
            pen = SVGPathPen(glyphs)
            label = element.text or ""
            for character in label:
                if ord(character) not in cmap:
                    raise ValueError(f"Missing glyph for {character!r}")
                glyph = glyphs[cmap[ord(character)]]
                glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, cursor, baseline)))
                cursor += glyph.width * scale + spacing
            attributes = {
                "d": pen.getCommands(),
                "aria-label": label,
                "fill": element.get("fill", group.get("fill", "#f8fafc")),
            }
            path = ET.Element(f"{{{namespace}}}path", attributes)
            group.insert(list(group).index(element), path)
            group.remove(element)
        group.attrib.pop("font-family", None)

    tree.write(root / "assets/banner.svg", encoding="unicode", xml_declaration=False)
    print("Built assets/banner.svg with outlined Geist lettering.")


if __name__ == "__main__":
    main()
