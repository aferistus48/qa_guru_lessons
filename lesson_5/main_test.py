from time import sleep

from selene import browser, command
import os


browser.config.driver_name = 'chrome'
browser.config.base_url = 'https://demoqa.com'


def test_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('first')
    browser.element('#lastName').type('last')

    browser.element('#userEmail').type('name@example.com')

    browser.element('#gender-radio-1').perform(command.js.click)

    browser.element('#userNumber').type('8909909909')

    browser.element('#dateOfBirthInput').press_enter()

    browser.element('#subjectsInput').type('che').press_enter()

    browser.element('#hobbies-checkbox-3').perform(command.js.click)

    browser.element('#currentAddress').type('Current Address')

    browser.element('.form-file').click().element('#uploadPicture').send_keys(os.path.abspath('requirements.txt'))

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()

    browser.element('#submit').click()
