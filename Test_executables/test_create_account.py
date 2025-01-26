import time

import pytest
from Test_cases.registration import Testregistration
from Test_cases.create_account import Testregistration1


@pytest.mark.parametrize("name,title, last_name,email, password, day, month , years",[("Naam","Mr","Jatt","nidhisharma@gmail.com","?0gZj%W40dO8",'1',"2","2002"), ("Naam","Mr","Jatt","swamisharma@gmail.com","Swami@123",'1',"4","2002"), ("Naam","Mr","Jatt","aryanfogi@gmail.com","?0gZj%W40dO8",'1',"2","2002"),("Naam","Mr","Jatt","test123@gmail.com","?0gZj%W40dO8",'1',"2","2002")])
def test_create(name,title, last_name,email, password, day, month , years,driver):
    r = Testregistration(driver)
    c= Testregistration1(driver)
    r.registration1(email)
    time.sleep(8)
    c.creating_account(name,title, last_name, password, day, month , years)
    time.sleep(5)

    c.register_button()
    time.sleep(8)
