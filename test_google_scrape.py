import requests, bs4
 
#proof of concept
 # use url basic pattern roll through search results, 
 # compare to table do insert update for identified item
 

def construct_urls(term):
    root = "https://www.google.com/#q="
    tail = "&tbs=vw:l&tbm=shop&start="

    blocks = [0,20,40,60,80,100]
    urls = [root+term+tail+str(block) for block in blocks]

    return urls


def get_responses(urls):

    user_agent = {'User-agent': 'Mozilla/5.0'}
    responses = [requests.get(url, headers=user_agent) for url in urls]
    return responses


def parse_html(html):
    parsed_html = {}
    bs4_obj = bs4.BeautifulSoup(html)
    # extract search results s.t. each key in dictionary is a result with data you wanted extracted

    parsed_html = {"name":"treee1", "price":"400.92", "url":"blahblah.com"}
    return parsed_html


def check_database(extracted_data):
    # get database connection
    # look at the key value in extracted_data
    # see if it exists in table
    # if it exists, insert with new price
    # if does not exist, do insert with all values
    




urls = construct_urls("trees")
responses = get_responses(urls)
parsed_htmls = []
for response in responses:
    parsed_htmls.append(parse_html(response.text))

for parsed_html in parsed_htmls:
    check_database(parsed_html)



