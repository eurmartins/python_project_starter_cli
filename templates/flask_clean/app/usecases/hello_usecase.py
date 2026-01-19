class HelloUseCase:
    def execute(self, name: str = "World"):
        return f"Hello, {name}!"