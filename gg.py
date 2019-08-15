#!/usr/bin/python3
import automodule
from multiprocessing import Pool
import json
import falcon    



class Youtube(object):
    def on_get(self, req, resp):
        accounts = json.loads(req.get_param('accounts'))

        pools = Pool(accounts.length)
        for pool in pools :
            pool = 
            t = threading.Thread(target=automodule.getUsers, args= (account,))
            
            t.start()
            #t.join()


        resp.body = 'hi'


api = falcon.API()
api.add_route('/youtube',Youtube())
