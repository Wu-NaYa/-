# 老年人群体疾病科普页面测试脚本
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局变量
BASE_URL = os.path.abspath('kepu1.html')

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
    assert "疾病科普" in driver.title
    # 验证页面主标题
    main_title = driver.find_element(By.CLASS_NAME, "tith1")
    assert "老年人群体疾病科普" in main_title.text

# 测试导航链接
def test_navigation_links(driver):
    """测试导航链接功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试疾病科普链接（当前页面）
    disease_edu_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病科普')]")
    assert disease_edu_link.is_displayed()
    
    # 测试疾病分析链接
    disease_analysis_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病分析')]")
    assert disease_analysis_link.is_displayed()
    
    # 测试返回首页链接
    home_link = driver.find_element(By.XPATH, "//a[contains(text(), '返回首页')]")
    assert home_link.is_displayed()
    
    # 测试疾病预测链接
    disease_prediction_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病预测')]")
    assert disease_prediction_link.is_displayed()

# 测试视频元素
def test_video_element(driver):
    """测试视频元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试高血压疾病科普视频
    video_element = driver.find_element(By.TAG_NAME, "video")
    assert video_element.is_displayed()
    
    # 测试视频源
    video_source = driver.find_element(By.TAG_NAME, "source")
    assert video_source.get_attribute("src") == "img/video2/gaoxueya.mp4"

# 测试页面图表元素
def test_chart_elements(driver):
    """测试页面图表元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试降血脂药市场份额图表
    lipid_chart = driver.find_element(By.ID, "chart_5")
    assert lipid_chart.is_displayed()
    
    # 测试调脂药与心血管系统用药销售数量对比图表
    sales_chart = driver.find_element(By.ID, "amiddboxtbott2")
    assert sales_chart.is_displayed()

# 测试心血管疾病简介
def test_cardiovascular_intro(driver):
    """测试心血管疾病简介"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试心血管疾病简介标题
    intro_title = driver.find_element(By.XPATH, "//h2[contains(text(), '心血管疾病简介')]")
    assert intro_title.is_displayed()
    
    # 测试心血管疾病简介内容
    intro_content = driver.find_element(By.XPATH, "//p[contains(text(), '心脑血管疾病是心脏血管和脑血管疾病的统称')]")
    assert intro_content.is_displayed()
    
    # 测试探索按钮
    explore_button = driver.find_element(By.XPATH, "//button[contains(text(), '快和我一起探索吧!')]")
    assert explore_button.is_displayed()

# 测试常见老年疾病内容
def test_common_elderly_diseases(driver):
    """测试常见老年疾病内容"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试常见老年疾病标题
    diseases_title = driver.find_element(By.XPATH, "//h2[contains(text(), '常见老年疾病')]")
    assert diseases_title.is_displayed()
    
    # 测试常见老年疾病列表
    diseases_list = driver.find_element(By.CLASS_NAME, "left2_table")
    assert diseases_list.is_displayed()
    
    # 测试高血脂链接
    hyperlipidemia_link = driver.find_element(By.XPATH, "//p[contains(., '高血脂')]")
    assert hyperlipidemia_link.is_displayed()
    
    # 测试心血管链接
    cardiovascular_link = driver.find_element(By.XPATH, "//p[contains(., '心血管')]")
    assert cardiovascular_link.is_displayed()
    
    # 测试老年高血压链接
    elderly_hypertension_link = driver.find_element(By.XPATH, "//p[contains(., '老年高血压')]")
    assert elderly_hypertension_link.is_displayed()
    
    # 测试糖尿病链接
    diabetes_link = driver.find_element(By.XPATH, "//p[contains(., '糖尿病')]")
    assert diabetes_link.is_displayed()

# 测试页面布局和响应式设计
def test_page_layout(driver):
    """测试页面布局和响应式设计"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试左侧内容区域
    left_content = driver.find_element(By.CLASS_NAME, "left1")
    assert left_content.is_displayed()
    
    # 测试右侧内容区域
    right_content = driver.find_element(By.CLASS_NAME, "mrbox")
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
