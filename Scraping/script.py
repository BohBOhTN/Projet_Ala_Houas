from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://bourse.societegenerale.fr/services/newsletters/bourse-matin")
time.sleep(2)
driver.find_element(By.XPATH,"(//button[normalize-space()='Tout sélectionner'])[1]").click()
time.sleep(3)
big_container = driver.find_element(By.XPATH,"//div[@id='editorial-3302']//p//iframe")
driver.switch_to.frame(big_container)
clot_wall_st = driver.find_element(By.XPATH,"//div[@class='grid_div r3d_l r2d_l']")
clot_wall_st.find_element(By.XPATH,"//a[@class='bouton_suite']").click()
text = clot_wall_st.find_element(By.XPATH,"//div[@class='zText']").text
clean_file_path = './clean/clean_data.txt'
file_path = './data/data.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(text)
driver.quit()

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Remove the first 7 lines
lines = lines[7:]

# Write the modified content back to the file
with open(clean_file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)