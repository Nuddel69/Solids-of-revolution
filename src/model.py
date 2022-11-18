from core import Vertices, Edges, Shape


class Model:
    def __init__(self,
            vertices: Vertices,
            edges: Edges = None,
        ) -> None:
        
        self._vertices = vertices
        self._edges = edges


    def set_vertices(self, vertices: Vertices) -> None:
        self._vertices = vertices


    def get_vertices(self) -> Vertices:
        return self._vertices


    def get_shape(self) -> Shape:
        return [self._vertices, self._edges]
