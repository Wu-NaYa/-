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
@pytest.fixture(scope="function")
def driver():
    """初始化浏览器"""
    # 创建Edge浏览器选项
    from selenium.webdriver.edge.options import Options
    edge_options = Options()
    # 添加必要的参数以避免崩溃（Jenkins环境）
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--remote-debugging-port=9222")
    edge_options.add_argument("--headless")  # 无头模式，适合CI环境
    edge_options.add_argument("--disable-gpu")  # 禁用GPU加速
    edge_options.add_argument("--window-size=1920,1080")  # 设置窗口大小
    edge_options.add_argument("--disable-extensions")  # 禁用扩展
    edge_options.add_argument("--disable-popup-blocking")  # 禁用弹窗阻止
    edge_options.add_argument("--disable-infobars")  # 禁用信息栏
    edge_options.add_argument("--start-maximized")  # 启动时最大化
    edge_options.add_argument("--disable-background-timer-throttling")  # 禁用后台定时器节流
    edge_options.add_argument("--disable-backgrounding-occluded-windows")  # 禁用后台 occlusion 窗口
    edge_options.add_argument("--disable-renderer-backgrounding")  # 禁用渲染器后台
    edge_options.add_argument("--disable-features=VizDisplayCompositor")  # 禁用 Viz 显示合成器
    
    # 尝试使用不同的Edge驱动程序路径（根据Jenkins环境调整）
    try:
        # 方法1：使用默认路径
        driver = webdriver.Edge(options=edge_options)
    except Exception as e:
        print(f"默认路径失败: {e}")
        # 方法2：指定Edge驱动程序路径（根据实际情况调整）
        from selenium.webdriver.edge.service import Service
        import os
        # 尝试常见的Edge驱动程序路径
        possible_paths = [
            "C:\\WebDrivers\\msedgedriver.exe",
            "D:\\WebDrivers\\msedgedriver.exe",
            os.path.join(os.path.dirname(__file__), "msedgedriver.exe")
        ]
        
        driver = None
        for path in possible_paths:
            if os.path.exists(path):
                try:
                    service = Service(executable_path=path)
                    driver = webdriver.Edge(service=service, options=edge_options)
                    print(f"使用Edge驱动程序路径: {path}")
                    break
                except Exception as e:
                    print(f"路径 {path} 失败: {e}")
        
        # 如果所有路径都失败，尝试使用Selenium的自动驱动管理
        if driver is None:
            print("尝试使用Selenium的自动驱动管理")
            driver = webdriver.Edge(options=edge_options)
    
    # 设置隐式等待时间为10秒
    driver.implicitly_wait(10)
    yield driver
    # 测试结束后关闭浏览器
    driver.quit()


# 测试登录页面加载
@pytest.mark.parametrize("username, password, expected", test_data)
def test_login(driver, username, password, expected):
    """测试登录功能"""
    # 打开登录页面（使用相对路径）
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "src/main/webapp/login.html")))

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
    # 这里需要根据实际情况进行调整，例如检查URL变化或错误提示
    # 由于是本地HTML文件，表单提交后可能会跳转到404页面，这里仅做示例
    current_url = driver.current_url
    print(f"当前URL: {current_url}")
    print(f"测试用例: 用户名={username}, 密码={password}, 预期结果={expected}")


# 测试注册链接

def test_register_link(driver):
    """测试注册链接"""
    # 打开登录页面（使用相对路径）
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "src/main/webapp/login.html")))

    # 点击注册链接
    register_link = driver.find_element(By.LINK_TEXT, "立即注册")
    register_link.click()

    # 验证页面跳转
    time.sleep(2)
    current_url = driver.current_url
    assert "register.html" in current_url, "注册链接跳转失败"
    print(f"注册链接跳转成功，当前URL: {current_url}")


# 测试管理员登录链接
def test_manager_login_link(driver):
    """测试管理员登录链接"""
    # 打开登录页面（使用相对路径）
    driver.get("file:///" + os.path.abspath(os.path.join(os.path.dirname(__file__), "src/main/webapp/login.html")))

    # 点击管理员登录链接
    manager_login_link = driver.find_element(By.LINK_TEXT, "管理员登录")
    manager_login_link.click()

    # 验证页面跳转
    time.sleep(2)
    current_url = driver.current_url
    assert "managerLogin.html" in current_url, "管理员登录链接跳转失败"
    print(f"管理员登录链接跳转成功，当前URL: {current_url}")


if __name__ == "__main__":
    pytest.main(["-v", "test_login.py"])
