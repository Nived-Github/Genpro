from time import sleep
from selenium import webdriver
driver = webdriver.Chrome(executable_path="../chromedriver.exe")
driver.get("https://www.saucedemo.com/")
sleep(2)
username_field = driver.find_element("id", "user-name")
username_field.send_keys("secret_sauce")
password_field = driver.find_element("id", "password")
password_field.send_keys("secret_sauce")
password_field.submit()

# price <$15
driver.find_element("class", "shopping_cart_link").click()
# TODO: Implement removal of items with price <$15

# Click on the Checkout button
driver.find_element(By.ID, "checkout").click()

# Enter details on the information page and click Continue
first_name_field = driver.find_element(By.ID, "first-name")
first_name_field.send_keys("user")
last_name_field = driver.find_element(By.ID, "last-name")
last_name_field.send_keys("A")
zip_code_field = driver.find_element(By.ID, "postal-code")
zip_code_field.send_keys("12345")
zip_code_field.submit()

# Finish the checkout by clicking the Finish button
driver.find_element(By.ID, "finish").click()

# Return to the home page
driver.find_element(By.ID, "back-to-products").click()

# Perform logout
driver.find_element(By.ID, "logout_sidebar_link").click()

# Close the browser
driver.quit()
