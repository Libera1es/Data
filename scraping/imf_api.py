#ref: https://www.bd-econ.com/imfapi1.html

import requests
import pandas as pd

def get_imf_database(search_term:str) -> dict:
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    key = 'Dataflow'  # Method with series information
    keywords = search_term  # Term to find in series names
    series_list = requests.get(f'{url}{key}').json()\
            ['Structure']['Dataflows']['Dataflow']

    ds_dict = {}
    for series in series_list:
        if search_term in series['Name']['#text']:
            print(f"{series['Name']['#text']}: {series['KeyFamilyRef']['KeyFamilyID']}")
            
            ds_dict[f"{series['Name']['#text']}"] = f"{series['KeyFamilyRef']['KeyFamilyID']}"
    if not ds_dict:
        print('No such database')
    else:
        return ds_dict



def get_imf_params(database) -> list: 
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    key = 'DataStructure/' + database
    dimension_list = requests.get(f'{url}{key}').json()\
            ['Structure']['KeyFamilies']['KeyFamily']\
            ['Components']['Dimension']
    for n, dimension in enumerate(dimension_list):
        print(f'Dimension {n+1}: {dimension['@codelist']}')
    
    return dimension_list

'''OBSOLETE
def get_imf_code(dimension_list:list, dimension_num:int):
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    #if dimension_num == 0, give codes for all elements of the dimension_list
    if dimension_num == 0:
        for i in range(len(dimension_list)):
            key = f"CodeList/{dimension_list[i]['@codelist']}"
            if key == "CodeList/CL_FREQ": #CL_FREQがなぜかErrorで返ってくる
                continue
            code_list = requests.get(f'{url}{key}').json()\
            ['Structure']['CodeLists']['CodeList']
            code = [(c['Description']['#text'],c['@value'])for c in code_list]

    key = f"CodeList/{dimension_list[1]['@codelist']}"
    code_list = requests.get(f'{url}{key}').json()\
	        ['Structure']['CodeLists']['CodeList']['Code']
    for code in code_list:
        print(f"{code['Description']['#text']}: {code['@value']}")
'''
def get_imf_code_list(dimension_list:list, dimension_num:int):
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    #if dimension_num == 0, give codes for all elements of the dimension_list
    if dimension_num == 0:
        code_dict = {}
        for i in range(len(dimension_list)):
            search_key = dimension_list[i]['@codelist']
            key = f"CodeList/{search_key}"
            if key == "CodeList/CL_FREQ": #CL_FREQがなぜかErrorで返ってくる
                continue
            code_list = requests.get(f'{url}{key}').json()\
            ['Structure']['CodeLists']['CodeList']['Code']
            code = [(c['Description']['#text'],c['@value'])for c in code_list]
            code_dict[search_key] = code
        return code_dict
    else:
        search_key = dimension_list[dimension_num-1]['@codelist']
        key = f"CodeList/{search_key}"
        if key == "CodeList/CL_FREQ":
            return f"Error: Codes of CL_FREQ(dimension_num={dimension_num}) are invalid"
        else:
            code_list = requests.get(f'{url}{key}').json()\
            ['Structure']['CodeLists']['CodeList']['Code']
            code = [(c['Description']['#text'],c['@value']) for c in code_list]
            print(f"Retrieved {search_key}'s codes")
            return code

def get_imf_code(codes:list, string:str) -> str:
    dic = dict(codes)
    matching_keys = {key: value for key, value in dic.items() if string in key}
    return matching_keys

def get_imf_data(database, frequency, indicator, start, end):
    host = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData'
    
    ds = database #IFS, BOP, DOT, etc
    
    freq = frequency
    
    ind = indicator
    
    url = host + '/' + ds + '/' + freq + '.' + ind + '.' + '?startPeriod=' + start + '&endPeriod=' + end