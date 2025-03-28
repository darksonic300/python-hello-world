from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()

        string = '{"platform": "Instagram", "time": 20, "data": 200}, {"platform": "Facebook", "time": 30, "data": 300}, {"platform": "Twitter", "time": 40, "data": 400 }, {"platform": "LinkedIn", "time": 50, "data": 500}, {"platform": "TikTok", "time": 60, "data": 600}'

        data = [
            {"platform": "Instagram", "time": 20, "data": 200},
            {"platform": "Facebook", "time": 30, "data": 10},
            {"platform": "Twitter", "time": 40, "data": 378},
            {"platform": "LinkedIn", "time": 50, "data": 300},
            {"platform": "TikTok", "time": 60, "data": 600}
        ]

        json_data = json.loads(data)

        totale = 0

        for spreco_dati in json_data:
            totale += spreco_dati["data"]

        data.extend([{"total": totale}])
        
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
