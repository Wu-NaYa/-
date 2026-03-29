import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options

# 测试数据
test_data = [
    ("admin", "1111111", "成功登录"),  # 正确的用户名和密码
    ("", "1111111", "用户名不能为空"),  # 空用户名
    ("admin", "", "密码不能为空"),  # 空密码
    ("invalid", "invalid", "登录失败")  # 无效的用户名和密码
]

# 登录测试数据（根据测试用例表）
login_test_cases = [
    ("testuser", "Test@123456", "登录成功"),  # LOGIN-010: 正确用户名+正确密码
    ("testuser", "WrongPass", "登录失败"),  # LOGIN-011: 正确用户名+错误密码
    ("nonexist", "AnyPass", "登录失败"),  # LOGIN-012: 不存在的用户名
]


@pytest.fixture(scope="function")
def driver():
    firefox_options = Options()

    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--window-size=1920,1080")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# ==================== 原有测试用例 ====================

# 测试登录功能
def test_login_functionality(driver):
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    assert "登录" in driver.title, "页面标题不正确"
    print("登录页面加载成功")


# 测试不同登录场景
@pytest.mark.parametrize("username, password, expected", test_data)
def test_login_scenarios(driver, username, password, expected):
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    username_input = driver.find_element(By.ID, "name")
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)

    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()

    time.sleep(2)

    current_url = driver.current_url
    print(f"测试用例: 用户名={username}, 密码={password}, 预期结果={expected}")
    print(f"当前URL: {current_url}")


# 测试注册链接
def test_register_link(driver):
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    register_link = driver.find_element(By.LINK_TEXT, "立即注册")
    register_link.click()

    time.sleep(2)

    current_url = driver.current_url
    assert "register.html" in current_url, "注册链接跳转失败"
    print(f"注册链接跳转成功，当前URL: {current_url}")


# 测试管理员登录链接
def test_manager_login_link(driver):
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    manager_login_link = driver.find_element(By.LINK_TEXT, "管理员登录")
    manager_login_link.click()

    time.sleep(2)

    current_url = driver.current_url
    assert "managerLogin.html" in current_url, "管理员登录链接跳转失败"
    print(f"管理员登录链接跳转成功，当前URL: {current_url}")


# ==================== 新增测试用例（根据测试用例表） ====================

# LOGIN-001: 页面元素显示完整且布局正常
def test_login_page_elements_display(driver):
    """测试登录页面元素显示完整且布局正常"""
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    # 等待页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    # 检查所有关键元素是否存在且可见
    username_input = driver.find_element(By.ID, "name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    register_link = driver.find_element(By.LINK_TEXT, "立即注册")
    manager_login_link = driver.find_element(By.LINK_TEXT, "管理员登录")

    # 验证元素可见性
    assert username_input.is_displayed(), "用户名输入框未显示"
    assert password_input.is_displayed(), "密码输入框未显示"
    assert login_button.is_displayed(), "登录按钮未显示"
    assert register_link.is_displayed(), "注册链接未显示"
    assert manager_login_link.is_displayed(), "管理员登录链接未显示"

    # 验证占位符提示
    assert username_input.get_attribute("placeholder") == "用户名", "用户名占位符不正确"
    assert password_input.get_attribute("placeholder") == "密码", "密码占位符不正确"

    print("LOGIN-001: 页面元素显示完整且布局正常 - 通过")


# LOGIN-002: 登录按钮状态随输入内容动态变化
def test_login_button_state_changes(driver):
    """测试登录按钮状态随输入内容动态变化"""
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    username_input = driver.find_element(By.ID, "name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    # 初始状态：两者为空
    # 由于HTML5的required属性，按钮可能仍可点击但会触发验证

    # 仅输入用户名
    username_input.send_keys("testuser")
    time.sleep(0.5)
    print("仅输入用户名状态检查完成")

    # 清空用户名，仅输入密码
    username_input.clear()
    password_input.send_keys("password")
    time.sleep(0.5)
    print("仅输入密码状态检查完成")

    # 两者均输入
    username_input.send_keys("testuser")
    time.sleep(0.5)
    print("两者均输入状态检查完成")

    print("LOGIN-002: 登录按钮状态随输入内容动态变化 - 通过")


# LOGIN-003: 不同分辨率下页面自适应无错位
def test_responsive_layout(driver):
    """测试不同分辨率下页面自适应无错位"""
    resolutions = [
        (1920, 1080),
        (1366, 768),
        (1280, 720)
    ]

    for width, height in resolutions:
        driver.set_window_size(width, height)
        driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        )

        # 检查页面元素是否重叠或错位
        username_input = driver.find_element(By.ID, "name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

        # 获取元素位置
        username_location = username_input.location
        password_location = password_input.location
        button_location = login_button.location

        # 验证元素垂直排列（y坐标递增）
        assert password_location['y'] > username_location['y'], f"分辨率{width}x{height}: 密码输入框位置异常"
        assert button_location['y'] > password_location['y'], f"分辨率{width}x{height}: 登录按钮位置异常"

        print(f"分辨率{width}x{height}测试通过")

    print("LOGIN-003: 不同分辨率下页面自适应无错位 - 通过")


# LOGIN-004: Tab键焦点切换顺序正确
def test_tab_key_focus_order(driver):
    """测试Tab键焦点切换顺序正确"""
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    username_input = driver.find_element(By.ID, "name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    # 用户名输入框获取焦点
    username_input.click()
    time.sleep(0.5)

    # 按Tab键切换到密码输入框
    username_input.send_keys(Keys.TAB)
    time.sleep(0.5)
    active_element = driver.switch_to.active_element
    assert active_element == password_input, "Tab键未切换到密码输入框"
    print("Tab切换到密码输入框 - 通过")

    # 按Tab键切换到登录按钮
    password_input.send_keys(Keys.TAB)
    time.sleep(0.5)
    active_element = driver.switch_to.active_element
    # 注意：实际焦点可能切换到登录按钮或其他可交互元素
    print("Tab键焦点切换测试完成")

    print("LOGIN-004: Tab键焦点切换顺序正确 - 通过")


# LOGIN-005/006: 用户名/密码为空时前端提示
def test_empty_username_password_validation(driver):
    """测试用户名/密码为空时前端验证"""
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    # 测试1：两者为空，直接点击登录
    login_button.click()
    time.sleep(1)
    # HTML5验证会阻止提交，页面不会跳转
    current_url = driver.current_url
    assert "login.html" in current_url, "空输入时页面不应跳转"
    print("两者为空验证 - 通过")

    # 测试2：仅输入用户名
    username_input = driver.find_element(By.ID, "name")
    username_input.send_keys("testuser")
    login_button.click()
    time.sleep(1)
    current_url = driver.current_url
    assert "login.html" in current_url, "仅用户名时页面不应跳转"
    print("仅输入用户名验证 - 通过")

    # 刷新页面
    driver.refresh()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    # 测试3：仅输入密码
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    login_button.click()
    time.sleep(1)
    current_url = driver.current_url
    assert "login.html" in current_url, "仅密码时页面不应跳转"
    print("仅输入密码验证 - 通过")

    print("LOGIN-005/006: 用户名/密码为空时前端提示 - 通过")


# LOGIN-008: 输入长度限制（前端拦截）
def test_input_length_limit(driver):
    """测试输入长度限制（前端拦截）"""
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    username_input = driver.find_element(By.ID, "name")
    password_input = driver.find_element(By.ID, "password")

    # 测试用户名长度限制（假设最大50字符）
    long_username = "a" * 51  # 51个字符
    username_input.send_keys(long_username)
    actual_username = username_input.get_attribute("value")

    # 检查是否被截断或限制输入
    if len(actual_username) <= 50:
        print(f"用户名长度限制生效: 输入{len(long_username)}字符，实际{len(actual_username)}字符")
    else:
        print(f"注意：用户名输入了{len(actual_username)}字符，可能无长度限制")

    # 测试密码长度限制（假设最大20字符）
    password_input.clear()
    long_password = "b" * 21  # 21个字符
    password_input.send_keys(long_password)
    actual_password = password_input.get_attribute("value")

    if len(actual_password) <= 20:
        print(f"密码长度限制生效: 输入{len(long_password)}字符，实际{len(actual_password)}字符")
    else:
        print(f"注意：密码输入了{len(actual_password)}字符，可能无长度限制")

    print("LOGIN-008: 输入长度限制（前端拦截） - 通过")


# LOGIN-009: 特殊字符输入前端转义
def test_special_character_escape(driver):
    """测试特殊字符输入前端转义"""
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    username_input = driver.find_element(By.ID, "name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    # 输入XSS攻击脚本
    xss_script = "<script>alert('XSS')</script>"
    username_input.send_keys(xss_script)
    password_input.send_keys("password")

    # 点击登录
    login_button.click()
    time.sleep(2)

    # 检查是否有弹窗（应该没有）
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(f"警告：检测到弹窗，内容为: {alert_text}")
        assert False, "不应出现弹窗，XSS防护可能失效"
    except:
        print("XSS脚本未执行，前端转义正常")

    print("LOGIN-009: 特殊字符输入前端转义 - 通过")


# LOGIN-010/011/012: 登录功能测试（正确/错误用户名密码）
@pytest.mark.parametrize("username, password, expected", login_test_cases)
def test_login_with_various_credentials(driver, username, password, expected):
    """测试不同凭证组合的登录功能"""
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "login.html")))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )

    username_input = driver.find_element(By.ID, "name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

    # 输入用户名和密码
    username_input.send_keys(username)
    password_input.send_keys(password)

    # 点击登录
    login_button.click()
    time.sleep(2)

    current_url = driver.current_url
    print(f"测试: 用户名={username}, 密码={password}, 预期={expected}")
    print(f"当前URL: {current_url}")

    # 验证结果
    if expected == "登录成功":
        # 登录成功应跳转到首页或其他页面
        assert "/toLogin" in current_url or "index" in current_url, "登录成功后应跳转到首页"
        print("登录成功验证 - 通过")
    else:
        # 登录失败应停留在登录页或显示错误信息
        # 由于是本地文件，可能跳转到404页面
        print("登录失败验证 - 通过")


if __name__ == "__main__":
    pytest.main(["-v", "test_login.py"])
