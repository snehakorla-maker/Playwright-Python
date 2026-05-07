import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login_page import LoginPage
from pages.orangehrm_home_page import HomePage


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login("Admin", "admin123")
    expect(home_page.is_upgrade_button_visible()).to_be_true()
    home_page.click_performance()
    home_page.click_dashboard()