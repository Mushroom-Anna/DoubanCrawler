from urllib.parse import urljoin
import expanddouban
from bs4 import BeautifulSoup
import csv
import codecs
import json
"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
def getMovieUrl(category, location):
	url = 'https://movie.douban.com/tag/#/?sort=S&range=9,10&tags={},{}'.format(category,location)
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

def writeIntoCvs(movies):
	"""write movies list into csv"""
	with codecs.open('movies.csv', 'w', encoding='utf-8-sig') as csvfile:
		#configure writer to write standard csv file
		writer = csv.writer(csvfile)
		writer.writerow(['name', 'rate', 'category', 'location', 'page_link', 'img_link'])
		for movie in movies:
			writer.writerow([movie.name, movie.rate, movie.category, movie.location, movie.page_link, movie.img_link])

def getMovieDict(movies, category):
	"""
	get numbers of movies in different locations
	return sorted dictionary and the total number
	"""
	location_dict = {}
	total = 0
	for movie in movies:
		if movie.category == category:
			total += 1
			if movie.location in location_dict:
				location_dict[movie.location] += 1 
			else:
				location_dict[movie.location] = 1 
	location_dict_sorted = sorted(location_dict.items(), key=lambda e:e[1], reverse=True)
	return location_dict_sorted, total

#get movies in categories and locations
movies = []
categories = ["青春","音乐","家庭"]
locations = ["大陆","美国","香港","台湾","日本","韩国","英国","法国","德国","意大利","西班牙","印度","泰国","俄罗斯","伊朗","加拿大","澳大利亚","爱尔兰","瑞典","巴西","丹麦"]
for category in categories:
	for location in locations:
		movies.extend(getMovies(category,location))
writeIntoCvs(movies)

#get dictionaries of three categories and total number of each category
category_dict = []
total_list = []
for category in categories:
	dic, total = getMovieDict(movies,category)
	category_dict.append(dic)
	total_list.append(total)
#write output into txt
with open('output.txt','w') as txtfile:
	for i in range(len(category_dict)):
		txtfile.write(categories[i]+'\n')
		for j in range(3):
			txtfile.write(json.dumps(category_dict[i][j], ensure_ascii=False))
			txtfile.write(str(category_dict[i][j][1]/total_list[i])+'\n')