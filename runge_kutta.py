from typing import Callable
__all__ = ['RungeKutta']


class RungeKutta:
    """
    Implementation of Runge-Kutta method.

    Arguments
    ---------
    h: float
        Step size
    n_iter:
        The number of iterations of method.
    dxdt: Callable
        The function dx/dt
    dydt: Callable
        The function dy/dt
    xs: list of float
        record of update of x
    ys: list of float
        record of update of y (= dx/dt)

    """
    def __init__(self, h: int, n_iter: int, dxdt: Callable[[float, float], float],
                 dydt: Callable[[float, float], float]):
        self.h = h
        self.n_iter = n_iter
        self.dxdt = dxdt
        self.dydt = dydt
        self.xs = []
        self.ys = []

    def solve(self) -> None:
        for _ in range(self.n_iter):
            pass

    def get_output(self) -> (list, list):
        return self.xs, self.ys



