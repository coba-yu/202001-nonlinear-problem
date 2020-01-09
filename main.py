import os
import matplotlib.pyplot as plt
from runge_kutta import RungeKutta


class Problem:
    def __init__(self, h, n_iter):
        self.h = h
        self.n_iter = n_iter

    def dxdt(self, xt: float, yt: float) -> float:
        raise NotImplementedError

    def dydt(self, xt: float, yt: float) -> float:
        raise NotImplementedError


class Problem1(Problem):
    def __init__(self, h, n_iter, epsilon: float, x0: float, y0: float):
        super(Problem1, self).__init__(h, n_iter)
        self.epsilon = epsilon
        self.x0 = x0
        self.y0 = y0

    def dxdt(self, xt: float, yt: float) -> float:
        return yt

    def dydt(self, xt: float, yt: float) -> float:
        return self.epsilon * yt * (1 - xt ** 2) - xt


if __name__ == '__main__':
    out_dir = '../report_tex'
    for i, epsilon in enumerate([0.05, 0.1, 0.3, 1.0]):
        p1 = Problem1(0.05, 4000, epsilon, 0.1, 0.1)
        rk = RungeKutta(p1.h, p1.n_iter, p1.dxdt, p1.dydt, p1.x0, p1.y0)
        rk.solve()
        x, y = rk.get_output()

        plt.figure(figsize=(18, 6))
        plt.subplot(131)
        plt.plot(x, y)
        plt.title(u'$x$-$\dot{x}$')
        plt.xlabel(u'$x$')
        plt.ylabel(u'$\dot{x}$')

        plt.subplot(132)
        plt.plot(x)
        plt.title(u'$t$-$x$')
        plt.xlabel(u'$t$')
        plt.ylabel(u'$\dot{x}$')

        plt.subplot(133)
        plt.plot(y)
        plt.title(u'$t$-$\dot{x}$')
        plt.xlabel(u'$t$')
        plt.ylabel(u'$\dot{x}$')
        plt.savefig(os.path.join(out_dir, f'problem1_{i}.eps'))
