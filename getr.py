# output.txt has the results
import sys
import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome('/home/amarjeet/Downloads/chromedriver_linux64/chromedriver')
browser.maximize_window()
try:
	import hashlib
	import webbrowser
	import pickle
except:
	print('  Install first hashlib,webbrowser\n-------------------------------------------\n   python3 -m pip install pickle\n   python3 -m pip install hashlib\n   python3 -m pip install webbrowser\nThis code will run on Python Version 3.x')
	sys.exit(0)

if sys.version_info[0] != 3:
	print('\n------------------------------\n     USE PYTHON 3.x \n------------------------------\n')
	sys.exit(0)

def open_roll(N):
	maps=pickle.load(open('Finals', 'rb'))
	has=hashlib.md5(N.encode('utf-8')).hexdigest()
	if has in maps.keys():
		cmd='http://academics.iitbhu.ac.in/grade_sheet/index.php?sname='+N+'&sid='+maps[has]+'&msname='+has+'&ms1=95aea4c3483c560373356d1ba3fd73cc'


		browser.get(cmd)
		try:
			btn = WebDriverWait(browser, 10).until(
				EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[1]/td/marquee/a/b/sup"))
			)
			btn = browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/marquee/a/b/sup")
			btn.click()
			name = browser.find_element_by_xpath("/html/body/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]")
			browser.execute_script("window.scrollTo(0, window.scrollY + 2000)")
			btn = browser.find_element_by_xpath("/html/body/table/tbody/tr[5]/td/table[2]/tbody/tr[1]/td[2]/b")
			with open('output.txt', 'a') as f:
				f.write(name.text)
				cpi = " "+btn.text+'\n'
				f.write(cpi)
				f.close()

		finally:
			return 0


try:
	for i in range(0, 0):   # Replace first 0 with the starting roll and the second zero with ending roll
		N = str(i)
		open_roll(N)
except pickle.UnpicklingError:
	content = open('Finals', 'rb').read()
	with open('Finals', 'wb') as output:
		for line in content.splitlines():
			output.write(line + str.encode('\n'))
	# open_roll(N)
except Exception as ex:
	print(ex)
	print('Messege Code Admin ...!')
