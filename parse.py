from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

LINK = "http://flibusta.site/book"
PATH = "C:\\Users\\issak\\OneDrive\\Рабочий стол\\Kindle project\\chromedriver.exe"


# IDs for the forms from flibusta.site/book webpage
BookNameFormID = "t"
AuthorLastNameFormID = "ln"
AuthorFirstNameFormID = "fn"
BookGenreFormID = "g"
BookMinSizeFormID = "s1"
BookMaxSizeFormID = "s2"
BookPublishedMinFormID = "issueYearMin"
BookPublishedMaxFormID = "issueYearMax"


def RemoveAds():   # this function is responsible for removing the html elements that contain advertisements for better UX
    driver.execute_script("""
            var PopUp = document.getElementById("logo");
            PopUp.parentNode.removeChild(PopUp);
    """)


def SearchForBook():   # This function gets the user input with the book name and then sends the name + enter to the book name form in the html page of flibusta.site/book
    BookName = input("Введите название книги:  ")
    BookNameForm = driver.find_element(By.ID, BookNameFormID)
    BookNameForm.send_keys(BookName)
    BookNameForm.send_keys(Keys.RETURN)


def SelectBestBook(books):
    return books[0]


def ProcessResults():  # After we entered the book name in the form we need to process the results (but also have enough delay between the two functions)
    # try:
    #     checknum = 0
    #     while True:
    #         print("update check " + str(checknum))
    #         InitialStateLabel = driver.find_element(
    #             By.CLASS_NAME, "g-comp_db g-economics")[0]
    #         print("##" + InitialStateLabel.text)
    #         checknum += 1

    # except:
    #     print("page updated")
    ResultsDiv = driver.find_element(By.NAME, "bk")
    Books = ResultsDiv.find_elements(By.TAG_NAME, "div")
    print(ResultsDiv)
    print(ResultsDiv.text)

    print("~~~~~~~~~~~~~~~~~~")
    for book in Books:
        print(book.text)

    # for now this function will click the download button for the epub of the first offered book
    SelectedBook = SelectBestBook(Books)
    EpubDownload = SelectedBook.find_elements(By.TAG_NAME, "a")[4]
    print('Clicked on: ' + EpubDownload.text)
    print("Started downloading " + SelectedBook.text)
    EpubDownload.click()


CustomOptions = ChromeOptions()
CustomOptions.add_experimental_option("detach", True)
# CustomOptions.add_extension('adblocker.crx')
driver = webdriver.Chrome(options=CustomOptions)
driver.maximize_window()
driver.get(LINK)


SearchForBook()
sleep(10)
ProcessResults()

input("press ENTER to quit the browser")
driver.quit()
