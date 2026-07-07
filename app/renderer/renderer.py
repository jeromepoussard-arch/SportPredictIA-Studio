import svgwrite
from pathlib import Path


class Renderer:

    WIDTH = 1024
    HEIGHT = 1536

    def __init__(self):

        self.dwg = svgwrite.Drawing(
            size=(self.WIDTH, self.HEIGHT)
        )

    def background(self, color):

        self.dwg.add(

            self.dwg.rect(

                insert=(0, 0),

                size=("100%", "100%"),

                fill=color

            )

        )

    def save(self, filename):

        Path("exports").mkdir(exist_ok=True)

        self.dwg.saveas(f"exports/{filename}")