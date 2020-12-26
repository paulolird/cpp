
from selenium import webdriver
import pytest

z = int(input("Enter amount of attempts: "))

driver = webdriver.Firefox(executable_path=r"C:\Users\Professional\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe")
driver.get('https://www.igame.com/eye-test/')

def func(y):
  return y + 1

def test_method():
  assert func(z) > 28, "unreasonable amount of checks"
  print("reasonable amount of checks, test successful")
x = 0
while x != z:
  content = driver.find_element_by_class_name('thechosenone')
  content.click()
  x = x + 1

driver.close()
