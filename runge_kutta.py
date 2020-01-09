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
            a1 = dxdt(xt, yt)
            b1 = dydt(xt, yt)
            a2 = dxdt(xt + 0.5 * h * a1, yt + 0.5 * h * b1)
            b2 = dydt(xt + 0.5 * h * a1, yt + 0.5 * h * b1)
            a3 = dxdt(xt + 0.5 * h * a2, yt + 0.5 * h * b2)
            b3 = dydt(xt + 0.5 * h * a2, yt + 0.5 * h * b2)
            a4 = dxdt(xt + h * a3, yt + h * b3)
            b4 = dydt(xt + h * a3, yt + h * b3)
            xt += (a1 + 2 * a2 + 2 * a3 + a4) * h / 6
            yt += (b1 + 2 * b2 + 2 * b3 + b4) * h / 6
            xs.append(xt)
            ys.append(yt)

    def get_output(self) -> (list, list):
        return self.xs, self.ys



