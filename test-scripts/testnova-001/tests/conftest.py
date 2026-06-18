import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

def _required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        launched_browser = playwright.chromium.launch(headless=True)
        yield launched_browser
        launched_browser.close()


@pytest.fixture
def browser_context(browser: Browser) -> BrowserContext:
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext) -> Page:
    test_page = browser_context.new_page()
    yield test_page
    test_page.close()


@pytest.fixture
def screenshot_dir() -> str:
    directory = os.environ.get("SCREENSHOT_DIR", "screenshots")
    os.makedirs(directory, exist_ok=True)
    return directory


@pytest.fixture(scope="session")
def base_url() -> str:
    return _required_env("BASE_URL")


@pytest.fixture(scope="session")
def test_username() -> str:
    return _required_env("TEST_USERNAME")


@pytest.fixture(scope="session")
def test_password() -> str:
    return _required_env("TEST_PASSWORD")
