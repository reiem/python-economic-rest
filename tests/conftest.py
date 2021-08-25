from fixtures.auth import auth


def pytest_addoption(parser):
    parser.addoption('--app-id', action='store')
    parser.addoption('--token', action='store')
