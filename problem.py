__all__ = ['Problem1', 'Problem2']


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


class Problem2(Problem):
    def __init__(self, h, n_iter, epsilon: float, x0: float, y0: float):
        super(Problem2, self).__init__(h, n_iter)
        self.epsilon = epsilon
        self.x0 = x0
        self.y0 = y0

    def dxdt(self, xt: float, yt: float) -> float:
        return yt

    def dydt(self, xt: float, yt: float) -> float:
        return self.epsilon * yt * (1 - xt ** 2) - xt
