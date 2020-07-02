class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result: "TestResult"):
        for test in self.tests:
            test.run(result)


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self):
        return f"{self.run_count} run, {self.error_count} failed"


class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self, result: TestResult):
        result.test_started()

        self.set_up()
        method = getattr(self, self.name)

        try:
            method()
        except Exception:
            result.test_failed()

        self.tear_down()

    def tear_down(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = "set_up "

    def set_up(self):
        self.log = "set_up "

    def test_method(self):
        self.log += "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log += "tear_down "

