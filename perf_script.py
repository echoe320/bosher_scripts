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
descs = []
dates = []
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
tags = []
cits = []
chores = []
comps = []

#gets performance links (missing pages 7-21 because not on the archive website)
performance_links = ["https://wayback.archive-it.org/org-1018/20170706202434/http://boshercollection.northwestern.edu/items/browse?type=18",
    "https://wayback.archive-it.org/org-1018/20170706203414/http://boshercollection.northwestern.edu/items/browse?type=18&page=2",
    "https://wayback.archive-it.org/org-1018/20170706222055/http://boshercollection.northwestern.edu/items/browse?type=18&page=3",
    "https://wayback.archive-it.org/org-1018/20170707060908/http://boshercollection.northwestern.edu/items/browse?type=18&page=4",
    "https://wayback.archive-it.org/org-1018/20170707234045/http://boshercollection.northwestern.edu/items/browse?type=18&page=5",
    "https://wayback.archive-it.org/org-1018/20170709003600/http://boshercollection.northwestern.edu/items/browse?type=18&page=6"]
#performance_link = "https://wayback.archive-it.org/org-1018/20170706202434/http://boshercollection.northwestern.edu/items/browse?type=18"
'''
for i in range(1,22):
    link = "https://wayback.archive-it.org/org-1018/20170706202434/http://boshercollection.northwestern.edu/items/browse?type=18"
    if i == 1:
        performance_links.append(link)
    else:
        link1 = link + "&page=" + str(i)
        performance_links.append(link)
'''
for link in performance_links:
    p_page = requests.get(link)
    page.status_code

    #extracting links for each performance
    performance_content = BeautifulSoup(p_page.content, "html.parser")
    a_link = performance_content.find_all('a', class_='permalink')

    links = []
    for link in a_link:
        l = "https://wayback.archive-it.org" + link['href']
        links.append(l)

    #extracting information from each page
    for l in links:
        page = requests.get(l)
        page.status_code 

        page_content = BeautifulSoup(page.content, "html.parser")

        #function template
        def info(name, id):
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

        #function calls
        info(titles, "dublin-core-title")
        info(descs, "dublin-core-description")
        info(dates, "dublin-core-date")
        info(yops, "performance-item-type-metadata-year-of-production")
        info(dops, "performance-item-type-metadata-dates-of-production")
        info(perfsps, "performance-item-type-metadata-performance-space")
        info(venues, "performance-item-type-metadata-venue")
        info(nhs, "performance-item-type-metadata-neighborhood")
        info(dirs, "performance-item-type-metadata-directors")
        info(prods, "performance-item-type-metadata-producers")
        info(thcoms, "performance-item-type-metadata-theater-companygroup")
        info(thcomtys, "performance-item-type-metadata-theater-company-type")
        info(uniacdgrs, "performance-item-type-metadata-university-departmentacademic-group-as-advertised")
        info(adps, "performance-item-type-metadata-adaptators")
        info(unis, "performance-item-type-metadata-university")
        info(deps, "performance-item-type-metadata-department")
        info(acts, "performance-item-type-metadata-actors-or-other-performers")
        info(conts, "performance-item-type-metadata-other-contributors")
        info(pas, "performance-item-type-metadata-play-author-as-advertised")
        info(ancs, "performance-item-type-metadata-primary-ancient-source")
        info(oancs, "performance-item-type-metadata-other-ancient-sources")
        info(langs, "performance-item-type-metadata-languages")
        info(perfgens, "performance-item-type-metadata-performative-genres")
        info(trans, "performance-item-type-metadata-translators")
        info(notes, "performance-item-type-metadata-notes")
        info(sois, "performance-item-type-metadata-sources-of-information")
        info(addrs, "performance-item-type-metadata-address")
        info(streets, "performance-item-type-metadata-street")
        info(cities, "performance-item-type-metadata-city")
        info(tags, "item-tags")
        info(cits, "item-citation")
        info(chores, "performance-item-type-metadata-choreographers")
        info(comps, "performance-item-type-metadata-composers")

#putting into CSV file
perf_data = pd.DataFrame({
"Title": titles,
"Description": descs,
"Date": dates,
"Year of Production": yops,
"Dates of Production": dops,
"Performance space": perfsps,
"Venue": venues,
"Neighborhood": nhs,
"Director(s)": dirs,
"Producer(s)": prods,
"Theater company/group": thcoms,
"Theater company type": thcomtys,
"University department/academic group, as advertised": uniacdgrs,
"Adaptator(s)": adps,
"University": unis,
"Department": deps,
"Actor(s) (or other performers)": acts,
"Choreographer(s)": chores,
"Composer(s)": comps,
"Other contributor(s)": conts,
"Play author (as advertised)": pas,
"Primary ancient source": ancs,
"Other ancient source(s)": oancs,
"Language(s)": langs,
"Performative genre(s)": perfgens,
"Translator(s)": trans,
"Notes": notes,
"Source(s) of information": sois,
"Address": addrs,
"Street": streets,
"City": cities,
"Tags": tags,
"Citation": cits
})

#save link (change to where you want to save it)
perf_data.to_csv('perf_data.csv')