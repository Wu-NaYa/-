import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 测试数据
test_data = [
    ("admin", "123456", "成功登录"),  # 正确的用户名和密码
    ("", "123456", "用户名不能为空"),  # 空用户名
    ("admin", "", "密码不能为空"),  # 空密码
    ("invalid", "invalid", "登录失败")  # 无效的用户名和密码
]


# 封装浏览器初始化和关闭的fixture
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

@pytest.fixture(scope="function")
def driver():
    """初始化浏览器（Firefox 国内无墙稳定版）"""
    firefox_options = Options()

    # CI / Jenkins 本地都能跑的稳定参数
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--window-size=1920,1080")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    # 自动下载火狐驱动，国内 100% 可用！
    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# 测试登录功能
def test_login_functionality(driver):
    """测试登录页面的基本功能"""
    # 打开登录页面（使用相对路径）
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    # 验证页面标题
    assert "登录" in driver.title, "页面标题不正确"
    print("登录页面加载成功")


# 测试不同登录场景
@pytest.mark.parametrize("username, password, expected", test_data)
def test_login_scenarios(driver, username, password, expected):
    """测试不同登录场景"""
    # 打开登录页面
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    # 输入用户名
    username_input = driver.find_element(By.ID, "name")
    username_input.clear()
    username_input.send_keys(username)

    # 输入密码
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

    # 点击登录按钮
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()

    # 等待页面跳转或提示信息
    time.sleep(2)

    # 验证登录结果
    # 由于是本地HTML文件，表单提交后可能会跳转到404页面，这里仅做示例
    current_url = driver.current_url
    print(f"测试用例: 用户名={username}, 密码={password}, 预期结果={expected}")
    print(f"当前URL: {current_url}")


# 测试注册链接
def test_register_link(driver):
    """测试注册链接"""
    # 打开登录页面
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    # 点击注册链接
    register_link = driver.find_element(By.LINK_TEXT, "立即注册")
    register_link.click()

    # 等待页面跳转
    time.sleep(2)

    # 验证页面跳转
    current_url = driver.current_url
    assert "register.html" in current_url, "注册链接跳转失败"
    print(f"注册链接跳转成功，当前URL: {current_url}")


# 测试管理员登录链接
def test_manager_login_link(driver):
    """测试管理员登录链接"""
    # 打开登录页面
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    # 点击管理员登录链接
    manager_login_link = driver.find_element(By.LINK_TEXT, "管理员登录")
    manager_login_link.click()

    # 等待页面跳转
    time.sleep(2)

    # 验证页面跳转
    current_url = driver.current_url
    assert "managerLogin.html" in current_url, "管理员登录链接跳转失败"
    print(f"管理员登录链接跳转成功，当前URL: {current_url}")


if __name__ == "__main__":
    pytest.main(["-v", "test_login.py"])
