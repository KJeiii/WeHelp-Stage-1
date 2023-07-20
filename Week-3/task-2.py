from bs4 import BeautifulSoup
import urllib.request as request
import html5lib

# connect to ppt url and make a sooup
ppt_url = "https://www.ptt.cc/bbs/movie/index.html"
headers_info = {'User-Agent': 'Mozilla/5.0'}

request_info = request.Request(ppt_url, headers = headers_info)
with request.urlopen(request_info) as response:
    data = response.read().decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")

movies_data = []

for n in range(3):
    # scrab first page
    amount_of_post = len(soup.select(".title a"))
    print(amount_of_post)
    for n in range(amount_of_post):

        post_data = {}

        # find title
        title = soup.select(".title a")[n].string
        post_data["title"] = title
        print(title)


        #find credit
        try:
            credit = soup.select("span.hl")[n].string
        except:
            credit = 0
        finally:
            post_data["credit"] = credit
        print(credit)

        # find post url
        post_url = "https://www.ptt.cc/" + soup.select(".title a")[n]["href"]

        # find post date; date is in the post content
        # connect to post url
        post_request_info = request.Request(post_url, headers = headers_info)
        with request.urlopen(post_request_info) as response:
            data = response.read().decode("utf-8")
            post_soup = BeautifulSoup(data, "html.parser")

        # find date
        post_date = post_soup.select("span.article-meta-value")[3].string
        post_data["post_date"] = post_date

        # movies_data append post_data
        movies_data.append(post_data)

    # scrab previos page
    # find previous page url
    previous_page_url = None
    for element in soup.select("a.btn"):
        if element.string == "‹ 上頁":
            previous_page_url = "https://www.ptt.cc/" + element["href"]
    
    # connect to previous page
    prevois_page_request = request.Request(previous_page_url, headers = headers_info)
    with request.urlopen(prevois_page_request) as response:
        data = response.read().decode("utf")
        soup = BeautifulSoup(data,"html.parser")


print(movies_data)
    
        

    



