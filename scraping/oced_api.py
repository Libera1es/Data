import requests

def get_oced_data(ds,dimensions,start,end):
    #{Host URL}/{Agency identifier},{Dataset identifier},{Dataset version}/{Data selection}?{other optional parameters}
    #required param
    host_url = "https://sdmx.oecd.org/public/rest/data"
    #agency_ident = ""
    #dat_ident = ""
    src = ds
    
    #optional
    version = ""
    
    dim_args = ['+'.join(d) for d in dimensions]
    dim_str = '.'.join(dim_args)
    
    url = host_url + '/' + src + '/' + dim_str + "/?startTime=" + start + "&endTime=" + end
    
    print(url)
    return requests.get(url)