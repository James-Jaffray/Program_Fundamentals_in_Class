class Coin:
    def __init__(self, type: str) -> None:
        self.type = type

    def __str__(self) -> str:
        return f"{self.type}"

    def 