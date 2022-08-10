from abc import ABC, abstractmethod
from webdriver_manager import driver


class ToolSelectionStrategy(ABC):

    @abstractmethod
    def set_driver(self, web_driver):
        pass

    @abstractmethod
    def select_plugin(self, plug_in):
        pass


class ZephyrPlugin(ToolSelectionStrategy):

    def __init__(self):
        self.driver = driver

    def set_driver(self, web_driver):
        self.driver = web_driver

    def select_plugin(self, plug_in):
        return plug_in


class XrayPlugin(ToolSelectionStrategy):

    def __init__(self):
        self.driver = driver

    def set_driver(self, web_driver):
        self.driver = web_driver

    def select_plugin(self, plug_in):
        return plug_in


class JiraConfluenceContext:

    tool_selection_strategy: ToolSelectionStrategy

    @staticmethod
    def select_zephyr_plugin():
        zep_plugin = ZephyrPlugin()
        zep_plugin.select_plugin("this is zephyr plugin")
        zep_plugin.set_driver(driver)

    @staticmethod
    def select_xray_plugin():
        xray_plugin = XrayPlugin()
        xray_plugin.select_plugin("this is xray plugin")
        xray_plugin.set_driver(driver)


class StrategyTest:

    def zephyr_results_test(self, jira_confluence_context: JiraConfluenceContext):
        jira_confluence_context.select_xray_plugin()

    def xray_results_test(self, jira_confluence_context: JiraConfluenceContext):
        jira_confluence_context.select_zephyr_plugin()



