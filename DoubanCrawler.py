from urllib.parse import urljoin
import expanddouban
from bs4 import BeautifulSoup
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = urljoin('https://movie.douban.com','tag/#/?tags={},{}'.format(category,location))
	return url

class Movie(object):
	"""
	Movie class contains:
	Name, rate, category, location, page link, post link
	"""
	name = ""
	rate = 0
	category = ""
	location = ""
	page_link = ""
	img_link = ""
	def __init__(self, name, rate, category, location, page_link, img_link):
		super(Movie, self).__init__()
		self.name = name
		self.rate = rate
		self.category = category
		self.location = location
		self.page_link = page_link
		self.img_link = img_link

def getMovies(category, location):
	"""
	return a list of Movie objects with the given category and location.
	"""
	html = expanddouban.getHtml(getMovieUrl(category, location))
	soup = BeautifulSoup(html, "html.parser")
	"""find the movie list in soup"""
	list_div = soup.find(attrs={'data-v-3e982be2':''}).find(class_="list-wp")
	items = list_div.find_all(class_="item")
	for item in items:
		name = item.p.find(class_='title').get_text().strip()
		rate = item.p.find(class_='rate').get_text().strip()
		page_link = item.get('href')
		img_link = item.find(class_="pic").img.get('src')
	return []