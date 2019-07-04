#importing libraries
import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

page_link = 'https://wayback.archive-it.org/org-1018/20170706202356/http://boshercollection.northwestern.edu/'
page = requests.get(page_link)
page.status_code

#empty arrays for lists
titles = []
subjects = []
creators = []
sources = []
dates = []
contribs = []
types =[]
idens = []
cits = []
descs = []
tags = []
relperf = []

yops = []
dops = []
perfsps = []
venues = []
nhs = []
dirs = []
prods = []
thcoms = []
thcomtys = []
uniacdgrs = []
adps = []
unis = []
deps = []
acts = []
conts = []
pas = []
ancs = []
oancs = []
langs = []
perfgens = []
trans = []
notes = []
sois = []
addrs = []
streets = []
cities = []
chores = []
comps = []

#gets document links
document_links = ["https://wayback.archive-it.org/org-1018/20170706202448/http://boshercollection.northwestern.edu/items/browse?type=1"]

'''
for i in range(1,22):
    link = "https://wayback.archive-it.org/org-1018/20170706202434/http://boshercollection.northwestern.edu/items/browse?type=18"
    if i == 1:
        document_links.append(link)
    else:
        link1 = link + "&page=" + str(i)
        document_links.append(link)
'''
for link in document_links:
    p_page = requests.get(link)
    page.status_code

    #extracting links for each document
    document_content = BeautifulSoup(p_page.content, "html.parser")
    a_link = document_content.find_all('a', class_='permalink')

    links = []
    for link in a_link:
        l = "https://wayback.archive-it.org" + link['href']
        links.append(l)

    #extracting get_information from each page
    for l in links:
        page = requests.get(l)
        page.status_code 

        page_content = BeautifulSoup(page.content, "html.parser")

        #function template
        def get_info(name, id):
            a1 = page_content.find("div", {"id": id})
            if (a1 == None):
                name.append(" ")
            else:
                a2 = a1.find_all("div", {"class": "element-text"})
                abc = ''
                for c in a2:
                    if (abc == '' and len(a2) == 1):
                        abc = c.get_text().splitlines()
                    elif (abc == ''):
                        abc = c.get_text()
                    else:
                        abc = abc + ', ' + c.get_text()
                name.append(abc)
            return name

        def get_relperf(name, id, type):
            a1 = page_content.find("div", {"id": id})
            if (a1 == None):
                name.append(" ")
            else:
                a2 = a1.find_all(type)
                abc = ''
                for c in a2:
                    if (abc == '' and len(a2) == 1):
                        abc = c.get_text().splitlines()
                    elif (abc == ''):
                        abc = c.get_text().lstrip()
                    else:
                        abc = abc + ', ' + c.get_text().lstrip()
                name.append(abc)
            return name

        #images were not working/downloadable to i didnt finish this
        '''
        def get_img(name, id):
            a1 = page_content.find("div", {"id": id})
            if (a1 == None):
                name.append(" ")
            else:
                a2 = a1.find_all(type, {"class": "element-text"})
                abc = ''
                for c in a2:
                    if (abc == '' and len(a2) == 1):
                        abc = c.get_text().splitlines()
                    elif (abc == ''):
                        abc = c.get_text()
                    else:
                        abc = abc + ', ' + c.get_text()
                name.append(abc)
            return name
        '''
        #function calls
        get_info(titles, "dublin-core-title")
        get_info(subjects, "dublin-core-subject")
        get_info(descs, "dublin-core-description")
        get_info(creators, "dublin-core-creator")
        get_info(sources, "dublin-core-source")
        get_info(dates, "dublin-core-date")
        get_info(contribs, "dublin-core-contributor")
        get_info(idens, "dublin-core-identifier")
        get_info(cits, "item-citation")
        get_info(types, "dublin-core-type")
        get_info(tags, "item-tags")
        get_relperf(relperf, "item-relations-display-item-relations", "a")

#putting into CSV file
doc_data = pd.DataFrame({
"Title": titles,
"Description": descs,
"Subject": subjects,
"Creator": creators,
"Source": sources,
"Date": dates,
"Contributor": contribs,
"Type": types,
"Identifier": idens,
"Tags": tags,
"Citation": cits,
"Related Performance": relperf
})

#save link (change to where you want to save it)
doc_data.to_csv('docs_data.csv')