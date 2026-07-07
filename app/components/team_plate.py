class TeamPlate:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def render(self, dwg):
        navy = "#102B4A"
        gold = "#D4AF37"
        white = "#FFFFFF"

        dwg.add(dwg.rect(
            insert=(self.x, self.y),
            size=(240, 62),
            rx=12,
            fill=navy,
            stroke=gold,
            stroke_width=3
        ))

        dwg.add(dwg.text(
            self.name,
            insert=(self.x + 120, self.y + 42),
            text_anchor="middle",
            font_size=28,
            font_weight="bold",
            fill=white,
            font_family="Arial"
        ))