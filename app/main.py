class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.was_run = None

    def test_method(self):
        self.was_run = 1
