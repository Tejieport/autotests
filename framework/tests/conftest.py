import pytest
from playwright.sync_api import sync_playwright
# import requests
# from faker import Faker
# from HelloApp.booking.constant import HEADERS, BASE_URL

@pytest.fixture(scope='session')
def custom_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    browser.close()
    playwright.stop()

# @pytest.fixture(scope='session')
# def session_req():
#     return requests.Session()
#
# faker = Faker()
# @pytest.fixture(scope='session')
# def auth_session():
#     session = requests.Session()
#     session.headers.update(HEADERS)
#
#     response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json={"username" : "admin", "password" : "password123"})
#     assert response.status_code == 200, "Ошибка авторизации"
#     token = response.json().get("token")
#     assert token is not None, "В ответе не оказалось токена"
#
#     session.headers.update({"Cookie": f"token={token}"})
#     return session
#
# @pytest.fixture()
# def booking_data():
#     return {
#         "firstname": faker.first_name(),
#         "lastname": faker.last_name(),
#         "totalprice": faker.random_int(min=100, max=100000),
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2024-04-05",
#             "checkout": "2024-04-08"
#         },
#         "additionalneeds": "Cigars"
#     }
#
# @pytest.fixture()
# def booking_data_1():
#     return {
#         "firstname": faker.first_name(),
#         "lastname": faker.last_name(),
#         "totalprice": faker.random_int(min=1, max=99),
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2024-04-05",
#             "checkout": "2024-04-08"
#         },
#         "additionalneeds": faker.text()
#     }
#
# @pytest.fixture()
# def booking_data_2():
#     return {
#         "firstname": faker.first_name(),
#         "lastname": faker.last_name(),
#         "totalprice": faker.random_int(min=1, max=99),
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2024-13-40",
#             "checkout": "2024-13-35"
#         },
#         "additionalneeds": faker.text()
#     }
#
# @pytest.fixture()
# def booking_data_patch_1():
#     return {
#         "firstname": faker.first_name(),
#         "lastname": faker.last_name(),
#     }
#
# @pytest.fixture()
# def booking_data_patch_2():
#     return {
#         "totalprice": 1510000000000000000000,
#     }
#
# @pytest.fixture()
# def create_booking(booking_data, auth_session):
#     create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
#     assert create_booking.status_code == 200
#     booking_id = create_booking.json().get("bookingid")
#     assert booking_id is not None, "ID букинга не найден в ответе"
#     return booking_id
#
# @pytest.fixture()
# def delete_bookinga(auth_session):
#     def _delete_booking(id):
#         delete_response = auth_session.delete(f"{BASE_URL}/booking/{id}")
#         assert delete_response.status_code == 201, f"Ошибка при удалении букинга с ID {id}"
#     return _delete_booking
#
# @pytest.fixture()
# def booking_filters():
#     return "checkin=2024-10-01,&checkout=2024-10-29"
#
# @pytest.fixture()
# def booking_filters_1():
#     return "firstname=Александр&lastname=Бородач"
#
# # @pytest.fixture(scope='session')
# # def delete_booking(booking_data, auth_session, create_booking):
# #     booking_id = create_booking
# #     delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
# #     assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"
# #
# # @pytest.fixture(scope='session')
# # def get_booking(booking_data, auth_session, create_booking):
# #     booking_id = create_booking
# #     get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
# #     assert get_booking.status_code == 200
# #
# # @pytest.fixture(scope='session')
# # def get_booking_after_delete(booking_data, auth_session, create_booking, delete_booking):
# #     booking_id = delete_booking
# #     get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
# #     assert get_deleted_booking.status_code == 404, "Букинг не был удален"
#
#
# # В рабочих проектах и тому подобным, лишнего кода и комментов быть не должно (как вот эти фикстуры выше), только по делу)
#
# # Определение фикстуры
# # @pytest.fixture
# # def sample_data():
# #     data = [1, 2, 3, 4, 5]
# #     print("Setup: Создание данных")
# #     yield data
# #     print("Teardown: Очистка данных")
# #
# # # Тестовая функция, использующая фикстуру
# # def test_sum(sample_data):
# #     assert sum(sample_data) == 15
# # @pytest.fixture(scope='function')
# # def random_int():
# #     return random.randint(0, 100)
#
# @pytest.fixture(scope='function')
# def function_scope():
#     return random.randint(1, 99)
#
# @pytest.fixture(scope='class')
# def class_scope():
#     return random.randint(100, 199)
#
# @pytest.fixture(scope='module')
# def module_scope():
#     return random.randint(200, 299)
#
# @pytest.fixture(scope='session')
# def session_scope():
#     return random.randint(300, 399)