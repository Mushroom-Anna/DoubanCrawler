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
