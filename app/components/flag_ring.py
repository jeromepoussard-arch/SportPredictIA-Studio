class FlagRing:
    def __init__(self, x, y, country_name):
        self.x = x
        self.y = y
        self.country_name = country_name

    def render(self, dwg):
        gold_light = "#F6D36A"
        gold = "#D4AF37"
        gold_dark = "#8C6A16"
        navy = "#102B4A"
        navy_dark = "#07182B"
        cyan = "#4EEFFF"
        white = "#FFFFFF"

        # Ombre externe
        dwg.add(dwg.circle(
            center=(self.x + 5, self.y + 7),
            r=100,
            fill="#000000",
            opacity=0.35
        ))

        # Anneau extérieur doré
        dwg.add(dwg.circle(
            center=(self.x, self.y),
            r=96,
            fill=gold_dark,
            stroke=gold_light,
            stroke_width=4
        ))

        # Couronne principale
        dwg.add(dwg.circle(
            center=(self.x, self.y),
            r=88,
            fill=gold,
            stroke=gold_light,
            stroke_width=5
        ))

        # Anneau bleu intérieur
        dwg.add(dwg.circle(
            center=(self.x, self.y),
            r=74,
            fill=navy_dark,
            stroke=cyan,
            stroke_width=2,
            opacity=0.95
        ))

        # Zone drapeau placeholder
        dwg.add(dwg.circle(
            center=(self.x, self.y),
            r=64,
            fill=navy,
            stroke=gold_light,
            stroke_width=2
        ))

        # Reflet haut gauche
        dwg.add(dwg.circle(
            center=(self.x - 22, self.y - 24),
            r=42,
            fill="none",
            stroke=white,
            stroke_width=2,
            opacity=0.25
        ))

        # Point lumineux
        dwg.add(dwg.circle(
            center=(self.x - 36, self.y - 40),
            r=5,
            fill=white,
            opacity=0.55
        ))