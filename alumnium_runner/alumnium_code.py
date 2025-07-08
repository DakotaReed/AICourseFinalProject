import os
import pytest
from dotenv import load_dotenv
from selenium.webdriver import Chrome
from alumnium import Alumni
from alumnium.models import Model, Provider

# Load environment variables
load_dotenv()

# Ensure API key exists
@pytest.fixture(scope="session", autouse=True)
def check_api_key():
    if not os.environ.get("GOOGLE_API_KEY"):
        pytest.fail("Missing GOOGLE_API_KEY in .env file", pytrace=False)

# Set up the LLM provider once for all tests
@pytest.fixture(scope="session", autouse=True)
def configure_model():
    Model.current = Model(
        provider=Provider.GOOGLE,
        name="gemini-2.5-flash-preview-04-17"
    )

# Selenium WebDriver fixture
@pytest.fixture
def driver():
    driver = Chrome()
    driver.get("https://todomvc.com/examples/vue/dist/#/")
    yield driver
    driver.quit()

def test_todomvc_task_completion(driver):
    al = Alumni(driver)

    al.do("Add a task: 'pick up the kids'")
    al.do("Add a task: 'buy milk'")
    al.do("mark all tasks complete and stop when all tasks are marked")
    al.check("task 'buy milk' is completed")
