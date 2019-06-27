import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", default="Firefox")
    parser.addoption("--env", default="local")
    parser.addoption("--url", default="test")