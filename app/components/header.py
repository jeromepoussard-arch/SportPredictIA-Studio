class Header:
    def __init__(self, title="COUPE DU MONDE 2026", subtitle="1/8ᵉ DE FINALE"):
        self.title = title
        self.subtitle = subtitle

    def render(self, dwg, width):
        gold = "#F6D36A"
        gold_dark = "#D4AF37"
        gold_shadow = "#8C6A16"
        navy_dark = "#061323"
        navy = "#102B4A"
        cyan = "#4EEFFF"
        white = "#FFFFFF"

        header_gradient = dwg.linearGradient(
            start=("0%", "0%"),
            end=("100%", "100%"),
            id="headerGradientV2"
        )
        header_gradient.add_stop_color("0%", navy_dark)
        header_gradient.add_stop_color("50%", navy)
        header_gradient.add_stop_color("100%", navy_dark)
        dwg.defs.add(header_gradient)

        title_gradient = dwg.linearGradient(
            start=("0%", "0%"),
            end=("0%", "100%"),
            id="titleGoldGradient"
        )
        title_gradient.add_stop_color("0%", "#FFF1A6")
        title_gradient.add_stop_color("45%", gold)
        title_gradient.add_stop_color("100%", gold_dark)
        dwg.defs.add(title_gradient)

        outer = [
            (100, 42), (924, 42), (960, 97),
            (924, 153), (100, 153), (64, 97)
        ]

        middle = [
            (118, 52), (906, 52), (938, 97),
            (906, 143), (118, 143), (86, 97)
        ]

        inner = [
            (140, 64), (884, 64), (910, 97),
            (884, 131), (140, 131), (114, 97)
        ]

        dwg.add(dwg.polygon(
            points=outer,
            fill="none",
            stroke=gold_shadow,
            stroke_width=8,
            opacity=0.75
        ))

        dwg.add(dwg.polygon(
            points=outer,
            fill="url(#headerGradientV2)",
            stroke=gold,
            stroke_width=4
        ))

        dwg.add(dwg.polygon(
            points=middle,
            fill="none",
            stroke=gold_dark,
            stroke_width=2
        ))

        dwg.add(dwg.polygon(
            points=inner,
            fill="none",
            stroke=cyan,
            stroke_width=2,
            opacity=0.95
        ))

        for y, opacity in [(67, 0.22), (72, 0.10)]:
            dwg.add(dwg.line(
                start=(155, y),
                end=(870, y),
                stroke=white,
                stroke_width=1,
                opacity=opacity
            ))

        dwg.add(dwg.text(
            self.title,
            insert=(width / 2 + 3, 116),
            text_anchor="middle",
            font_size=48,
            font_weight="bold",
            fill="#000000",
            opacity=0.45,
            font_family="Arial"
        ))

        dwg.add(dwg.text(
            self.title,
            insert=(width / 2, 113),
            text_anchor="middle",
            font_size=48,
            font_weight="bold",
            fill="url(#titleGoldGradient)",
            font_family="Arial"
        ))

        phase_gradient = dwg.linearGradient(
            start=("0%", "0%"),
            end=("100%", "100%"),
            id="phaseGradientV2"
        )
        phase_gradient.add_stop_color("0%", "#07182B")
        phase_gradient.add_stop_color("50%", "#12385E")
        phase_gradient.add_stop_color("100%", "#07182B")
        dwg.defs.add(phase_gradient)

        phase = [
            (342, 166), (682, 166), (706, 189),
            (682, 214), (342, 214), (318, 189)
        ]

        phase_inner = [
            (356, 173), (668, 173), (688, 189),
            (668, 207), (356, 207), (336, 189)
        ]

        dwg.add(dwg.polygon(
            points=phase,
            fill="url(#phaseGradientV2)",
            stroke=cyan,
            stroke_width=3
        ))

        dwg.add(dwg.polygon(
            points=phase_inner,
            fill="none",
            stroke=white,
            stroke_width=0.8,
            opacity=0.25
        ))

        dwg.add(dwg.text(
            self.subtitle,
            insert=(width / 2, 198),
            text_anchor="middle",
            font_size=25,
            font_weight="bold",
            fill=white,
            font_family="Arial"
        ))