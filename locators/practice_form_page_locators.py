from selenium.webdriver.common.by import By


class PracticeFormPageLocators:
    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    gender_checkbox_male = (By.XPATH, '//*[contains(text(), "Male")]')
    phone_number = (By.ID, "userNumber")
    birth_date = (By.ID, 'dateOfBirthInput')
    display_list_year = (By.XPATH, "//select[@class='react-datepicker__year-select']")
    select_year = (By.XPATH, "//option[@value='1995']")
    select_date =(By.XPATH, "//*[text() = '18']")
    subject = (By.XPATH, "//*[@id='subjectsInput']")
    select_computer_subject = (By.XPATH, '//*[contains(text(), "Computer")]')
    hobbies_checkbox_sports = (By.XPATH, '//*[contains(text(), "Sports")]')
    picture = (By.ID, 'uploadPicture')
    current_address = (By.ID, 'currentAddress')
    state_list = (By.XPATH, '//*[contains(text(), "Select State")]')
    state_NCR = (By.XPATH, '//*[contains(text(), "NCR")]')
    city_list = (By.XPATH, '//*[contains(text(), "Select City")]')
    city_DELHI = (By.XPATH, '//*[contains(text(), "Delhi")]')
    btn_submit = (By.ID, 'submit')
    modal_email = (By.XPATH, '(//*[contains(text(), "Student Email")]/../td)[2]')
    modal_mobile_number = (By.XPATH, '(//*[contains(text(), "Mobile")]/../td)[2]')
    modal_address = (By.XPATH, '(//*[contains(text(), "Address")]/../td)[2]')
    modal_gender_male = (By.XPATH, '(//*[contains(text(), "Gender")]/../td)[2]')