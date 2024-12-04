#ref: https://www.bd-econ.com/imfapi1.html

import requests

def get_imf_data(data_type, database, frequency, indicator, start, end):
    host = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    
    dat_type = data_type #"CompactData" to retrieve data, "DataStructure" to retrieve series info, "GenericMetadata" to get metadata
    
    ds = database #IFS, BOP, etc
    
    freq = frequency
    
    ind = indicator
    
    url = host + dat_type + '/' + ds + '/' + freq + '..' + ind + '.' + '?startPeriod=' + start + '&endPeriod=' + end