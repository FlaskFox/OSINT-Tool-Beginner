import requests
from core.colors import pink, reset
from googlesearch import search

class FIOOSINT:
	def __init__(self, fio):
		self.fio = fio 

	def fio_checker(self):
		query = self.fio  
		for url in search(query, num_results=15):
			print(url)
