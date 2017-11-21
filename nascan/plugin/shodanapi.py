
#coding:utf-8
import os
import shodan

def run(apikey,query,page):
    api = shodan.Shodan(apikey)

    open_list = {}
    for i in range(1,page+1):
        try:
            results = api.search(query,i)
            print 'current page: %s query:%s total:%s' % (i,query,results['total'])
            
            for result in results['matches']:
                ip = result['ip_str']
                port = result['port']

                if ip in open_list:
                    open_list[ip].append(port)
                else:
                    open_list[ip] = [port]
                    
        except shodan.APIError, e:
                print 'Error: %s' % e

    print 'Results found: %s' % len(open_list)
    return open_list
