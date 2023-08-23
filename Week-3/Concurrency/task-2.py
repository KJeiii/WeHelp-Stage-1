from bs4 import BeautifulSoup
import urllib.request as request
import html5lib
import time

time_start = time.perf_counter()

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
    for n in range(amount_of_post):

        # find title
        title = soup.select(".title a")[n].string

        #find credit
        try:
            credit = soup.select("span.hl")[n].string
        except:
            credit = 0

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

        # create a string conssiting of title,credit,date
        post_data = f"{title},{credit},{post_date}"
        print(post_data)

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


with open("movie.txt","wt") as file :
    for movie in movies_data:
        file.write(movie + "\n")

    
print(f'Finished in {time.perf_counter() - time_start} seconds')
        

    



