# Proper Library Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

# Query Info
query = 'Data Science Intern'
location = 'United States'


# Note: Selenium uses chromedriver to "control" Chrome
service = Service("C:/Users/Andrew/Documents/CPDS/Scraper/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service = service, options=options)

driver.implicitly_wait(10)

driver.get('https://www.linkedin.com/login')

email_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
email_input.send_keys('amartpsn@gmail.com')
password_input.send_keys('Annakourn1!')
password_input.send_keys(Keys.ENTER)

time.sleep(50)

soup = BeautifulSoup(driver.page_source, 'html.parser')

# html = soup.prettify()

# with open("out.txt","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1


data = []
for page_num in range(1, 150):
    url = f'https://www.linkedin.com/jobs/search/?keywords={query}&location={location}&start={8 * (page_num - 1)}'
    driver.get(url)
    last_height = driver.execute_script('return document.body.scrollHeight')

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(20)  # Wait for 20 seconds

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    li_class = "ember-view jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item"
    try:
        job_postings = soup.find('ul', class_ = 'scaffold-layout__list-container').find_all('li', class_ = li_class)
    except:
        print("Fail To Find Job Postings")
        pass

    # with open("UL.txt","w") as out:
    #     out.write(str(job_postings) + '\n')
    
    # Extract relevant information from each job posting and store it in a list of dictionaries
    job_number = 0
    for job_posting in job_postings:
        job_number += 1
        # with open(f"LI{job_number}.txt","w") as out:
        #     out.write(str(job_posting) + '\n')
        try: 
            job_title = job_posting.find("strong").get_text()
            company_name = job_posting.find("span", class_ =  "job-card-container__primary-description").get_text().strip()
            job_location = job_posting.find('li', class_='job-card-container__metadata-item').get_text().strip()
            Job_Link = "https://www.linkedin.com/" + job_posting.find('a', class_ ="disabled ember-view job-card-container__link job-card-list__title")['href']

            if "Data" in job_title or "AI" in job_title or "ML" in job_title or "Machine Learning" in job_title or "Research" in job_title:
                if "Remote" in job_location:
                    data.append({
                        'Job Title': job_title,
                        'Company Name': company_name,
                        'Location': job_location,
                        'Job Link': Job_Link,
                        'Work Type': 'Remote',
                        })          
                elif "Hybrid" in job_location:
                    data.append({
                        'Job Title': job_title,
                        'Company Name': company_name,
                        'Location': job_location,
                        'Job Link': Job_Link,
                        'Work Type': 'Hybrid',
                        })
                else:
                    data.append({
                        'Job Title': job_title,
                        'Company Name': company_name,
                        'Location': job_location,
                        'Job Link': Job_Link,
                        'Work Type': 'On-Site',
                        })
        except:
            print("Fail To Find Job Info")
            pass    


df = pd.DataFrame(data)
df.to_csv(f'linkedin_jobs_TEST.csv', index=False)
driver.quit()