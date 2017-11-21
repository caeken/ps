
#coding:utf-8
import os
import shodan

def run(apikey,query,page):
    api = shodan.Shodan(apikey)

    open_list = {}
    for p in range(page):
        try:
            results = api.search(query,p+1)

            print 'Results found: %s' % results['total']
            for result in results['matches']:
                ip = result['ip_str']
                port = result['port']

                if ip in open_list:
                    open_list[ip].append(port)
                else:
                    open_list[ip] = [port]
                    
        except shodan.APIError, e:
                print 'Error: %s' % e

    return open_list
