import parabola as p


class Trajectory:
    def __init__(
        self,
        measured_coordinate_1: tuple[float, float],
        measured_coordinnate_2: tuple[float, float],
        y_intercept: float = 0,
    ) -> None:
        """
        The class for a trajectory of a baseball

        measured_coordinate_1: After how many feet horizontally was the ball heigh vertically feet
        measured_coordinate_2: After how many feet horizontally was the ball heigh vertically feet
        y_intercept: How high was the ball when it was hit
        """

        self.x1, self.y1 = measured_coordinate_1
        self.x2, self.y2 = measured_coordinnate_2
        self.y_int = y_intercept

        self.a, self.b, self.c = p.find_parabola(
            y_intercept, self.x1, self.y1, self.x2, self.y2
        )
        self.distance = max(p.find_parabolic_roots(self.a, self.b, self.c))

    def plot(self) -> None:
        """
        Plots the graph
        """

        p.plot_graph(self.a, self.b, self.c, self.distance)

    def __str__(self) -> str:
        return f"Equation: {p.str_equation(self.a, self.b, self.c)}\nDistance: {round(self.distance)}"


t = Trajectory((50, 30), (200, 60), y_intercept=5)
print(t)
t.plot()
