from selenium import webdriver

def test_wp_title():
    driver = webdriver.Chrome()
    driver.get("https://wp.pl")
    print(driver.title)
    assert driver.title == "Wirtualna Polska - Wszystko co ważne - www.wp.pl"
    driver.quit()