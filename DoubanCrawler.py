from urllib.parse import urljoin
import expanddouban
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = urljoin('https://movie.douban.com','tag/#/?tags={},{}'.format(category,location))
	return url

"""get html from url"""
url = getMovieUrl("电影","日本")
print(url)
html = expanddouban.getHtml(url)

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
