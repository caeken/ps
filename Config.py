class Config(object):
    ACCOUNT = 'admin'
    PASSWORD = 'xf321'
    
    SHODAN_CONFIG = {
        "api_key" : "D17aQU0QNYBLHFEQWbmfgEYxgG7z3j0k",
        "query_list" : [['Gateway port:23',30],['huawei country:cn port:8443',30],['zte country:cn port:80',1],['zte country:cn port:8080',1],['tp-link country:cn port:8080',1]]
    }
    #,['username country:cn port:23',200]


class ProductionConfig(Config):
    DB = '127.0.0.1'
    PORT = 65521
    DBUSERNAME = 'scan'
    DBPASSWORD = 'scanlol66'
    DBNAME = 'xunfeng'
