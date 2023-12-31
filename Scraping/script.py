from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

clean_file_path = './clean/clean_data.txt'
file_path = './data/data.txt'

def get_text_from_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    return element.text

def accepting():
    driver = webdriver.Chrome()
    driver.get("https://bourse.societegenerale.fr/services/newsletters/bourse-matin")

    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Tout sélectionner'])[1]"))
        )
        button.click()

        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='editorial-3302']//p//iframe"))
        )
        driver.switch_to.frame(iframe)

        clot_wall_st = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='grid_div r3d_l r2d_l']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", clot_wall_st)
        lire_la_suite = clot_wall_st.find_element(By.XPATH, "//a[@class='bouton_suite']")
        lire_la_suite.click()

        text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='zText']"))
        )
        text = get_text_from_element(driver, text_element)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        driver.quit()

def remove_first_n_lines(file_path, clean_file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines = lines[n:]

    with open(clean_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

accepting()
remove_first_n_lines(file_path, clean_file_path, 7)
