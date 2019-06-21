from careerjet_api_client import CareerjetAPIClient
import json, ast, csv

#try:
cj  =  CareerjetAPIClient("en_US")

result_json = cj.search({
                        'location'    : 'USA',
                        'keywords'    : 'remodeling',
                        'affid'       : '213e213hd12344552',
                        'user_ip'     : '129.114.19.4',
                        'url'         : 'https://www.careerjet.com/search/jobs?s=remodeling&l=',
                        'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                        })
result_json_1 = ast.literal_eval(json.dumps(result_json))
jobs = (result_json_1['jobs'])
dictOfWords = { i : jobs[i] for i in range(0, len(jobs))}
joblist = []
for i in range(0, len(dictOfWords)):
  job_dict = dictOfWords.get(i)
  joblist.append(job_dict.get('salary'))
  joblist.append(job_dict.get('description'))
  joblist.append(job_dict.get('title'))
  joblist.append(job_dict.get('url'))
  joblist.append(job_dict.get('company'))
  joblist.append(job_dict.get('locations'))
  joblist.append(job_dict.get('site'))
  joblist.append(job_dict.get('date'))

filename = 'Data.csv'
mycsv = csv.writer(open(filename, 'w'))
header = ['Salary', 'Description', 'Title', 'Url', 'Company', 'Locations','Site', 'Date']
mycsv.writerow(header)
i = 0
for row in range(len(joblist)):
    row = i
    mycsv.writerow(joblist[row:i+8])
    i += 8

#except:
  #print 'Failure!'