import requests
import allure
from config import API_ENDPOINTS


class StellarBurgersAPI:
    """Класс для работы с API Stellar Burgers"""

    @allure.step("API: Авторизовать пользователя")
    def login_user(self, email, password):
        """
        Авторизация пользователя через API
        :param email: email пользователя
        :param password: пароль пользователя
        :return: response object
        """
        login_data = {"email": email, "password": password}
        response = requests.post(API_ENDPOINTS["login"], json=login_data)
        return response

    @allure.step("API: Создать заказ")
    def create_order(self, ingredients, access_token=None):
        """
        Создание заказа через API
        :param ingredients: список ID ингредиентов
        :param access_token: токен авторизации (опционально)
        :return: response object
        """
        headers = {}
        if access_token:
            headers["Authorization"] = access_token

        data = {"ingredients": ingredients}
        response = requests.post(API_ENDPOINTS["orders"], json=data, headers=headers)
        return response

    @allure.step("API: Получить список ингредиентов")
    def get_ingredients(self):
        """
        Получение списка всех ингредиентов через API
        :return: response object
        """
        response = requests.get(API_ENDPOINTS["ingredients"])
        return response

    @allure.step("API: Получить ID ингредиентов по типу")
    def get_ingredient_ids_by_type(self, ingredient_type, count=1):
        """
        Получить ID ингредиентов по типу
        :param ingredient_type: тип ингредиента (bun, main, sauce)
        :param count: количество ингредиентов
        :return: список ID ингредиентов
        """
        response = self.get_ingredients()
        if response.status_code == 200:
            ingredients = response.json().get("data", [])
            filtered = [
                ing["_id"] for ing in ingredients if ing["type"] == ingredient_type
            ]
            return filtered[:count]
        return []