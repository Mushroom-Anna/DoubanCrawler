from urllib.parse import urljoin
import expanddouban
from bs4 import BeautifulSoup
import csv
import codecs
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = urljoin('https://movie.douban.com','tag/#/?sort=S&range=9,10&tags={},{}'.format(category,location))
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
	movies = []
	"""
	return a list of Movie objects with the given category and location.
	"""
	html = expanddouban.getHtml(getMovieUrl(category, location), True)
	soup = BeautifulSoup(html, "html.parser")
	#find the movie list in soup
	list_div = soup.find(attrs={'data-v-3e982be2':''}).find(class_="list-wp")
	items = list_div.find_all(class_="item")
	#get data of each movie
	for item in items:
		name = item.p.find(class_='title').get_text().strip()
		rate = item.p.find(class_='rate').get_text().strip()
		page_link = item.get('href')
		img_link = item.find(class_="pic").img.get('src')
		movies.append(Movie(name, rate, category, location, page_link, img_link))
	return movies

#write movies into csv
movies = getMovies("电影","日本")
with open('movies.csv', 'w', encoding='gb18030') as csvfile:
	#configure writer to write standard csv file
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
	writer.writerow(['name', 'rate', 'category', 'location', 'page_link', 'img_link'])
	for movie in movies:
		writer.writerow([movie.name, movie.rate, movie.category, movie.location, movie.page_link, movie.img_link])