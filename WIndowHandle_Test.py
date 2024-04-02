"""
 Test case file with all required test cases to execute
"""

from WIndowHandle_Functions import WindowHandleClass
import pytest



url = "https://www.cowin.gov.in/"
#Creating Instance of WindowHandleClass to utilise its methods / functions
window = WindowHandleClass(url)

# Test case to navigate to URL

def test_navigate_url():
   testing_url = "https://www.cowin.gov.in/"
   assert window.fetch_url() == testing_url
print("Landed on login page")

# Test case to open FAQS page in new window
def test_open_FAQ_in_new_window():
   window.open_FAQ_in_new_window()

# Test case to open Partners page in new window
def test_open_partners_in_new_window():
   window.open_partners_in_new_window()

# Test case to display window / Frame ID individually and also collectively
def test_display_window_handles():
   window.display_window_handles()

#Test case to close FAQ and Partners Windows and return to main window(Cowin) and displays homepage title
def test_close_window_handles():
   window.close_window_handles()

#Test case to quit / shutdown browser
def test_shutdown():
   window.shutdown()
