# python!
# Takes a list of terms, enters them into the search box, clicks the button and then finds all the resulting
# links and returns them a list, ** with the browser ** I'm not sure this module should do that, we'll see. 

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def search_geneid(terms,browser): 
	'''Input a search term and return a geneid'''
	# Input(list)
	# Return(list)

	print ('using search_geneid')
	
	# Find the keyword field and enter the term 
	keyword_box = '//div[3]/form/table[4]/tbody/tr[2]/td[5]/input[1]'
	try:
		keywordElem = browser.find_element_by_xpath(keyword_box)
		print('Found keywordElem with that xpath!')
	except:
		print('Was not able to find keywordElem with that xpath.')

	for term in terms: 
		keywordElem.send_keys(term)
		button = '//div[3]/form/table[4]/tbody/tr[2]/td[5]/input[2]'
		try:
			buttonElm = browser.find_element_by_xpath(button).click()
			print ('Found buttonElm with that xpath')
		except:
			print('Was not able to find buttonPress.')

		#If, for some reason, the links can't be found, it could be due to the website loading slowly. Time.sleep()
		#gives the browser time to complete loading. 
		time.sleep(3) 
		
		#Return geneid links produced by search
		geneids =[]
		row = 3
		link = None
		
		result_link = '//div[3]/table[3]/tbody/tr/td[1]/form/table[1]/tbody/tr[*]/td[2]/a'

		for link in browser.find_elements_by_xpath(result_link): 
			geneid = link.text
			geneids.append((geneid.split("="))[0]) # split the geneid to provide id to make gene sequence page url 
			
		#print("search_term returns geneids: \n", geneids)
		return geneids 


# Data for testing purposes
'''
terms = ['ig_4', 'Ig_2']
#terms = ['ig_4', 'Ig_2']
geneids = [['badger','badger2','mushroom','mushroom2'], ['monkey','rat','boar','ox','moon']]
transcripts = [[['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']],\
			   [['bad','ger','bad','ger'],['bad2','ger2','bad2','ger2'],['snake','oh','snake'],['mush','room','mush','room']]]

search_geneid(terms)
'''






