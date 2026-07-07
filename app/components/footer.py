class Footer:
    """
    Composant Footer DS07
    ---------------------
    Affiche le nom SportPredictIA centré en bas de l'affiche.
    """

    def __init__(self, text="SportPredictIA"):
        self.text = text

    def render(self, dwg, width, height):

        GOLD = "#F6D36A"

        dwg.add(
            dwg.text(
                self.text,
                insert=(width / 2, height - 40),
                text_anchor="middle",
                font_size=24,
                font_weight="bold",
                fill=GOLD,
                font_family="Arial"
            )
        )