import time
import schedule
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

def job():
    # 设置您的钱包地址
    wallet_address = "0x92CaDCd5a69Bb327a56392B76f1D55A2C3a718d7"  # 请替换为您的钱包地址
    get_test_eth(wallet_address)

# 设置定时任务为每天的 9:00 AM
schedule.every().day.at("09:00").do(job)

print("Scheduler started. Waiting for 9:00 AM...")

# 持续运行，等待任务执行
while True:
    schedule.run_pending()  # 检查是否有任务到期并执行
    time.sleep(60)  # 每 60 秒检查一次
