from careerjet_api_client import CareerjetAPIClient
import json, ast, csv

def csv_tech():
  try:
    cj  =  CareerjetAPIClient("en_US") 
    #This tells the api what country to look for
    result_json = cj.search({
                            'location'    : 'USA',
                            'keywords'    : 'remodeling',
                            'affid'       : '213e213hd12344552',
                            'user_ip'     : '129.114.19.4',
                            'url'         : 'https://www.careerjet.com/search/jobs?s=remodeling&l=',
                            'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                            })
    #This is the information is used to do a get the information
    result_json_1 = ast.literal_eval(json.dumps(result_json))
    #This is used to strip u' from all the dictionaries
    jobs = (result_json_1['jobs'])
    #This is used to get the jobs from the results of the api cal
    dictOfWords = { i : jobs[i] for i in range(0, len(jobs))}
    #This is used to give a number for each job and its information
    joblist1 = []
    joblist2 = []
    joblist3 = []
    joblist4 = []
    joblist5 = []
    joblist6 = []
    joblist7 = []
    joblist8 = []
    #A list used to get the information of each job
    for i in range(0, len(dictOfWords)):
      job_dict = dictOfWords.get(i)
      joblist1.append(job_dict.get('salary'))
      if (job_dict.get('description') != ''):
        joblist2.append(job_dict.get('description'))
        joblist3.append(job_dict.get('title'))
        joblist4.append(job_dict.get('url'))
        joblist5.append(job_dict.get('company'))
        joblist6.append(job_dict.get('locations'))
        joblist7.append(job_dict.get('site'))
        joblist8.append(job_dict.get('date'))
      #This for loop spilts the information of each job into its own index in the list
  except:
    print 'Failure!'

  return joblist1,joblist2,joblist3,joblist4,joblist5,joblist6,joblist7,joblist8
