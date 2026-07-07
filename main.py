from app.renderer.renderer import Renderer
from app.components.header import Header
from app.components.flag_ring import FlagRing
from app.components.team_plate import TeamPlate
from app.components.info_bar import InfoBar
from app.components.footer import Footer
from app.poster import Poster

poster = Poster()
poster.render()

renderer = Renderer()
dwg = renderer.dwg

W = renderer.WIDTH
H = renderer.HEIGHT

NAVY = "#07182B"
NAVY_2 = "#102B4A"
GOLD = "#D4AF37"
GOLD_LIGHT = "#F6D36A"
CYAN = "#4EEFFF"
WHITE = "#FFFFFF"
BLACK = "#101010"

renderer.background(NAVY)

# Bordure
dwg.add(dwg.rect((25, 25), (W - 50, H - 50), fill="none", stroke=GOLD, stroke_width=3))
dwg.add(dwg.rect((45, 45), (W - 90, H - 90), fill="none", stroke=CYAN, stroke_width=1))

Header().render(dwg, W)

# Drapeaux / anneaux
FlagRing(245, 330, "Portugal").render(dwg)
FlagRing(779, 330, "Espagne").render(dwg)

dwg.add(dwg.text("VS", insert=(W / 2, 350), text_anchor="middle",
                 font_size=64, font_weight="bold", fill=GOLD_LIGHT, font_family="Arial"))

# Plaques équipes
TeamPlate(115, 455, "PORTUGAL").render(dwg)
TeamPlate(669, 455, "ESPAGNE").render(dwg)

# Skyline placeholder
dwg.add(dwg.rect((60, 560), (904, 260), fill="#08111D", opacity=0.9))
for i, h in enumerate([120, 160, 95, 180, 130, 220, 150, 100, 170, 135]):
    x = 80 + i * 85
    dwg.add(dwg.rect((x, 820 - h), (55, h), fill="#101820", stroke=GOLD, stroke_width=1))

# Stade mieux placé
dwg.add(dwg.ellipse((W / 2, 875), (390, 95), fill=BLACK, stroke=GOLD_LIGHT, stroke_width=4))
dwg.add(dwg.ellipse((W / 2, 875), (300, 55), fill=NAVY_2, stroke=WHITE, stroke_width=2))
dwg.add(dwg.rect((310, 910), (404, 45), rx=6, fill=BLACK, stroke=GOLD, stroke_width=2))
dwg.add(dwg.text("DALLAS STADIUM", insert=(W / 2, 940), text_anchor="middle",
                 font_size=24, font_weight="bold", fill=WHITE, font_family="Arial"))

# Trophée placeholder au-dessus du stade
dwg.add(dwg.rect((420, 515), (184, 350), rx=50, fill="#9B7416", stroke=GOLD_LIGHT, stroke_width=5))
dwg.add(dwg.circle((512, 560), 85, fill="#B88918", stroke=GOLD_LIGHT, stroke_width=4))
dwg.add(dwg.text("TROPHÉE", insert=(W / 2, 710), text_anchor="middle",
                 font_size=26, font_weight="bold", fill=WHITE, font_family="Arial"))

# Terre plus basse, moins envahissante
dwg.add(dwg.ellipse((W / 2, 1165), (590, 135), fill=NAVY_2, stroke=CYAN, stroke_width=3))
dwg.add(dwg.text("TERRE / DALLAS", insert=(W / 2, 1175), text_anchor="middle",
                 font_size=30, font_weight="bold", fill=WHITE, font_family="Arial"))

# Rayon lumineux
dwg.add(dwg.line((W / 2, 870), (W / 2, 1165), stroke=GOLD_LIGHT, stroke_width=4, opacity=0.75))

# Info bar
InfoBar(
    55,
    1308,
    [
        ("6 JUILLET 2026", "21H FR / 14H LOCAL"),
        ("MATCH 93", "1/8ᵉ DE FINALE"),
        ("DALLAS STADIUM", "ARLINGTON, USA"),
        ("DALLAS", "TEXAS, USA"),
    ]
).render(dwg)

# Footer
Footer().render(dwg, W, H)

# Sauvegarde
renderer.save("ds10_v02.svg")

print("✅ Affiche générée : exports/ds10_v02.svg")