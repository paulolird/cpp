from selenium import webdriver
import pytest

driver = webdriver.Firefox(executable_path=r"C:\Users\Professional\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe")
driver.get('https://www.igame.com/eye-test/')

def func(y):
  return y + 1

def test_method():
  x = 0
  while x != 8:
    content = driver.find_element_by_class_name('thechosenone')
    content.click()
    x = x + 1
  assert func(8) == 9 , "fail"
  driver.close()
