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
    joblist = []
    #A list used to get the information of each job
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
      #This for loop spilts the information of each job into its own index in the list

    filename = 'Data.csv'
    #The csv file name that will be used
    mycsv = csv.writer(open(filename, 'w'))
    #Create the csv file 
    header = ['Salary', 'Description', 'Title', 'Url', 'Company', 'Locations','Site', 'Date']
    mycsv.writerow(header)
    #Write the header row into the csv before writing in the data
    i = 0
    #i is used for indexing the list 
    for row in range(len(joblist)):
        row = i
        mycsv.writerow(joblist[row:i+8])
        i += 8
        #This for loop is used to put the information of each job into one row 
        #This is because that way each job has its own row of information

  except:
    print 'Failure!'
  
  return './module/'+filename