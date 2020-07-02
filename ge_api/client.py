import requests

from .exceptions import RequestError


class Client:
	"""
	"""
	def __init__(self):
		"""
		"""
		pass

	def _get(self, url):
		"""
		"""
		response = requests.get(url)
		return response.json()
		
	def get_detail(self, item_id):
		"""
		"""
		response = self._get(f"https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={item_id}")
		return response
		
	def get_category(self, category_id):
		"""
		"""
		response = self._get(f"https://services.runescape.com/m=itemdb_rs/api/catalogue/category.json?category={category_id}")
		return response
		
	def get_items(self, category_id, starting_letter, page_number):
		"""
		"""
		response = self._get(f"https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category={category_id}&alpha={starting_letter}&page={page_number}")
		return response
		