
import requests
from bs4 import BeautifulSoup
import sched
import time



"""
scrapper parent class
make an object of Scraper class and pass the url
call the run function 
"""
class Scraper:

    def __init__(self, url) -> None:
        self.URL = url
        self.content = self.run()


    """
    for getting parsed request content 
    by passing the request content and the html parser.
    """
    def run(self):

        try:

            request = requests.get(self.URL)
            soup = BeautifulSoup(request.content, 'html.parser')
            return soup

        # handle any errors happen
        except Exception as e:
            return e


    """
    fuction to get content based on tag name as div/tag name
    and attributes names as {"class/id/tag":"name of class/id/tag"}.
    """

    def get_tag_content(self, tag, attr):

        try:
            # filter the content based on the tag ,attributes
            tag_cotent = self.content.find(
                tag, attrs= attr)
            return tag_cotent.text
        except Exception as e:
            return e



    """
    this function is used for scheduling the scraping for 
    a particular interval of time period.
    """
    def sceduler(self, url):
        sced = sched.scheduler(time.time, time.sleep)
        sced.enter(delay=,priority=,run)
        sced.run()



scrapper = Scraper("https://tryhackme.com/paths")

print(scrapper.get_tag_content('div',{'class':'mt-3 size-16 faded'}))