import time

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class ExpressCartLocators:
    searchField = (By.XPATH, '//*[@id="frm_search"]')
    searchButton = (By.XPATH, '//*[@id="btn_search"]')
    backpacksNavBar = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[2]/a')
    bootsNavBar = (By.XPATH, '//*[@id="feedback"]/div/div/h5')
    homeNavBar = (By.XPATH, '//*[@id="navbarMenu"]/ul/li[1]/a')
    profileButton = (By.XPATH, '//*[@id="navbarText"]/ul/li[1]/a')
    languageDropdown = (By.XPATH, '//*[@id="dropdownMenuButton"]')
    englishLaunguage = (By.XPATH, '//*[@id="navbarText"]/ul/div/div/li[1]/a')
    italiaonoLanguage = (By.XPATH, '//*[@id="navbarText"]/ul/div/div/li[2]/a')
    russianLanguage = (By.XPATH, '//*[@id="navbarText"]/ul/div/div/li[3]/a')
    cartButton = (By.XPATH, '//*[@id="navbarText"]/ul/li[2]/a')
    pulloverAddToCart = (By.XPATH, '//*[@id="container"]/div/div[1]/div/div[1]/div/p/a')
    pulloverList = (By.XPATH, '//*[@id="container"]/div/div[1]/div/div[1]/div/div/a/h3')
    addButton = (By.XPATH, '//*[@id="container"]/div/div/div/div[2]/div/div[1]/div/div[2]/button')
    removeButton = (By.XPATH, '//*[@id="container"]/div/div/div/div[2]/div/div[1]/div/div[1]/button')
    addReviewButton = (By.XPATH, '//*[@id="add-review"]')
    mainPageButton = (By.XPATH, '/html/body/nav/a')
    loginField = (By.XPATH, '//*[@id="email"]')
    passwordField = (By.XPATH, '//*[@id="password"]')
    loginButton = (By.XPATH, '//*[@id="customerloginForm"]')
    clearCartButton = (By.XPATH, '//*[@id="empty-cart"]')
    checkoutButton = (By.XPATH, '//*[@id="cart"]/div[2]/div/a')
    addToCartListButton = (By.XPATH, '//*[@id="container"]/div/div/div/div[2]/div/div[2]/button')
    profileDropdown = (By.XPATH, '//*[@id="dropdownMenuButton"]')
    accountButton = (By.XPATH, '//*[@id="navbarText"]/ul/div[2]/div/li[1]/a')


class ExpressCartFunc(BasePage):

    def login(self):
        self.driverwait(ExpressCartLocators.profileButton).click()
        self.driverwait(ExpressCartLocators.loginField).send_keys('test@test.com')
        self.driverwait(ExpressCartLocators.passwordField).send_keys('test')
        self.driverwait(ExpressCartLocators.loginButton).click()

    def find(self):
        self.driverwait(ExpressCartLocators.searchField).send_keys('Whitney pullover')
        self.driverwait(ExpressCartLocators.searchButton).click()

    def open_list(self):
        self.driverwait(ExpressCartLocators.pulloverList).click()

    def add_to_cart(self):
        self.driverwait(ExpressCartLocators.pulloverList).click()
        self.driverwait(ExpressCartLocators.addToCartListButton).click()

    def open_cart(self):
        self.driverwait(ExpressCartLocators.cartButton).click()

    def checkout(self):
        self.driverwait(ExpressCartLocators.pulloverList).click()
        self.driverwait(ExpressCartLocators.addToCartListButton).click()
        self.driverwait(ExpressCartLocators.cartButton).click()
        self.driverwait(ExpressCartLocators.checkoutButton).click()

    def switch_language(self):
        self.driverwait(ExpressCartLocators.languageDropdown).click()
        self.driverwait(ExpressCartLocators.italiaonoLanguage).click()

    def add_review(self):
        self.driverwait(ExpressCartLocators.profileButton).click()
        self.driverwait(ExpressCartLocators.loginField).send_keys('test@test.com')
        self.driverwait(ExpressCartLocators.passwordField).send_keys('test')
        self.driverwait(ExpressCartLocators.loginButton).click()
        self.go_to_site()
        self.driverwait(ExpressCartLocators.pulloverList).click()
        self.driverwait(ExpressCartLocators.addReviewButton).click()

    def test_nav_bar(self):
        self.driverwait(ExpressCartLocators.bootsNavBar).click()
        self.driverwait(ExpressCartLocators.backpacksNavBar).click()
        self.driverwait(ExpressCartLocators.homeNavBar).click()

    def test_profile(self):
        self.driverwait(ExpressCartLocators.profileDropdown).click()
        self.driverwait(ExpressCartLocators.accountButton).click()
