from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.management import call_command
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumTests(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()

    def consultar_repositorios_con_mas_seguidores(self):
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Repositorios COVID con más observadores/watchers\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Observadores\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "COVID-19")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0

    