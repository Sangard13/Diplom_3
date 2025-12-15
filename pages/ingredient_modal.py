"""Page Object для модального окна ингредиента"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModal(BasePage):
    """Класс для работы с модальным окном деталей ингредиента"""

    def __init__(self, driver):
        super().__init__(driver, "")
        self.locators = IngredientModalLocators()
        self.url = "/"

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_opened(self):
        """Проверить, что модальное окно открыто"""
        return self.is_element_visible(IngredientModalLocators.MODAL_CONTENT)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Проверить, что модальное окно закрыто"""
        return self.wait_for_element_to_disappear(IngredientModalLocators.MODAL_CONTENT)

    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        """Получить текст заголовка модального окна"""
        return self.get_element_text(IngredientModalLocators.MODAL_TITLE)

    @allure.step("Получить название ингредиента")
    def get_ingredient_name(self):
        """Получить название ингредиента из модального окна"""
        return self.get_element_text(IngredientModalLocators.INGREDIENT_NAME)

    @allure.step("Кликнуть на кнопку закрытия (крестик)")
    def click_close_button(self):
        """Закрыть модальное окно кликом по крестику"""
        self.click_element(IngredientModalLocators.CLOSE_BUTTON)

    @allure.step("Проверить наличие изображения ингредиента")
    def is_ingredient_image_visible(self):
        """Проверить, отображается ли изображение ингредиента"""
        return self.is_element_visible(IngredientModalLocators.INGREDIENT_IMAGE)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрыть модальное окно"""
        self.click_close_button()
        return self.is_modal_closed()

    @allure.step("Проверить открытие деталей ингредиента")
    def is_ingredient_details_visible(self):
        """Проверить что детали ингредиента видны"""
        # В вашем приложении открывается страница, а не модальное окно
        return "/ingredient/" in self.driver.current_url

    @allure.step("Проверить калорийность ингредиента")
    def get_calories(self):
        """Получить значение калорийности ингредиента"""
        return self.get_element_text(IngredientModalLocators.CALORIES_VALUE)

    @allure.step("Проверить белки ингредиента")
    def get_proteins(self):
        """Получить значение белков ингредиента"""
        return self.get_element_text(IngredientModalLocators.PROTEINS_VALUE)

    @allure.step("Проверить жиры ингредиента")
    def get_fat(self):
        """Получить значение жиров ингредиента"""
        return self.get_element_text(IngredientModalLocators.FATS_VALUE)

    @allure.step("Проверить углеводы ингредиента")
    def get_carbohydrates(self):
        """Получить значение углеводов ингредиента"""
        return self.get_element_text(IngredientModalLocators.CARBOHYDRATES_VALUE)

    @allure.step("Получить все данные о пищевой ценности")
    def get_all_nutrition_data(self):
        """Получить все данные о пищевой ценности ингредиента"""
        return {
            "calories": self.get_calories(),
            "proteins": self.get_proteins(),
            "fat": self.get_fat(),
            "carbohydrates": self.get_carbohydrates()
        }

    @allure.step("Кликнуть на оверлей для закрытия")
    def click_overlay_to_close(self):
        """Закрыть модальное окно кликом на оверлей"""
        self.click_element(IngredientModalLocators.MODAL_OVERLAY)
        return self.is_modal_closed()

