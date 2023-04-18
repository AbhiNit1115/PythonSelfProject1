from abc import ABC, abstractmethod


class LoginPage(ABC):  # To Log to any application
    """Interface for login"""

    def __init__(self, hrberry_login):
        self._hrberry_login = hrberry_login

    @abstractmethod
    def user_details(self):
        pass


class HRBerryLogin(LoginPage):
    """Implements Login Page"""

    def __init__(self, hrberry_login):
        super().__init__(hrberry_login)
        self._hrberry_login = hrberry_login

    def user_details(self):
        return self._hrberry_login


class TestEmployeeLogin(HRBerryLogin):
    """Existing feature to test employee login"""

    def __init__(self, hrberry_login):
        super().__init__(hrberry_login)
        self._hrberry_login = hrberry_login

    def user_details(self):
        return "{}".format(self._hrberry_login.user_details())

    def employee_login_test(self):
        return "Employee logged in successfully"


class HRBerryLoginDecorator(HRBerryLogin):
    """HR Berry Login Decorator interface which will have additional functionality"""

    @abstractmethod
    def hr_login_test(self):
        pass


class TestHRLogin(HRBerryLoginDecorator):
    """Wrapper to test HR login implements the decorator interface"""

    def __init__(self, hrberry_login):
        super().__init__(hrberry_login)
        self._hrberry_login = hrberry_login

    def user_details(self):
        return "{}".format(self._hrberry_login.user_details())

    def hr_login_test(self):
        return "HR logged in successfully"


hrberry_page = HRBerryLogin("HR berry")
hr_login = TestHRLogin(HRBerryLogin("hr login details"))

print("Website Name :", hrberry_page.user_details())
print("Login Details :", hr_login.user_details())
print("Info Message:", hr_login.hr_login_test())
