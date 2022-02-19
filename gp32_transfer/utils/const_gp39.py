# flake8: noqa: E501
class Const(object):
    def __init__(self):
        self.header = """<?xml version="1.0"  encoding="ISO-8859-1"?>\n<gpx creator="jujumini" version="1.1">\n\n"""
        # self.metadata = """<metadata>
        # <link href="http://www.garmin.com">
        #   <text>Garmin International</text>
        # </link>
        # <time>{time}</time>
        # </metadata>\n\n"""
        self.waypoint = """  <wpt lat = "{lat}" lon = "{lon}">\n   <name>{name}</name>\n  <extensions>\n<GP39Symbol>{mark}</GP39Symbol>\n				<FECColor>{color}</FECColor>\n				<GP39Comment></GP39Comment>\n				<GP39Flag>1</GP39Flag>\n	</extensions>\n</wpt>\n\n"""
        # self.route = """    <rtept lat="{lat}" lon="{lon}">\n      <name>{name}</name>\n      <desc>{desc}</desc>\n      <sym>{mark}, {color}</sym>\n    </rtept>\n\n"""
        # self.routeStart = """  <rte>\n    <name>{name}</name>\n"""
        # self.routeEnd = """  </rte>\n\n"""
        self.footer = "</gpx>"
        self.colors = ["Black", "Red", "Yellow", "Green", "Brown", "Purple", "Blue"]
        self.marks = {
            "@q": "Pin",
            "@r": "Flag",
            "@s": "Flag",
            "@t": "Fishing Area",
            "@u": "Fishing Area",
            "@v": "Fishing Area",
            "@w": "Shipwreck",
            "@x": "Anchor",
            "@y": "Skull And Crossbones",
            "@z": "Flag",
        }
        self.defaultMark = "@q"
        self.defaultColor = 0
        self.defaultColorText = "Blue"
