class FlagRing:
    def __init__(self, x, y, country_name):
        self.x = x
        self.y = y
        self.country_name = country_name

    def render(self, dwg):
        gold = "#F6D36A"
        gold_dark = "#D4AF37"
        navy = "#102B4A"
        white = "#FFFFFF"

        dwg.add(dwg.circle(
            center=(self.x, self.y),
            r=92,
            fill=navy,
            stroke=gold,
            stroke_width=14
        ))

        dwg.add(dwg.circle(
            center=(self.x, self.y),
            r=77,
            fill=navy,
            stroke=gold_dark,
            stroke_width=3
        ))

        dwg.add(dwg.circle(
            center=(self.x - 18, self.y - 18),
            r=58,
            fill="none",
            stroke=white,
            stroke_width=1,
            opacity=0.25
        ))