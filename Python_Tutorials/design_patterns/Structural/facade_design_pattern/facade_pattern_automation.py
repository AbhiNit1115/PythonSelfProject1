import requests


class PostTest:

    @staticmethod
    def request_to_post():
        request_url = requests.post("http://httpbin.org/post", params={"name": "Abhi", "job": "Functional_Automation"})
        print(request_url.status_code)


class DeleteTest:

    @staticmethod
    def request_to_delete():
        request_url = requests.delete("http://httpbin.org/delete")
        response_validation = request_url.text
        print(response_validation)


class GetTest:

    @staticmethod
    def request_to_get():
        request_url = requests.get("http://httpbin.org/get")
        response_validation = request_url.headers
        print(response_validation)


class CRUDFacade:

    def __init__(self):
        self.get_test = GetTest
        self.post_test = PostTest
        self.delete_test = DeleteTest

    def execute_crud_facade(self) -> None:
        self.get_test.request_to_get()
        self.post_test.request_to_post()
        self.delete_test.request_to_delete()


crud = CRUDFacade()
crud.execute_crud_facade()

