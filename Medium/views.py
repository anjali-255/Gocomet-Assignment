from django.shortcuts import render, redirect
from selenium import webdriver
from bs4 import BeautifulSoup
from Medium.models import *


def Scrape(topic):
    browser = webdriver.Chrome(r'C:\Users\Anjali Tyagi\Desktop\MediumScraping\MediumScraping\Medium\chromedriver.exe')
    browser.get("https://medium.com/search?q=" + topic)
    blogs = browser.find_elements_by_class_name('u-paddingTop20')

    all_links = []
    for blog in blogs:
        details = BeautifulSoup(blog.get_attribute('innerHTML'), 'html.parser')
        link = str(details.find('a', class_='button--smaller'))
        link = (link[link.find('href=') + len('href="'):link.find('?source=', link.find('href='))]).replace("\n","").strip()
        all_links.append(link)

    topic = topic.split("%20")
    topic = " ".join(topic)

    for link in all_links:
        browser.get(link)
        try:
            for link in all_links:
                browser.get(link)
                all_data = browser.find_elements_by_tag_name("section")
                data = BeautifulSoup(all_data[1].get_attribute('innerHTML'), 'html.parser')

                newData = data.find_all('h1')
                title = newData[0].text

                author = data.find_all('a')[1].text
                date = data.find_all('a')[2].text

                complete_details = []
                blogDetails = data.find_all('p')
                for details in blogDetails:
                    complete_details.append(details.text)
                    complete_details.append("<br>")

                complete_details = "  ".join(complete_details)
                AllBlogs.objects.create(topic=topic, title=title,
                                        details=complete_details, author=author, date=date)
        except:
            pass

        if len(AllBlogs.objects.filter(topic=topic)) > 10:
            break


def Home(request):
    if request.method == "POST":
        Topic = request.POST['topic'].split(" ")
        Topic = "%20".join(Topic)
        Scrape(Topic)
        return redirect("all_blogs")
    return render(request, 'home.html')


def all_blogs(request):
    return render(request, "all_blogs.html")
