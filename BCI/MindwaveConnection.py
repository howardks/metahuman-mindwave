

import hashlib
import json
import socket
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

RAW_COLUMNS = ['attention', 'meditation', 'delta', 'theta', 'lowAlpha', 'highAlpha', 'lowBeta', 'highBeta', 'lowGamma', 'highGamma']

class Mindwave(object): 
    def __init__(self, appname="myapp", appkey="mykey"): 
        self.TGHOST = "127.0.0.1"
        self.TGPORT = 13854
        self.APPNAME = appname
        self.APPKEY = appkey
        self.CONFSTRING = '{"enableRawOutput": false, "format": "Json"}'
        self.HEADER_EEGPOWER = [u'delta',
                                u'theta',
                                u'lowAlpha',
                                u'highAlpha',
                                u'lowBeta',
                                u'highBeta',
                                u'lowGamma',
                                u'highGamma']
        self.HEADER_ESENSE = [u'attention',
                              u'meditation']
    
    def authenticate(self): 
        # open socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.TGHOST, int(self.TGPORT)))
        
        # hash app key
        app_key = hashlib.sha1(self.APPKEY.encode('utf-8')).hexdigest()

        # authenticate
        auth_request = json.dumps({"appName": self.APPNAME, "appKey": app_key}, sort_keys=False)
        sock.setblocking(0)
        sock.send(str(auth_request).encode('utf-8'))
        print('Authentication request sent. ')
        try:
            sock.recv(1024)
            print('Authentication complete. ')
        except:
            print('Device already authenticated. ')

    def collect_data(self, duration=10):
        # open socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.TGHOST, int(self.TGPORT)))

        # configuration
        sock.send(self.CONFSTRING.encode('utf-8'))

        data_all = {}
        s = '\r\n'.encode('utf-8')
        d = 0
        start_time = time.time()
        print('Data collection started. Do not remove headset. ')
        while (d<duration):
            # entry: array to hold one-time reading
            entry = []
            try:
                print('Reading data ', d)
                data = sock.recv(1024).strip()
                if s in data: 
                    data = data.split(s)[1]
                #print(data)
                json_data = json.loads(data)
                print(json_data)
                # read data and add entry to json_all
                if 'eegPower' in json_data:
                    for i in self.HEADER_ESENSE:
                        if i in json_data['eSense']:
                            entry.append(str(json_data['eSense'][i]))
                    for i in self.HEADER_EEGPOWER:
                        if i in json_data['eegPower']:
                            entry.append(str(json_data[u'eegPower'][i]))
                    
                    # check if data is valid (no 0s, no empty values)
                    entry = np.array(entry)
                    if len(entry)==10 and len(entry[entry=='0'])==0: 
                        # get current time
                        t = str(time.time())
                        data_all[t] = entry.tolist()
                        d += 1
                # check if timeout
                curr_time = time.time()
                if curr_time-start_time > 80:
                    data_all = None
                    break
            except:
                print ('Could not read from socket. Please try again. ')
                #break
        
        # finished
        if data_all == None: 
            print(data_all)
            return data_all

        json_all = json.dumps(data_all)
        print('Data collection finished. ')
        print(json_all)
        return json_all
    
    def create_df(self, json_data): 
        """Loads data from json and convert to pandas dataframe. """
        loaded = json.loads(json_data)
        self.raw = loaded
        df = pd.DataFrame.from_dict(loaded, orient='index', columns=RAW_COLUMNS)
        self.data = df
        print('Data loaded. ')
        return df
    
    def create_linegraph(self, dataf):
        plt.plot(dataf['delta'], color='red', label='delta')
        plt.plot(dataf['theta'], color='orange', label='theta')
        plt.plot(dataf['lowAlpha'], color='yellow', label='low alpha')
        plt.plot(dataf['highAlpha'], color='green', label='high alpha')
        plt.plot(dataf['lowBeta'], color='blue', label='low beta')
        plt.plot(dataf['highBeta'], color='indigo', label='high beta')
        plt.plot(dataf['lowGamma'], color='violet', label='low gamma')
        plt.plot(dataf['highGamma'], color='pink', label='high gamma')
        plt.legend()
        plt.title("Mindwave Mobile 2 EEG Wave Quantities")
        plt.xlabel("Time")
        plt.ylabel("Amount")
        plt.show()

if __name__ == '__main__':
    MW = Mindwave()
    MW.authenticate()
    data = MW.collect_data()
    df = MW.create_df(data)
    
    df.to_csv('test.csv')
    print(df)
    