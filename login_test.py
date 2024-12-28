from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome(executable_path='./chromedriver.exe')  # Ganti dengan path chromedriver Anda

# URL Login Page
BASE_URL = "https://app2.jubelio.com/login"
HOME_URL = "https://app2.jubelio.com/home/getting-started"
LOGIN_URL = "https://app2.jubelio.com/login"

# Test Case: Login Berhasil
def test_login_success():
    driver.get(BASE_URL)

    # Tunggu hingga elemen input email tersedia
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    # Masukkan email dan password valid
    driver.find_element(By.NAME, "email").send_keys("adindakarla123@gmail.com")  # Ganti dengan email yang valid
    driver.find_element(By.NAME, "password").send_keys("G@S6srvUMefCL55")  # Ganti dengan password yang salah
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)  # Tunggu beberapa detik agar halaman dapat dimuat

    # Verifikasi apakah login berhasil dengan memeriksa URL halaman
    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/home/getting-started"))  # Cek apakah URL mengandung '/home/getting-started'
        print("Test Login Success: PASSED")
    except:
        # Jika halaman tidak sesuai (login gagal), tampilkan URL saat ini
        print("Login gagal, URL saat ini:", driver.current_url)
        assert False, "Login gagal, halaman dashboard tidak ditemukan."

# Test Case: Login Gagal - Kolom Kosong
def test_login_empty_fields():
    driver.get(BASE_URL)

    # Tunggu hingga elemen input email tersedia
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    # Biarkan kolom email dan password kosong
    driver.find_element(By.NAME, "email").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Verifikasi apakah login gagal dengan memeriksa apakah tetap di halaman login
    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        print("Test Login Empty Fields: PASSED")
    except:
        print("Login gagal, tidak ada pesan error yang ditemukan.")
        assert False, "Login gagal, halaman login tidak ditemukan."

# Test Case: Login Gagal - Password Salah
def test_login_invalid_password():
    driver.get(BASE_URL)

    # Tunggu hingga elemen input email tersedia
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    # Masukkan email yang valid, tetapi password salah
    driver.find_element(By.NAME, "email").send_keys("adindakarla123@gmail.com")  # Ganti dengan email yang valid
    driver.find_element(By.NAME, "password").send_keys("G@S6srvUMefCL55")  # Ganti dengan password yang salah
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Verifikasi apakah login gagal dengan memeriksa apakah tetap di halaman login
    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        print("Test Login Invalid Password: PASSED")
    except:
        print("Login gagal, tidak ada pesan error yang ditemukan.")
        assert False, "Login gagal, halaman login tidak ditemukan."

# Eksekusi Semua Test
if __name__ == "__main__":
    try:
        test_login_success()
        test_login_empty_fields()
        test_login_invalid_password()
    finally:
        driver.quit()  # Pastikan browser tertutup setelah pengujian
