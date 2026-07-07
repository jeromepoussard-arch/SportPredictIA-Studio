class InfoBar:
    def __init__(self, x, y, items):
        self.x = x
        self.y = y
        self.items = items

    def render(self, dwg):
        navy = "#102B4A"
        gold = "#D4AF37"
        cyan = "#4EEFFF"
        white = "#FFFFFF"

        width = 914
        height = 125
        block_width = width / 4

        dwg.add(dwg.rect(
            insert=(self.x, self.y),
            size=(width, height),
            rx=14,
            fill=navy,
            stroke=gold,
            stroke_width=3
        ))

        for i, (line1, line2) in enumerate(self.items):
            block_x = self.x + i * block_width

            if i > 0:
                dwg.add(dwg.line(
                    start=(block_x, self.y + 12),
                    end=(block_x, self.y + height - 12),
                    stroke=gold,
                    stroke_width=2
                ))

            dwg.add(dwg.text(
                line1,
                insert=(block_x + block_width / 2, self.y + 57),
                text_anchor="middle",
                font_size=16,
                font_weight="bold",
                fill=white,
                font_family="Arial"
            ))

            dwg.add(dwg.text(
                line2,
                insert=(block_x + block_width / 2, self.y + 97),
                text_anchor="middle",
                font_size=15,
                fill=cyan,
                font_family="Arial"
            ))