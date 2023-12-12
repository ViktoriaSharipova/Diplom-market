import allure
from Selectors import ExpressCartFunc
from allure_commons.types import AttachmentType


@allure.title('Тест авторизации')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_login(browser):
    with allure.step('Открыть сайт'):
        login = ExpressCartFunc(browser)
        login.go_to_site()
    with allure.step('Авторизоваться на сайте'):
        login.login()
    allure.attach(login.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест поиск')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_find(browser):
    with allure.step('Открыть сайт'):
        find = ExpressCartFunc(browser)
        find.go_to_site()
    with allure.step('Проверка работы поиска'):
        find.find()
    allure.attach(find.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест открытие товара')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_open_list(browser):
    with allure.step('Открыть сайт'):
        open_list = ExpressCartFunc(browser)
        open_list.go_to_site()
    with allure.step('Октрытие товара'):
        open_list.open_list()
    allure.attach(open_list.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест добавления в корзину')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_add_to_cart(browser):
    with allure.step('Открыть сайт'):
        add = ExpressCartFunc(browser)
        add.go_to_site()
    with allure.step('Добавить товар в корзину'):
        add.add_to_cart()
    allure.attach(add.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест окрытия корзины')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_open_cart(browser):
    with allure.step('Открыть сайт'):
        cart = ExpressCartFunc(browser)
        cart.go_to_site()
    with allure.step('Открыть корзину'):
        cart.open_cart()
    allure.attach(cart.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест заказа')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_checkout(browser):
    with allure.step('Открыть сайт'):
        checkout = ExpressCartFunc(browser)
        checkout.go_to_site()
    with allure.step('Добавить товар в корзину и нажать оплатить'):
        checkout.checkout()


@allure.title('Тест изменения языка')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_switch_language(browser):
    with allure.step('Открыть сайт'):
        language = ExpressCartFunc(browser)
        language.go_to_site()
    with allure.step('Изменение языка'):
        language.switch_language()
    allure.attach(language.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест отзыва')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_review(browser):
    with allure.step('Открыть сайт'):
        review = ExpressCartFunc(browser)
        review.go_to_site()
    with allure.step('Клик по кнопке добавить отзыв'):
        review.add_review()
    allure.attach(review.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест навигации')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_navbar(browser):
    with allure.step('Открыть сайт'):
        navbar = ExpressCartFunc(browser)
        navbar.go_to_site()
    with allure.step('Клик по навигационному бару'):
        navbar.test_nav_bar()
    allure.attach(navbar.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


@allure.title('Тест истории профиля')
@allure.feature('проверка основных функций')
@allure.story('тестирование expresscart')
def test_profile(browser):
    with allure.step('Открыть сайт'):
        profile = ExpressCartFunc(browser)
        profile.go_to_site()
    with allure.step('Клик по навигационному бару'):
        profile.test_nav_bar()
    allure.attach(profile.browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
