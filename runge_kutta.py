import sys
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
                 dydt: Callable[[float, float], float], x0: float, y0: float):
        self.h = h
        self.n_iter = n_iter
        self.dxdt = dxdt
        self.dydt = dydt
        self.xs = [x0]
        self.ys = [y0]

    def solve(self) -> None:
        xs = self.xs
        ys = self.ys
        dxdt = self.dxdt
        dydt = self.dydt
        h = self.h
        if len(xs) > 1 or len(ys) > 1:
            sys.exit('Already solved.')
        xt = xs[0]
        yt = ys[0]
        for _ in range(self.n_iter):
            a1 = dxdt(xt, yt) * h
            b1 = dydt(xt, yt) * h
            a2 = dxdt(xt + 0.5 * a1, yt + 0.5 * b1) * h
            b2 = dydt(xt + 0.5 * a1, yt + 0.5 * b1) * h
            a3 = dxdt(xt + 0.5 * a2, yt + 0.5 * b2) * h
            b3 = dydt(xt + 0.5 * a2, yt + 0.5 * b2) * h
            a4 = dxdt(xt + a3, yt + b3) * h
            b4 = dydt(xt + a3, yt + b3) * h
            xt = (a1 + 2 * a2 + 2 * a3 + a4) / 6
            yt = (b1 + 2 * b2 + 2 * b3 + b4) / 6
            xs.append(xt)
            ys.append(yt)

    def get_output(self) -> (list, list):
        return self.xs, self.ys



