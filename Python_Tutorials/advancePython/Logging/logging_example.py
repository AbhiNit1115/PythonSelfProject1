# If we are using multiple loggers we have to use "Handlers" to do all the configuration. Handlers forwards
# events from Loggers to outputs such as console, file or syslog server. Loggers can have multiple(or zero)
# handlers assigned to them, letting us log events to multiple destinations simultaneously.
# Types of Handlers
# File Handlers: It allows us to log to a file.
# Stream Handler: Allows us to log to system standard out/ system standard error. Standard out and standard
# error are nothing but basically python console (which come below for any any error like compile, runtime)
from selenium.common.exceptions import NoSuchElementException


class base:
    def button_dict(self, btn):
        button = dict()
        button['Yes'] = "ABC"
        return button[btn]

    def click_button(self, btn_name):
        self.button_dict(btn_name).click()


class Child(base):
    def click_button(self, btn):
        try:
            button = dict()
            button['No'] = "XYZ"
            button[btn].click()
        except NoSuchElementException:
            super().click_button()


child_obj = Child()
child_obj.click_button("Yes")
