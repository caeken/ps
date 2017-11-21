class Config(object):
    ACCOUNT = 'admin'
    PASSWORD = 'xf321'
    
    SHODAN_CONFIG = {
        "api_key" : "",
        "query_list" : []
    }


class ProductionConfig(Config):
    DB = '127.0.0.1'
    PORT = 65521
    DBUSERNAME = 'scan'
    DBPASSWORD = 'scanlol66'
    DBNAME = 'xunfeng'
