from selenium import webdriver
import pytest
@pytest.fixture(scope="class")
def driver():
    driver=webdriver.Firefox()
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
    yield driver
    driver.quit()