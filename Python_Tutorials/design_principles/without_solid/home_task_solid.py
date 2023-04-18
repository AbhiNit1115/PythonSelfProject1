class BaseClass:

    def __init__(self, driver, locator, wait, message):
        self.message = message
        self.driver = driver
        self.locate = locator
        self.wait = wait

    # Methods related to action class.
    def input_text(self, locator_string, input_text):
        self.wait.wait_for_element_until_clickable(locator_string).send_keys(input_text)
        return self

    def get_text(self, locator_string):
        return self.wait.wait_for_element_until_clickable(locator_string).text

    def clear_value(self, locator_string):
        self.wait.wait_for_element_until_clickable(locator_string).clear()
        return self

    # Methods related to locators
    def get_element(self, locator, driver=None):

        if driver:
            return driver.find_element(locator)
        else:
            return self.driver.find_element(locator)

    # Helper Method
    def get_element(self, locator, driver=None):

        if driver:
            return driver.find_elements(locator)
        else:
            return self.driver.find_elements(locator)

    def get_locator_by(locator, separator=None):
        if separator in locator:
            locator_by, locator_str = locator.split(separator)
            if locator_by.lower() == "id":
                return By.ID, locator_str
            elif locator_by.lower() == "name":
                return By.NAME, locator_str
        else:
            raise Exception("Invalid locator type : {}".format(locator))

    # Exceptions method
    def element_not_found(self):
        self.message = "Element Not found"

