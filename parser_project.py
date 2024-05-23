from bs4 import BeautifulSoup  
import requests                


url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

jobs = results.find_all("div", calss = "card-content")

for jobs in jobs:
    print(jobs, end="\n"*2)

python_jobs = results.find_all("h2", string = lambda text: "python" in text.lower())

python_jobs_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

for jobs in python_jobs_elements:
    title = jobs.find("h2", class_="title")
    company = jobs.find("h3", class_="company")
    location = jobs.find("p", class_="location")
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()