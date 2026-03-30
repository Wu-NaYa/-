# 青少年群体眼部疾病预防页面测试脚本
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局变量
BASE_URL = os.path.abspath('yufang.html')

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
    assert "人口疾病分析" in driver.title
    # 验证页面主标题
    main_title = driver.find_element(By.CLASS_NAME, "tith1")
    assert "青少年群体眼部疾病预防" in main_title.text

# 测试导航链接
def test_navigation_links(driver):
    """测试导航链接功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试疾病分析链接
    disease_analysis_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病分析')]")
    assert disease_analysis_link.is_displayed()
    
    # 测试疾病预防链接（当前页面）
    disease_prevention_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病预防')]")
    assert disease_prevention_link.is_displayed()
    
    # 测试返回首页链接
    home_link = driver.find_element(By.XPATH, "//a[contains(text(), '返回首页')]")
    assert home_link.is_displayed()

# 测试眼部疾病四大种类按钮
def test_eye_disease_buttons(driver):
    """测试眼部疾病四大种类按钮"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试近视按钮
    myopia_button = driver.find_element(By.XPATH, "//button[contains(., '近视')]")
    assert myopia_button.is_displayed()
    
    # 测试远视按钮
    hyperopia_button = driver.find_element(By.XPATH, "//button[contains(., '远视')]")
    assert hyperopia_button.is_displayed()
    
    # 测试青光眼按钮
    glaucoma_button = driver.find_element(By.XPATH, "//button[contains(., '青光眼')]")
    assert glaucoma_button.is_displayed()
    
    # 测试散光按钮
    astigmatism_button = driver.find_element(By.XPATH, "//button[contains(., '散光')]")
    assert astigmatism_button.is_displayed()

# 测试视频元素
def test_video_element(driver):
    """测试视频元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试视频元素
    video_element = driver.find_element(By.TAG_NAME, "video")
    assert video_element.is_displayed()
    
    # 测试视频源
    video_source = driver.find_element(By.TAG_NAME, "source")
    assert video_source.get_attribute("src") == "img/video1/yan.mp4"

# 测试页面图表元素
def test_chart_elements(driver):
    """测试页面图表元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试眼部疾病种类占比图表
    disease_ratio_chart = driver.find_element(By.ID, "aleftboxtmidd")
    assert disease_ratio_chart.is_displayed()
    
    # 测试眼部疾病男女患病分析图表
    gender_analysis_chart = driver.find_element(By.ID, "amiddboxtbott1")
    assert gender_analysis_chart.is_displayed()
    
    # 测试各类眼部疾病患病人数图表
    patient_count_chart = driver.find_element(By.ID, "amiddboxtbott2")
    assert patient_count_chart.is_displayed()

# 测试近视科普内容
def test_myopia_edu_content(driver):
    """测试近视科普内容"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试近视科普标题
    edu_title = driver.find_element(By.XPATH, "//h2[contains(text(), '青少年近视科普')]")
    assert edu_title.is_displayed()
    
    # 测试近视科普内容
    edu_content = driver.find_element(By.CLASS_NAME, "left2_table")
    assert edu_content.is_displayed()
    
    # 测试了解更多按钮
    more_info_button = driver.find_element(By.XPATH, "//button[contains(text(), '点击这可以了解更多哦')]")
    assert more_info_button.is_displayed()

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
