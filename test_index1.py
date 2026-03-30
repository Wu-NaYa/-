# 老年人群体心血管疾病分析页面测试脚本
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局变量
BASE_URL = os.path.abspath('index1.html')

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
    assert "老年人群体心血管疾病分析" in main_title.text

# 测试导航链接
def test_navigation_links(driver):
    """测试导航链接功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试疾病科普链接
    disease_edu_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病科普')]")
    assert disease_edu_link.is_displayed()
    
    # 测试疾病分析链接（当前页面）
    disease_analysis_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病分析')]")
    assert disease_analysis_link.is_displayed()
    
    # 测试返回首页链接
    home_link = driver.find_element(By.XPATH, "//a[contains(text(), '返回首页')]")
    assert home_link.is_displayed()
    
    # 测试疾病预测链接
    disease_prediction_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病预测')]")
    assert disease_prediction_link.is_displayed()

# 测试页面图表元素
def test_chart_elements(driver):
    """测试页面图表元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试心血管疾病患病人数图
    patient_count_chart = driver.find_element(By.ID, "purightboxtop")
    assert patient_count_chart.is_displayed()
    
    # 测试心脑血管出院人数占比图表
    discharge_ratio_chart = driver.find_element(By.ID, "amiddboxtbott3")
    assert discharge_ratio_chart.is_displayed()
    
    # 测试心血管疾病死亡率走势图表
    mortality_trend_chart = driver.find_element(By.ID, "amiddboxtbott2")
    assert mortality_trend_chart.is_displayed()
    
    # 测试2016-2021年中国医院高血压病死率走势图
    hypertension_mortality_chart = driver.find_element(By.ID, "purightboxmidd")
    assert hypertension_mortality_chart.is_displayed()
    
    # 测试2015~2021年中国城乡居民心血管病变化率图表
    cardiovascular_change_chart = driver.find_element(By.ID, "pumiddboxtbott1")
    assert cardiovascular_change_chart.is_displayed()

# 测试高血压病因内容
def test_hypertension_causes(driver):
    """测试高血压病因内容"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试高血压病因标题
    causes_title = driver.find_element(By.XPATH, "//h2[contains(text(), '高血压病因')]")
    assert causes_title.is_displayed()
    
    # 测试遗传因素
    genetic_factor = driver.find_element(By.XPATH, "//h3[contains(text(), '遗传因素')]")
    assert genetic_factor.is_displayed()
    
    # 测试精神和环境因素
    mental_factor = driver.find_element(By.XPATH, "//h3[contains(text(), '精神和环境因素')]")
    assert mental_factor.is_displayed()
    
    # 测试生活习惯因素
    lifestyle_factor = driver.find_element(By.XPATH, "//h3[contains(text(), '生活习惯因素')]")
    assert lifestyle_factor.is_displayed()
    
    # 测试药物的影响
    drug_factor = driver.find_element(By.XPATH, "//h3[contains(text(), '药物的影响')]")
    assert drug_factor.is_displayed()

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
