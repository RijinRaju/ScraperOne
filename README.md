
# ScraperOne

ScraperOne is a simple Python web scraping tool that allows you to extract content from web pages based on HTML tags and attributes, and schedule scraping tasks at specified intervals.

## Installation
To install ScraperOne, you can use pip:

   ** pip install ScraperOne **

## Usage
### Initialize ScraperOne
To use ScraperOne, first import the ScraperOne class and create an instance by passing the URL of the webpage you want to scrape:

    from ScraperOne import ScraperOne

    scrapper = ScraperOne("https://example.com")

### Extract Content
You can extract content from the webpage using the get_tag_content method, which takes a tag name and attributes as input:

    content = scrapper.get_tag_content('div', {'class': 'content'})
    print(content)


### Schedule Scraping Tasks
You can schedule scraping tasks to be executed at specified intervals using the scheduler method:


    scrapper.scheduler(delay_time=60, priority=1)


This is a simple scraping package. You can use
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.



