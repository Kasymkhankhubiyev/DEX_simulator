class AMM_GRAP_ERROR(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class SimulationParamsError(Exception):
    def __init__(self, error_field: str, false_value: str) -> None:
        super().__init__(
            f'{error_field}'
            f'But `{false_value}` was recieved'
        )