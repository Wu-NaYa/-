# 订单详情页面测试脚本
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局变量
BASE_URL = os.path.abspath('personInfo.html')

@pytest.fixture(scope="function")
def driver():
    """初始化浏览器驱动"""
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

# 测试页面加载和基本元素
def test_page_load(driver):
    """测试页面是否正常加载"""
    driver.get(f"file://{BASE_URL}")
    # 验证页面标题
    assert "数据后台管理" in driver.title
    # 验证页面主标题
    page_title = driver.find_element(By.CLASS_NAME, "navbar-page-title")
    assert "订单详情" in page_title.text

# 测试导航链接
def test_navigation_links(driver):
    """测试导航链接功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试购买药物链接
    buy_medicine_link = driver.find_element(By.XPATH, "//a[contains(text(), '购买药物')]")
    assert buy_medicine_link.is_displayed()
    
    # 测试订单详情链接（当前页面）
    order_detail_link = driver.find_element(By.XPATH, "//a[contains(text(), '订单详情')]")
    assert order_detail_link.is_displayed()
    
    # 测试个人信息链接
    personal_info_link = driver.find_element(By.XPATH, "//a[contains(text(), '个人信息')]")
    assert personal_info_link.is_displayed()
    
    # 测试返回首页链接
    home_link = driver.find_element(By.XPATH, "//a[contains(text(), '返回首页')]")
    assert home_link.is_displayed()
    
    # 测试退出登录链接
    logout_link = driver.find_element(By.XPATH, "//a[contains(text(), '退出登录')]")
    assert logout_link.is_displayed()

# 测试订单表格元素
def test_order_table_elements(driver):
    """测试订单表格元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试订单信息卡片
    order_card = driver.find_element(By.CLASS_NAME, "card")
    assert order_card.is_displayed()
    
    # 测试订单信息标题
    order_title = driver.find_element(By.XPATH, "//h4[contains(text(), '订单信息')]")
    assert order_title.is_displayed()
    
    # 测试表格
    order_table = driver.find_element(By.CLASS_NAME, "table")
    assert order_table.is_displayed()
    
    # 测试表格表头
    table_headers = driver.find_elements(By.TAG_NAME, "th")
    assert len(table_headers) == 5
    assert table_headers[0].text == "#"
    assert table_headers[1].text == "用户名"
    assert table_headers[2].text == "药物名称"
    assert table_headers[3].text == "药物价格"
    assert table_headers[4].text == "操作"

# 测试主题切换功能
def test_theme_switching(driver):
    """测试主题切换功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试主题切换按钮
    theme_button = driver.find_element(By.CLASS_NAME, "icon-palette")
    assert theme_button.is_displayed()
    
    # 点击主题切换按钮
    theme_button.click()
    
    # 测试主题下拉菜单是否显示
    theme_dropdown = driver.find_element(By.CLASS_NAME, "dropdown-menu")
    assert theme_dropdown.is_displayed()

# 测试用户信息显示
def test_user_info_display(driver):
    """测试用户信息显示"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试用户名显示
    user_name = driver.find_element(By.ID, "userName")
    assert user_name.is_displayed()

# 测试取消订单按钮
def test_cancel_order_button(driver):
    """测试取消订单按钮"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试取消订单按钮是否存在
    # 注意：由于订单数据是通过AJAX加载的，实际测试中可能需要等待数据加载完成
    # 这里我们测试按钮的模板是否存在
    cancel_button_template = driver.find_element(By.XPATH, "//button[contains(text(), '取消订单')]")
    assert cancel_button_template.is_displayed()

# 测试页面布局和响应式设计
def test_page_layout(driver):
    """测试页面布局和响应式设计"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试左侧导航栏
    sidebar = driver.find_element(By.CLASS_NAME, "lyear-layout-sidebar")
    assert sidebar.is_displayed()
    
    # 测试头部信息
    header = driver.find_element(By.CLASS_NAME, "lyear-layout-header")
    assert header.is_displayed()
    
    # 测试主要内容区域
    main_content = driver.find_element(By.CLASS_NAME, "lyear-layout-content")
    assert main_content.is_displayed()

# 测试浏览器兼容性
def test_browser_compatibility(driver):
    """测试浏览器兼容性"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试页面是否能在不同窗口大小下正常显示
    driver.set_window_size(1366, 768)
    assert driver.title
    
    driver.set_window_size(1920, 1080)
    assert driver.title
