from http.server import BaseHTTPRequestHandler
import json
import random

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Accept, Access-Control-Allow-Origin, Access-Control-Allow-Methods')
        self.end_headers()

        string = '{"platform": "Instagram", "time": 20, "data": 200}, {"platform": "Facebook", "time": 30, "data": 300}, {"platform": "Twitter", "time": 40, "data": 400 }, {"platform": "LinkedIn", "time": 50, "data": 500}, {"platform": "TikTok", "time": 60, "data": 600}'

        sum = 0
        
        data = [
            {"platform": "Instagram", "time": random.randint(5, 120), "data": random.randint(50, 400)},
            {"platform": "Facebook", "time": random.randint(5, 120), "data": random.randint(50, 400)},
            {"platform": "Twitter", "time": random.randint(5, 120), "data": random.randint(50, 400)},
            {"platform": "LinkedIn", "time": random.randint(5, 120), "data": random.randint(50, 400)},
            {"platform": "TikTok", "time": random.randint(5, 120), "data": random.randint(50, 400)},
            {"total": 1488}
        ]

        #json_string = json.dumps(data)

        #for(entry in json_string):
        #    sum += entry['data']

        #data.append({"total": sum})
    
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
