import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 目標網址
url = "https://hike.taiwan.gov.tw/bed_6main.aspx?orgid=C951CDCD-B75A-46B9-8002-8EF952EC95FD&node_id=3&sdate=2025-09-15"

# 設定 Chrome 無頭模式（不開啟視窗）
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

def check_and_save():
    # 啟動 WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        driver.get(url)
        time.sleep(3)  # 等待 JS 載入

        # 找出所有表格列
        rows = driver.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            row_text = row.text.strip()
            if "榕" in row_text and "2025的心願" in row_text:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                output = f"[{timestamp}] {row_text}"
                print(output)

                # 存到文字檔
                with open("result.txt", "a", encoding="utf-8") as f:
                    f.write(output + "\n")

    finally:
        driver.quit()

if __name__ == "__main__":
    while True:
        check_and_save()
        print("等待 60 秒後再次檢查...\n")
        time.sleep(60)
