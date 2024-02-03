from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.bestjobs.eu/en/jobs/python').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('h2', class_ = "h6 truncate-2-line").text.strip()
company_div = soup.find('div', class_ = "h6 text-muted text-truncate py-2")
company_name = company_div.find('small').text.strip()
salary = soup.find('div', class_ = "text-nowrap").text.strip()
rating = soup.find('span', class_ = "d-inline-block position-relative stretched")


print(f'''
Company name: {company_name}
Possition: {job}
Salary: {salary}
''')
