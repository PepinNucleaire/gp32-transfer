import re
import math
from xml.etree import cElementTree
import serial

from . import const_gp39


Const = const_gp39.Const()


def read_file(path_of_file):
    try:
        root = cElementTree.parse(path_of_file).getroot()
    except:
        print("Could not open input file!")
    return root


def extract_wpt(node):
    # find waypoint
    lon = float(node.attrib["lon"])
    furuno_lon = round(math.floor(abs(lon)) * 100 + ((abs(lon) - math.floor(abs(lon))) * 60), 3)
    lat = float(node.attrib["lat"])
    furuno_lat = round(math.floor(abs(lat)) * 100 + ((abs(lat) - math.floor(abs(lat))) * 60), 3)
    tmp_wpt = {
        "lon": "%09.3f" % furuno_lon,
        "NS": "S" if lon > 0 else "N",
        "lat": "%08.3f" % furuno_lat,
        "EW": "W" if lat > 0 else "E",
        "name": "",
        "desc": "",
        "color": Const.defaultColor,
        "mark": Const.defaultMark,
    }
    for wpt in node:
        if re.search("\}name", wpt.tag) and wpt.text:
            tmp_wpt["name"] = wpt.text.strip().upper()
        if re.search("\}desc", wpt.tag) and wpt.text:
            tmp_wpt["desc"] = wpt.text.strip().upper()
        if re.search("\}sym", wpt.tag) and wpt.text:
            splitSym = re.split(",", wpt.text)
            if len(splitSym) == 2:
                foundmark = [f for f in Const.marks if (Const.marks[f] == splitSym[0].strip())]
                tmp_wpt["mark"] = foundmark[0] if len(foundmark) > 0 else Const.defaultMark
                tmp_wpt["color"] = (
                    Const.colors.index(splitSym[1].strip())
                    if splitSym[1].strip() in Const.colors
                    else Const.defaultColor
                )
            else:
                foundmark = [f for f in Const.marks if (Const.marks[f] == wpt.text.strip())]
                tmp_wpt["mark"] = foundmark[0] if len(foundmark) > 0 else Const.defaultMark
    return tmp_wpt
