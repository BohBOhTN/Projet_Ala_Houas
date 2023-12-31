from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

clean_file_path = './clean/clean_data.txt'

def get_text_from_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    return element.text

def clean_text(text):
    cleaned_text = text.replace('\n', ' ').replace('\r', '')  # Example: Removing line breaks and carriage returns
    # You can add more cleaning operations as needed
    return cleaned_text

def remove_first_n_lines(text, n):
    lines = text.split('\n')
    cleaned_lines = lines[n:]
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text

def accepting():
    driver = webdriver.Chrome()
    driver.get("https://bourse.societegenerale.fr/services/newsletters/bourse-matin")

    try:
        # Click on the "Tout sélectionner" button
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Tout sélectionner'])[1]"))
        )
        button.click()

        # Wait for the iframe to be present and switch to it
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='editorial-3302']//p//iframe"))
        )
        driver.switch_to.frame(iframe)

        # Find and click the "Lire la suite" link
        clot_wall_st = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='grid_div r3d_l r2d_l']"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", clot_wall_st)
        lire_la_suite = clot_wall_st.find_element(By.XPATH, "//a[@class='bouton_suite']")
        lire_la_suite.click()

        # Get text from the designated element
        text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='zText']"))
        )
        text = get_text_from_element(driver, text_element)

        # Remove the first 7 lines from the text
        text = remove_first_n_lines(text, 7)

        # Clean the extracted text
        cleaned_text = clean_text(text)

        # Write the cleaned text to a file
        with open(clean_file_path, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        driver.quit()

# Run the function to extract text, clean it, and save it directly
accepting()
