from urllib.parse import urljoin
import expanddouban
from bs4 import BeautifulSoup
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = urljoin('https://movie.douban.com','tag/#/?tags={},{}'.format(category,location))
	return url

"""get html from url"""
url = getMovieUrl("电影","日本")

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
	post_link = ""
	def __init__(self, name, rate, category, location, page_link, post_link):
		super(Movie, self).__init__()
		self.name = name
		self.rate = rate
		self.category = category
		self.location = location
		self.page_link = page_link
		self.post_link = post_link


def getMovies(category, location):
	"""
	return a list of Movie objects with the given category and location.
	"""
	html = expanddouban.getHtml(getMovieUrl(category, location))
	soup = BeautifulSoup(html, "html.parser")
	"""find the movie list in soup"""
	data_div = soup.find(attrs={'data-v-3e982be2':''})
	list_div = data_div.find(class_="list-wp")
	return []