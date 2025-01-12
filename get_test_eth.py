import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_test_eth(wallet_address):
    # 设置 Chrome 浏览器选项
    options = Options()
    options.add_argument("--headless")  # 无头模式，不显示浏览器界面
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")  # 对于 Docker 环境更稳定

    # 使用 ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # 打开测试网站
        driver.get("https://cloud.google.com/application/web3/faucet/ethereum/sepolia")
        print("Opened faucet page.")
        time.sleep(2)  # 等待页面加载

        # 找到钱包地址输入框并输入地址
        address_input = driver.find_element(By.XPATH, '//input[@placeholder="Enter Wallet Address"]')
        address_input.clear()
        address_input.send_keys(wallet_address)

        # 找到并点击领取按钮
        claim_button = driver.find_element(By.XPATH, '//button[contains(text(), "Get free ETH")]')
        claim_button.click()
        print("Clicked the claim button.")

        time.sleep(5)  # 等待一段时间，确保领取过程完成
        print(f"Successfully requested ETH for address: {wallet_address}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    # 从环境变量中获取钱包地址
    wallet_address = os.getenv("WALLET_ADDRESS", "0xxxx")  # 默认为您的钱包地址
    print(f"Using wallet address: {wallet_address}")
    get_test_eth(wallet_address)
