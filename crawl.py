import urllib2
import sys
from bs4 import BeautifulSoup


#key=raw_input("Enter the title of first article : ")
#link = "http://en.wikipedia.org/wiki/" + key
#url = urllib2.urlopen(link)

link="http://en.wikipedia.org"
url = urllib2.urlopen(link)




page=""
i=1
while (page!="Philosophy"):
	soup  = BeautifulSoup(url, "html.parser")

	var = soup.find_all('a')

	#var = soup.find("div", {"id":"mw-content-text"})
	crawl_to = var.find("p").find_all("a")

	
	
	for links in crawl_to:
		if (str(links.get("title"))=="None" or str(links.get("title"))=="Latin language" or str(links.get("title"))=="Greek language"):
			pass
		else:
			y=str(links.get("title"))
			#print y
			if (len(y.split())>=2):
				word =''
				for page in range(len(y.split())):
					word = word + y.split()[page]
					if (page!=(len(y.split())-1)):
						word=word+"_"
				y=word

			next_link = "http://en.wikipedia.org/wiki/" + y
			#print next_link
			page=str(links.get("title"))	
			print(page, "(%i)" %i)
			i+=1
			if (page!="Philosophy"):
				print ("Found after " + "(%i)" %i + " links")
			if(i==100):
				print ("Quitting")
				sys.exit(1)
			url = urllib2.urlopen(next_link)
			break