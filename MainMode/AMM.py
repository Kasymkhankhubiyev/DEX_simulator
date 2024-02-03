from abc import ABC

class AMM(ABC):
    def __init__(self, depth, data) -> None:
        super().__init__()

        self.depth = depth
        self.data = data
        self.current_price = 0.


    def get_order(self) -> None:
        pass

    def response_to_order(self) -> None:
        pass

    def update_graph(self) -> None:
        pass


class UniswapV3(AMM):
    def __init__(self, depth) -> None:
        super().__init__()


    def _balance_func(self) -> None:
        # f(x, y) = x * y = K = depth
        pass


class SUMM(AMM):
    def __init__(self, depth) -> None:
        super().__init__()


    def _balance_func(self) -> None:
        # f(x, y) = x + y = K = depth
        pass


class WeightedSUMM(AMM):
    def __init__(self, depth) -> None:
        super().__init__()


    def _balance_func(self) -> None:
        # f(x, y) = w_1 * x + w_2 * y = K = depth
        pass