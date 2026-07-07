from app.renderer.renderer import Renderer
from app.components.header import Header
from app.components.flag_ring import FlagRing
from app.components.team_plate import TeamPlate
from app.components.info_bar import InfoBar
from app.components.footer import Footer


class Poster:
    def __init__(self):
        self.renderer = Renderer()
        self.dwg = self.renderer.dwg
        self.W = self.renderer.WIDTH
        self.H = self.renderer.HEIGHT

        self.NAVY = "#07182B"
        self.NAVY_2 = "#102B4A"
        self.GOLD = "#D4AF37"
        self.GOLD_LIGHT = "#F6D36A"
        self.CYAN = "#4EEFFF"
        self.WHITE = "#FFFFFF"
        self.BLACK = "#101010"

    def render(self):
        self.renderer.background(self.NAVY)

        self._render_frame()
        self._render_header()
        self._render_flags()
        self._render_vs()
        self._render_team_plates()
        self._render_skyline_placeholder()
        self._render_stadium_placeholder()
        self._render_trophy_placeholder()
        self._render_earth_placeholder()
        self._render_light_beam()
        self._render_info_bar()
        self._render_footer()

        self.renderer.save("ds10_v02.svg")
        print("✅ Affiche générée : exports/ds10_v02.svg")

    def _render_frame(self):
        self.dwg.add(self.dwg.rect(
            (25, 25),
            (self.W - 50, self.H - 50),
            fill="none",
            stroke=self.GOLD,
            stroke_width=3
        ))
        self.dwg.add(self.dwg.rect(
            (45, 45),
            (self.W - 90, self.H - 90),
            fill="none",
            stroke=self.CYAN,
            stroke_width=1
        ))

    def _render_header(self):
        Header().render(self.dwg, self.W)

    def _render_flags(self):
        FlagRing(245, 330, "Portugal").render(self.dwg)
        FlagRing(779, 330, "Espagne").render(self.dwg)

    def _render_vs(self):
        self.dwg.add(self.dwg.text(
            "VS",
            insert=(self.W / 2, 350),
            text_anchor="middle",
            font_size=64,
            font_weight="bold",
            fill=self.GOLD_LIGHT,
            font_family="Arial"
        ))

    def _render_team_plates(self):
        TeamPlate(115, 455, "PORTUGAL").render(self.dwg)
        TeamPlate(669, 455, "ESPAGNE").render(self.dwg)

    def _render_skyline_placeholder(self):
        self.dwg.add(self.dwg.rect(
            (60, 560),
            (904, 260),
            fill="#08111D",
            opacity=0.9
        ))

        for i, h in enumerate([120, 160, 95, 180, 130, 220, 150, 100, 170, 135]):
            x = 80 + i * 85
            self.dwg.add(self.dwg.rect(
                (x, 820 - h),
                (55, h),
                fill="#101820",
                stroke=self.GOLD,
                stroke_width=1
            ))

    def _render_stadium_placeholder(self):
        self.dwg.add(self.dwg.ellipse(
            (self.W / 2, 875),
            (390, 95),
            fill=self.BLACK,
            stroke=self.GOLD_LIGHT,
            stroke_width=4
        ))
        self.dwg.add(self.dwg.ellipse(
            (self.W / 2, 875),
            (300, 55),
            fill=self.NAVY_2,
            stroke=self.WHITE,
            stroke_width=2
        ))
        self.dwg.add(self.dwg.rect(
            (310, 910),
            (404, 45),
            rx=6,
            fill=self.BLACK,
            stroke=self.GOLD,
            stroke_width=2
        ))
        self.dwg.add(self.dwg.text(
            "DALLAS STADIUM",
            insert=(self.W / 2, 940),
            text_anchor="middle",
            font_size=24,
            font_weight="bold",
            fill=self.WHITE,
            font_family="Arial"
        ))

    def _render_trophy_placeholder(self):
        self.dwg.add(self.dwg.rect(
            (420, 515),
            (184, 350),
            rx=50,
            fill="#9B7416",
            stroke=self.GOLD_LIGHT,
            stroke_width=5
        ))
        self.dwg.add(self.dwg.circle(
            (512, 560),
            85,
            fill="#B88918",
            stroke=self.GOLD_LIGHT,
            stroke_width=4
        ))
        self.dwg.add(self.dwg.text(
            "TROPHÉE",
            insert=(self.W / 2, 710),
            text_anchor="middle",
            font_size=26,
            font_weight="bold",
            fill=self.WHITE,
            font_family="Arial"
        ))

    def _render_earth_placeholder(self):
        self.dwg.add(self.dwg.ellipse(
            (self.W / 2, 1165),
            (590, 135),
            fill=self.NAVY_2,
            stroke=self.CYAN,
            stroke_width=3
        ))
        self.dwg.add(self.dwg.text(
            "TERRE / DALLAS",
            insert=(self.W / 2, 1175),
            text_anchor="middle",
            font_size=30,
            font_weight="bold",
            fill=self.WHITE,
            font_family="Arial"
        ))

    def _render_light_beam(self):
        self.dwg.add(self.dwg.line(
            (self.W / 2, 870),
            (self.W / 2, 1165),
            stroke=self.GOLD_LIGHT,
            stroke_width=4,
            opacity=0.75
        ))

    def _render_info_bar(self):
        InfoBar(
            55,
            1308,
            [
                ("6 JUILLET 2026", "21H FR / 14H LOCAL"),
                ("MATCH 93", "1/8ᵉ DE FINALE"),
                ("DALLAS STADIUM", "ARLINGTON, USA"),
                ("DALLAS", "TEXAS, USA"),
            ]
        ).render(self.dwg)

    def _render_footer(self):
        Footer().render(self.dwg, self.W, self.H)