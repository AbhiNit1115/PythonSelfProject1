# In Selenium Chrome/Firefox/Safari/IE driver concrete classes implements WebDriver interface

from selenium import webdriver
import abc


class IOrganizeManager(abc):

    @abc.abstractmethod
    def start_service(self):
        pass

    @abc.abstractmethod
    def stop_service(self):
        pass

    @abc.abstractmethod
    def create_driver(self):
        pass

    @abc.abstractmethod
    def get_driver(self):
        pass

    @abc.abstractmethod
    def quit_driver(self):
        pass


class OrganizeChromeDriver(IOrganizeManager):

    def __init__(self, driver):
        self.driver = driver
        self.commence = "Commence Driver Service"
        self.cease = "Stop Driver Service"
        self.create_driver = "Create Webdriver"
        self.driver.get_driver = webdriver.Chrome()
        self.driver.quit = "Quit Driver"

    def start_service(self):
        self.driver = webdriver.Chrome
        return self.commence

    def stop_service(self):
        self.driver = webdriver.Chrome
        stop = self.cease
        return stop

    def create_driver(self):
        return self.create_driver

    def get_driver(self):
        return self.driver.get_driver

    def quit_driver(self):
        return self.driver.quit


class OrganizeFFDriver(IOrganizeManager):

    def __init__(self, driver):
        self.driver = driver
        self.commence = "Commence Driver Service"
        self.cease = "Stop Driver Service"
        self.create_driver = "Create Webdriver"
        self.driver.get_driver = webdriver.firefox
        self.driver.quit = "Quit Driver"

    def start_service(self):
        self.driver = webdriver.firefox
        return self.commence

    def stop_service(self):
        self.driver = webdriver.firefox
        stop = self.cease
        return stop

    def create_driver(self):
        return self.create_driver

    def get_driver(self):
        return self.driver.get_driver

    def quit_driver(self):
        return self.driver.quit


class DriverManagerFactory:

    @staticmethod
    def select_webdriver(driver_type):
        try:
            if driver_type == "Chrome":
                return OrganizeChromeDriver
        except:
            raise AssertionError("Chrome Driver not available")
        try:
            if driver_type == "Firefox":
                return OrganizeFFDriver
        except:
            raise AssertionError("FF Driver not available")


class Test1:

    def chrome_tests(self):
        driver_manager = DriverManagerFactory.select_webdriver("Chrome")
        driver_manager.create_driver()
        driver_manager.get_driver()
        driver_manager.start_service()
        driver_manager.stop_service()
        driver_manager.quit_driver()

class Test2:

    def ff_tests(self):
        driver_manager = DriverManagerFactory.select_webdriver("Firefox")
        driver_manager.create_driver()
        driver_manager.get_driver()
        driver_manager.start_service()
        driver_manager.stop_service()
        driver_manager.quit_driver()
