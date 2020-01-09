import os
import matplotlib.pyplot as plt
from problem import Problem1, Problem2
from runge_kutta import RungeKutta


if __name__ == '__main__':
    out_dir = '../report_tex'

    # Problem 1
    for i, epsilon in enumerate([0.05, 0.1, 0.3, 1.0]):
        h = 0.05
        n_iter = 4000
        p1 = Problem1(h, n_iter, epsilon, 0.1, 0.1)
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
        plt.savefig(os.path.join(out_dir, f'problem1_{i}.eps'), dpi=300)
