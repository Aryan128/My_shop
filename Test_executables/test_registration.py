from selenium import webdriver
import pytest
from Test_cases.registration import Testregistration
class Testregistration1:
    @pytest.fixture(scope="class")
    def driver(self):
        driver=webdriver.Firefox()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account#account-creation")
        yield driver
        driver.quit()
    @pytest.mark.parametrize("email",["aryanfogi@gmail.com"])
    def test_registration1(self,driver,email):
        r = Testregistration(driver)
        a=r.registration1(email)
        assert a == "CREATE AN ACCOUNT", "NONONON"
