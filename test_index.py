# 青少年群体眼部疾病分析页面测试脚本
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局变量
BASE_URL = os.path.abspath('index.html')

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
    assert "疾病科普疾病分析" in driver.title
    # 验证页面主标题
    main_title = driver.find_element(By.CLASS_NAME, "tith1")
    assert "青少年群体眼部疾病分析" in main_title.text

# 测试导航链接
def test_navigation_links(driver):
    """测试导航链接功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试疾病分析链接（当前页面）
    disease_analysis_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病分析')]")
    assert disease_analysis_link.is_displayed()
    
    # 测试疾病预防链接
    disease_prevention_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病预防')]")
    assert disease_prevention_link.is_displayed()
    
    # 测试返回首页链接
    home_link = driver.find_element(By.XPATH, "//a[contains(text(), '返回首页')]")
    assert home_link.is_displayed()

# 测试页面图表元素
def test_chart_elements(driver):
    """测试页面图表元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试词云图元素
    wordcloud_element = driver.find_element(By.ID, "topmap")
    assert wordcloud_element.is_displayed()
    
    # 测试眼科用药类型占比图表
    medicine_chart = driver.find_element(By.ID, "amiddboxtbott3")
    assert medicine_chart.is_displayed()
    
    # 测试全国学生近视变化率图表
    myopia_rate_chart = driver.find_element(By.ID, "amiddboxtbott2")
    assert myopia_rate_chart.is_displayed()
    
    # 测试眼部疾病对比分析图
    comparison_chart = driver.find_element(By.ID, "pumiddboxtbott1")
    assert comparison_chart.is_displayed()
    
    # 测试2018-2020年中国近视眼手术有效病例数图表
    surgery_chart = driver.find_element(By.ID, "lefttoday_number")
    assert surgery_chart.is_displayed()
    
    # 测试2014-2020年中国眼科医院数量走势图表
    hospital_chart = driver.find_element(By.ID, "purightboxmidd")
    assert hospital_chart.is_displayed()
    
    # 测试近视程度图表
    myopia_degree_chart = driver.find_element(By.ID, "purightboxbott")
    assert myopia_degree_chart.is_displayed()

# 测试页面布局和响应式设计
def test_page_layout(driver):
    """测试页面布局和响应式设计"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试左侧内容区域
    left_content = driver.find_element(By.CLASS_NAME, "puleft")
    assert left_content.is_displayed()
    
    # 测试中间内容区域
    middle_content = driver.find_element(By.CLASS_NAME, "puleft2")
    assert middle_content.is_displayed()
    
    # 测试右侧内容区域
    right_content = driver.find_element(By.CLASS_NAME, "mr_right")
    assert right_content.is_displayed()

# 测试浏览器兼容性
def test_browser_compatibility(driver):
    """测试浏览器兼容性"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试页面是否能在不同窗口大小下正常显示
    driver.set_window_size(1366, 768)
    assert driver.title
    
    driver.set_window_size(1920, 1080)
    assert driver.title
