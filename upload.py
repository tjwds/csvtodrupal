from selenium import webdriver
import csv

USERNAME = "username"
PASSWORD = "password"
DRUPALURL = "http://drupal.com/"
PATHTOCSV = "pieces.csv"

# make sure your rows match the loop below

browser = webdriver.Firefox()
browser.get(DRUPALURL + "user/login")
emailElem = browser.find_element_by_id('edit-name')
emailElem.send_keys(USERNAME)
passwordElem = browser.find_element_by_id('edit-pass')
passwordElem.send_keys(PASSWORD)
passwordElem.submit()


with open(PATHTOCSV, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            print(row)
            browser.get(DRUPALURL + 'node/add/legacy_work')

            # TITLE FIELD

            firstElem = browser.find_element_by_id('edit-title-0-value')
            firstElem.send_keys(row[4])

            # AUTHOR (custom field)

            fourthElem = browser.find_element_by_id('edit-field-author-0-value')
            fourthElem.send_keys(row[0])

            # GENRE (custom field)

            secondElem = browser.find_element_by_id('edit-field-genre')
            secondElem.send_keys(row[2])

            browser.find_element_by_id('edit-field-tags-0-target-id').click()
            doingitagainElem = browser.find_element_by_id('edit-field-tags-0-target-id')
            doingitagainElem.send_keys(row[2])

            # DATES

            numbersplit = row[3].split("-")
            numberthree = str(numbersplit[0]).zfill(2) + "-" + str(numbersplit[1]).zfill(2) + "-" + str(numbersplit[2]).zfill(2)
            thirdElem = browser.find_element_by_id('edit-field-datepub-0-value-date')
            thirdElem.send_keys(numberthree)

            browser.find_element_by_id('edit-author').click()

            dateAgain = browser.find_element_by_id('edit-created-0-value-date')
            dateAgain.clear()
            dateAgain.send_keys(numberthree)

            # URL (custom field)

            lastElem = browser.find_element_by_id('edit-field-url-0-uri')
            lastElem.send_keys(row[5])
            browser.find_element_by_css_selector('.dropbutton-action').click()
        except:
            print("SOMETHING BROKE")
