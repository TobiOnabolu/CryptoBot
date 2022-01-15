class Price():
    pair: str = ''
    exchange: str = ''
    current: float = 0
    lowest: float = 0
    highest: float = 0
    currency: str = ''
    asset: str = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

