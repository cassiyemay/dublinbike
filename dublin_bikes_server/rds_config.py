
class rds_config(object):
    
    def __init__(self):
        self.db_endpoint = None
        self.db_username = None
        self.db_password = None
        self.db_name = None
            
    def db_config_setup(self):
        self.db_endpoint = 'dublinbikes.c05zdd0tamge.us-west-2.rds.amazonaws.com'
        self.db_username = 'clover1_2'
        self.db_password = 'lanchenchang'
        self.db_name = 'dublinbikes'
        
