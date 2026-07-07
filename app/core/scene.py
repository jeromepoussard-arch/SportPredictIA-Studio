class Scene:
    """
    Une scène contient tous les composants d'une affiche.
    Elle les rend dans le bon ordre grâce au système de layers.
    """

    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def render(self, canvas):
        ordered_components = sorted(
            self.components,
            key=lambda component: component.layer
        )

        for component in ordered_components:
            if component.visible:
                component.render(canvas)