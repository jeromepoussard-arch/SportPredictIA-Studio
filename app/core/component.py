from dataclasses import dataclass


@dataclass
class Component:
    """
    Classe de base de tous les composants graphiques du Studio.
    """

    id: str
    x: float
    y: float
    width: float
    height: float

    layer: int = 0
    visible: bool = True
    locked: bool = True

    def render(self, canvas):
        raise NotImplementedError(
            "Chaque composant doit implémenter sa méthode render()."
        )