import pytest

def pytest_addoption(parser):
    parser.addoption("--runlive", action="store_true", help="run live tests")
    parser.addoption("--dbuser", action="store", default="root:root", help="db user:pwd for mysql tests")
    parser.addoption("--server", action="store", default="localhost:8085/api", help="set api-server: host:port/api-path")
    parser.addoption("--append", action="store_true", help="don't clear previous live test results")

