from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

ACCOUNT_EMAIL="mohan@test.com"
ACCOUNT_PASSWORD="password123"
GYM_URL="https://appbrewery.github.io/gym/"

def display_summary(c_booked, wl_joined, alr_booked_waitlisted, total_processed):
    print("--- BOOKING SUMMARY ---")
    print(f"Classes booked: {c_booked}")
    print(f"Waitlists joined: {wl_joined}")
    print(f"Already booked/waitlisted: {alr_booked_waitlisted}")
    print(f"Total Tuesday/Thursday 6pm classes: {total_processed}")

def display_detailed_class_list(detailed_list):
    print("--- DETAILED CLASS LIST ---")
    if detailed_list:
        for entry in detailed_list:
            print(f"  •{entry}")
    else:
        print("  •Nothing to show...")

def display_booking_verification(bookings, waitlists, expected_reservations):
    total_bookings = len(bookings)+len(waitlists)

    print("---VERIFYING ON MY BOOKINGS PAGE---")
    for booking in bookings:
        print(f"✓ Verified: {booking.text}")
    for waitlist in waitlists:
        print(f"✓ Verified: {waitlist.text}")

    print("---VERIFICATION RESULT---")
    print(f"Expected: {expected_reservations} bookings")
    print(f"Found: {total_bookings} bookings")
    if expected_reservations == total_bookings:
        print("✅ SUCCESS: All bookings verified!")
    else:
        print(f"❌ MISMATCH: Missing {expected_reservations-total_bookings} bookings")

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt {i+1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    wait.until(EC.visibility_of_element_located((By.ID, "email-input")))
    print("Login page has loaded")

    email_input = driver.find_element(By.ID, "email-input")
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    driver.find_element(By.ID, "submit-button").click()

    wait.until(EC.visibility_of_element_located((By.ID, "schedule-page")))
    print("User has logged in")

def book_class(booking_button, class_status):
    booking_button.click()
    if class_status == "book":
        wait.until(lambda d: booking_button.text == "Booked")
    if class_status == "waitlist":
        wait.until(lambda d: booking_button.text == "Waitlisted")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/gym/")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
wait = WebDriverWait(driver, timeout=2, poll_frequency=.2)

retry(login, description="login")

classes_booked = 0
waitlists_joined = 0
already_booked_or_waitlisted = 0
tuesday_6pm_classes_processed = 0
total_bookings = 0
detailed_class_list = []

#Looks for bookings on tuesday or thursday at 6pm and books them or joins the waitlist
daily_plan = driver.find_elements(By.CSS_SELECTOR, "div[id^=day-group-]")
for plan in daily_plan:
    plan_day=plan.find_element(By.CSS_SELECTOR, "h2").text
    if 'Tue' in plan_day or 'Thu' in plan_day:
        class_cards=plan.find_elements(By.CSS_SELECTOR, "div[id^=class-card-]")
        for card in class_cards:
            card_id = card.get_attribute("id")
            if "1800" in card_id:
                class_type = card.find_element(By.CSS_SELECTOR, "h3[id^=class-name-").text
                button = card.find_element(By.CSS_SELECTOR, "button")
                if button.text == "Book Class":
                    classes_booked += 1
                    tuesday_6pm_classes_processed+=1
                    total_bookings+=1
                    retry(lambda: book_class(button, "book"), description="Booking")
                    print(f"✓ Booked: 6pm {class_type}, {plan_day}")
                    detailed_class_list.append(f"[New Booking] {class_type} on {plan_day}")
                elif button.text == "Join Waitlist":
                    waitlists_joined +=1
                    tuesday_6pm_classes_processed+=1
                    total_bookings+=1
                    retry(lambda: book_class(button, "waitlist"), description="Waitlisting")
                    print(f"✓ Joined Waitlist: 6pm {class_type}, {plan_day}")
                    detailed_class_list.append(f"[New Waitlist] {class_type} on {plan_day}")
                elif button.text == "Waitlisted":
                    already_booked_or_waitlisted +=1
                    total_bookings+=1
                    print(f"✓ Already on waitlist: 6pm {class_type}, {plan_day}")
                elif button.text == "Booked":
                    already_booked_or_waitlisted +=1
                    total_bookings+=1
                    print(f"✓ Already booked: 6pm {class_type}, {plan_day}")

display_summary(classes_booked, waitlists_joined, already_booked_or_waitlisted, tuesday_6pm_classes_processed)
display_detailed_class_list(detailed_class_list)

driver.find_element(By.ID, "my-bookings-link").click()
wait.until(EC.visibility_of_element_located((By.ID, "my-bookings-page")))

try:
    confirmed_bookings = driver.find_elements(By.CSS_SELECTOR, "h3[id^=booking-class-name-booking_]")
    confirmed_waitlists = driver.find_elements(By.CSS_SELECTOR, "h3[id^=waitlist-class-name-waitlist]")
except NoSuchElementException:
    print("Couldn't find bookings!")
else:
    display_booking_verification(bookings=confirmed_bookings, waitlists=confirmed_waitlists,
                                 expected_reservations=total_bookings)
