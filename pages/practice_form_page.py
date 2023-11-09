
import allure
from pages.base_page import BasePage
from locators.practice_form_page_locators import PracticeFormPageLocators
from generator.generator import generate_person


class PracticeFormPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def open(self, url):
        self.browser.get(url)

    def fill_in_fist_name(self, text: str):
        self.wait_and_fill_in(PracticeFormPageLocators.first_name, text)

    def fill_in_last_name(self, text: str):
        self.wait_and_fill_in(PracticeFormPageLocators.last_name, text)

    def fill_in_email(self, text: str):
        self.wait_and_fill_in(PracticeFormPageLocators.email, text)

    def select_male_radiobutton(self):
        self.wait_and_click(PracticeFormPageLocators.gender_checkbox_male)

    def fill_in_number(self, text: str):
        self.wait_and_fill_in(PracticeFormPageLocators.phone_number, text)

    def open_birth_date_window(self):
        self.wait_and_click(PracticeFormPageLocators.birth_date)

    def open_year_list(self):
        self.wait_and_click(PracticeFormPageLocators.display_list_year)

    def select_year(self):
        self.wait_and_click(PracticeFormPageLocators.select_year)

    def select_date(self):
        self.wait_and_click(PracticeFormPageLocators.select_date)

    def fill_in_subject(self, text: str):
        self.wait_and_fill_in(PracticeFormPageLocators.subject, text)

    def select_subject(self):
        self.wait_and_click(PracticeFormPageLocators.select_computer_subject)

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 500)")

    def select_sports_radiobatton(self):
        self.wait_and_click(PracticeFormPageLocators.hobbies_checkbox_sports)

    def add_picture(self, path):
        self.wait_and_fill_in(PracticeFormPageLocators.picture, path)

    def fill_in_adress(self, text: str):
        self.wait_and_fill_in(PracticeFormPageLocators.current_address, text)

    def remove_footer(self):
        self.browser.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.browser.execute_script("document.getElementById('fixedban').style.display='none'")

    def open_state_list(self):
        self.wait_and_click(PracticeFormPageLocators.state_list)

    def select_state(self):
        self.wait_and_click(PracticeFormPageLocators.state_NCR)

    def open_city_list(self):
        self.wait_and_click(PracticeFormPageLocators.city_list)

    def select_city(self):
        self.wait_and_click(PracticeFormPageLocators.city_DELHI)

    def click_submit(self):
        self.wait_and_click(PracticeFormPageLocators.btn_submit)

    #@allure.title('check email')
    def check_modal_email(self, text: str):
        email_text = self.get_text(PracticeFormPageLocators.modal_email)
        assert email_text == text


    #@allure.title('check phone number')
    def check_phone_number(self, text: str):
        phone_text = self.get_text(PracticeFormPageLocators.modal_mobile_number)
        assert phone_text == text

    @allure.title('check the male gender')
    def check_gender(self):
        gender_text = self.get_text(PracticeFormPageLocators.modal_gender_male)
        assert gender_text == "Male"

    def check_address(self, text: str):
        adress_text = self.get_text(PracticeFormPageLocators.modal_address)
        assert adress_text == text


















