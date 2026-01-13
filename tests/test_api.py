import allure
from api.api_add_cart import AddToCartAPI
from constants import API1_url
from constants import API2_url
from api.api_delete_cart import DeleteFromCart


@allure.feature("Тестирование API интернет-магазина")
@allure.story("Добавление продукта в корзину")
def test_add_product_to_cart():
    """ 
                        Тест для метода добавления продукта в корзину. 
                        Проверяет, успешен ли запрос на добавление товара в корзину. 
    """
    with allure.step("Добавить книгу в корзину"):
        product_id = 2841859  # ID продукта для добавления
        item_list_name = "search"  # Имя списка, откуда добавляется продукт
        # Создаем экземпляр API для добавления в корзину
        add_to_cart_api = AddToCartAPI(API1_url)
        status_code = add_to_cart_api.add_product_to_cart(
            product_id, item_list_name)  # Выполняем запрос

    with allure.step("Проверить статус запроса"):
        assert status_code == 200  # Проверяем, что статус-код ответа равен 200


@allure.feature("Тестирование API интернет-магазина")
@allure.story("Удаление товара из корзины")
def test_delete_product_from_cart():
    """ 
                    Тест для удаления товара из корзины. 
                    Проверяет, что товар успешно удален. 
    """
    product_id = 2967760  # ID добавленной книги
    item_list_name = "search"  # Имя списка, откуда добавляется продукт

    # Создаем экземпляр класса для добавления товара в корзину
    add_to_cart_api = AddToCartAPI(API1_url)

    # Добавляем товар в корзину
    status_code = add_to_cart_api.add_product_to_cart(
        product_id, item_list_name)

    with allure.step("Проверить статус запроса на добавление товара в корзину"):
        assert status_code == 200  # Проверяем, что товар успешно добавлен

    # Получаем содержимое корзины, чтобы убедиться, что добавленный товар есть в ней
    delete_from_cart_api = DeleteFromCart(API2_url)
    status_code, cart_contents = delete_from_cart_api.get_cart_contents()

    # Проверяем успешность получения содержимого корзины
    with allure.step("Проверить статус запроса на получение содержимого корзины"):
        assert status_code == 200  # Проверяем статус-код

    # Получаем ID товара из корзины
    prod_id = cart_contents['products'][0]['goodsId']

    # Удаляем товар по ID
    status_code = delete_from_cart_api.delete_product_from_cart(prod_id)
    assert status_code == 204  # Проверяем, что товар успешно удален