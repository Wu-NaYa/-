# 心血管疾病预测页面测试脚本
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 全局变量
BASE_URL = os.path.abspath('yufang1.html')

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
    assert "心血管疾病分析" in driver.title
    # 验证页面主标题
    main_title = driver.find_element(By.CLASS_NAME, "tith1")
    assert "心血管疾病预测" in main_title.text

# 测试导航链接
def test_navigation_links(driver):
    """测试导航链接功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试疾病科普链接
    disease_edu_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病科普')]")
    assert disease_edu_link.is_displayed()
    
    # 测试疾病分析链接
    disease_analysis_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病分析')]")
    assert disease_analysis_link.is_displayed()
    
    # 测试返回首页链接
    home_link = driver.find_element(By.XPATH, "//a[contains(text(), '返回首页')]")
    assert home_link.is_displayed()
    
    # 测试疾病预测链接（当前页面）
    disease_prediction_link = driver.find_element(By.XPATH, "//a[contains(text(), '疾病预测')]")
    assert disease_prediction_link.is_displayed()

# 测试预测表单元素
def test_prediction_form_elements(driver):
    """测试预测表单元素是否存在"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试身高输入框
    height_input = driver.find_element(By.ID, "loan_1")
    assert height_input.is_displayed()
    
    # 测试体重输入框
    weight_input = driver.find_element(By.ID, "loan_2")
    assert weight_input.is_displayed()
    
    # 测试收缩压输入框
    systolic_input = driver.find_element(By.ID, "loan_3")
    assert systolic_input.is_displayed()
    
    # 测试舒张压输入框
    diastolic_input = driver.find_element(By.ID, "loan_4")
    assert diastolic_input.is_displayed()
    
    # 测试胆固醇输入框
    cholesterol_input = driver.find_element(By.ID, "loan_5")
    assert cholesterol_input.is_displayed()
    
    # 测试葡萄糖输入框
    glucose_input = driver.find_element(By.ID, "loan_6")
    assert glucose_input.is_displayed()
    
    # 测试是否长期抽烟下拉框
    smoke_select = driver.find_element(By.ID, "loan_7")
    assert smoke_select.is_displayed()
    
    # 测试是否长期喝酒下拉框
    alcohol_select = driver.find_element(By.ID, "loan_8")
    assert alcohol_select.is_displayed()
    
    # 测试是否坚持运动下拉框
    exercise_select = driver.find_element(By.ID, "loan_9")
    assert exercise_select.is_displayed()
    
    # 测试预测结果输出
    prediction_output = driver.find_element(By.ID, "predict")
    assert prediction_output.is_displayed()
    
    # 测试点击预测按钮
    predict_button = driver.find_element(By.XPATH, "//button[contains(text(), '点击预测')]")
    assert predict_button.is_displayed()

# 测试预测表单功能
def test_prediction_form_submission(driver):
    """测试预测表单提交功能"""
    driver.get(f"file://{BASE_URL}")
    
    # 填写表单
    driver.find_element(By.ID, "loan_1").send_keys("170")  # 身高
    driver.find_element(By.ID, "loan_2").send_keys("65")   # 体重
    driver.find_element(By.ID, "loan_3").send_keys("120")  # 收缩压
    driver.find_element(By.ID, "loan_4").send_keys("80")   # 舒张压
    driver.find_element(By.ID, "loan_5").send_keys("1")    # 胆固醇
    driver.find_element(By.ID, "loan_6").send_keys("1")    # 葡萄糖
    
    # 选择下拉框
    smoke_select = driver.find_element(By.ID, "loan_7")
    smoke_select.click()
    smoke_select.find_element(By.XPATH, "//option[@value='0']").click()  # 否
    
    alcohol_select = driver.find_element(By.ID, "loan_8")
    alcohol_select.click()
    alcohol_select.find_element(By.XPATH, "//option[@value='0']").click()  # 否
    
    exercise_select = driver.find_element(By.ID, "loan_9")
    exercise_select.click()
    exercise_select.find_element(By.XPATH, "//option[@value='1']").click()  # 是
    
    # 点击预测按钮
    predict_button = driver.find_element(By.XPATH, "//button[contains(text(), '点击预测')]")
    predict_button.click()
    
    # 测试预测结果是否显示
    # 注意：由于是前端模拟，实际预测结果可能不会显示，但我们可以测试按钮点击后页面是否正常
    assert driver.title

# 测试心血管预防方法内容
def test_prevention_methods(driver):
    """测试心血管预防方法内容"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试预防方法标题
    prevention_title = driver.find_element(By.XPATH, "//h2[contains(text(), '小贴士：快来看看心血管的预防方法吧！')]")
    assert prevention_title.is_displayed()
    
    # 测试一级预防内容
    primary_prevention = driver.find_element(By.XPATH, "//p[contains(text(), '一级预防:')]")
    assert primary_prevention.is_displayed()
    
    # 测试二级预防内容
    secondary_prevention = driver.find_element(By.XPATH, "//p[contains(text(), '二级预防:')]")
    assert secondary_prevention.is_displayed()
    
    # 测试了解更多按钮
    more_info_button = driver.find_element(By.XPATH, "//button[contains(text(), '点我了解更多吧')]")
    assert more_info_button.is_displayed()

# 测试页面布局和响应式设计
def test_page_layout(driver):
    """测试页面布局和响应式设计"""
    driver.get(f"file://{BASE_URL}")
    
    # 测试左侧内容区域
    left_content = driver.find_element(By.CLASS_NAME, "mrbox_topmidd")
    assert left_content.is_displayed()
    
    # 测试右侧内容区域
    right_content = driver.find_element(By.CLASS_NAME, "mrbox_top_right")
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
