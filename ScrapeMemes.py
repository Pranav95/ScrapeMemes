from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.request
import os

base_url = "https://knowyourmeme.com"

#first get all the pages with gun debate memes 
def getAllPageUrls():
	urls = list()
	try:
		#the url of the main page for a particular tab - example  /association-football/photos/sort/oldest
		url = ""
		html = urlopen(url).read()
		soup = BeautifulSoup(html)

		pagination = soup.findAll("div",{'class':'pagination'})
		for page in pagination:
			web_page = page.findAll("a", href = True)
			for w in web_page:
				urls.append(w['href'])
	except Exception as e:
		print(str(e))
	return urls

#get urls of the pages where the images are hosted
def getImagePageUrls(page_url):
	image_urls = list()
	try:
		html = urlopen(page_url).read()
		soup = BeautifulSoup(html)

		mydivs = soup.findAll("div", {'class':'item'})
		for div in mydivs:
			temp = div.findAll("a",  href=True)
			for t in temp:
				image_urls.append(t['href'])
	except Exception as e:
		print(str(e))
	return image_urls


#get url of the image
def getImageUrl(url):
	img = ""
	try:
		html = urlopen(url).read()
		soup = BeautifulSoup(html)
		desc = soup.findAll(attrs={"property": re.compile(r"og:image", re.I)}) 
		img = desc[0]['content']
	except Exception as e:
		print(str(e))
	return img



#get all the image urls to download in final_urls
if __name__ == '__main__':
	final_urls = list()

	#the location of the file you want to save your memes in 
	save_file = ""

	base_url = "https://knowyourmeme.com"
	page_list  = getAllPageUrls()
	
	#iterate through all pages
	for page in page_list:
		image_page = getImagePageUrls(base_url+page)
		for image in image_page:
			final = getImageUrl(base_url+image)
			final_urls.append(final)

	os.chdir(save_file)
	try:

		for i,image in enumerate(final_urls):
			f_name = "Image_" + str(i) + ".jpg"
			urllib.request.urlretrieve(image,f_name)
	except Exception as e:
		print(img)




			

