from phoopy.console import Application


class TestApplication(object):
    def test_init(self):
        assert Application is not None
