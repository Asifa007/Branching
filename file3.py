class i:
    def __init__(self, height=10):
        self.height = height

    def build_pattern(self):
        return ["*" * row for row in range(1, self.height + 1)]

    def render(self):
        for line in self.build_pattern():
            print(line)


if __name__ == "__main__":
    i().render()