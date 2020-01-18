# python!
# search_term enters terms on the Pfam Domain page for Hydra
# TODO: enter multiple search terms for results. 
# TODO: return multiple geneId for each search term 

import openpyxl
import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

def search_term(term): 
	'''input a search term and return a geneID'''

	if type(term) != str:
		raise NotStringError('the search term is not a string') 

	# Find the keyword field and enter the term 
	keyword_box = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]'
	
	try:
		keywordElem = browser.find_element_by_xpath(keyword_box)
		print('Found keywordElem with that xpath!')
		keywordElem.send_keys(term)
		print(term)
	except:
		print('Was not able to find keywordElem with that xpath.')

	#Click on the search button  
	button = '/html/body/div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]'
	
	try:
		buttonElm = browser.find_element_by_xpath(button).click()
		print ('Found buttonElm with that xpath')
	except:
		print('Was not able to find buttonPress.')

	#return first gene id link produced by search
	result_link = '/html/body/div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[3]/td[2]/a'
	geneIdElem = browser.find_element_by_xpath(result_link).text

	gene_id = (geneIdElem.split("="))[0]
	
	return gene_id

class NotStringError(ValueError): 
	pass   


