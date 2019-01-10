#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import sqlite3

global conn
print("Database opened successfully")

class SQLoperations:
    def removeCharFromString(self, data, i):
        a = data[ : i]
        b = data[i + 1: ]
        return a + b

    def fetchFilteredData(self, tablename,fieldname,value):
        global conn
        if type(value)==type("String"):
            query = "SELECT * from " + tablename + " WHERE " + fieldname + " = \""+value + "\""
        else:
            query = "SELECT * from " + tablename + " WHERE " + fieldname + " = "+value 
            
        response = ""
        flag = False

        if (tablename == "booking"):
            cursor = conn.execute(query)
            response += "{\"booking\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"tour_name\":\""+str(row[1])+"\","
                response +=  "\"city_id\":"+str(row[2])+","
                response +=  "\"date\":\""+str(row[3])+"\","
                response +=  "\"start_time\":\""+str(row[4])+"\","
                response +=  "\"number_of_people\":"+str(row[5])+","
                response +=  "\"discount\":"+str(row[6])+","
                response +=  "\"payment_type_id\":"+str(row[7])+","
                response +=  "\"channel_id\":"+str(row[8])+","
                response +=  "\"guest_id\":"+str(row[9])+","
                response +=  "\"booking_reference\":\""+str(row[10])+"\","
                response +=  "\"storyteller_id\":"+str(row[11])+"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "booking_channel"):
            cursor = conn.execute(query)
            response += "{\"booking_channel\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"details\":\""+str(row[2])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "city"):
            cursor = conn.execute(query)
            response += "{\"city\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "guest"):
            cursor = conn.execute(query)
            response += "{\"guest\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"mobile_number\":\""+str(row[2])+"\","
                response +=  "\"email\":\""+str(row[3])+"\","
                response +=  "\"details\":\""+str(row[4])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "ops_executive"):
            cursor = conn.execute(query)
            response += "{\"ops_executive\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":\""+str(row[0])+"\","
                response +=  "\"password\":\""+str(row[1])+"\","
                response +=  "\"name\":\""+str(row[2])+"\","
                response +=  "\"designation\":\""+str(row[3])+"\","
                response +=  "\"city_id\":"+str(row[4])+","
                response +=  "\"email\":\""+str(row[5])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "payment_type"):
            cursor = conn.execute(query)
            response += "{\"payment_type\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "story_teller"):
            cursor = conn.execute(query)
            response += "{\"story_teller\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"city_id\":"+str(row[2])+","
                response +=  "\"exp_level\":"+str(row[3])+","
                response +=  "\"salary_per_month\":"+str(row[4])+","
                response +=  "\"cash_holding\":"+str(row[5])+","
                response +=  "\"number_of_tours\":"+str(row[6])+","
                response +=  "\"per_tour_fee\":"+str(row[7])+","
                response +=  "\"per_paid_tour_fee\":"+str(row[8])+"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")
		
        elif (tablename == "storyteller_avaliability"):
            cursor = conn.execute(query)
            response += "{\"storyteller_avaliability\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"date\":\""+str(row[0])+"\","
                response +=  "\"story_teller_ids\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "tour"):
            cursor = conn.execute(query)
            response += "{\"tour\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"type_id\":"+str(row[2])+","
                response +=  "\"city_id\":"+str(row[3])+","
                response +=  "\"start_time\":\""+str(row[4])+"\","
                response +=  "\"duration\":\""+str(row[5])+","
                response +=  "\"price\":"+str(row[6])+"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "tour_type"):
            cursor = conn.execute(query)
            response += "{\"tour_type\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        return response
    def fetchData(self, tablename):
        global conn
        query = "SELECT * from " + tablename
        response = ""
        flag = False

        if (tablename == "booking"):
            cursor = conn.execute(query)
            response += "{\"booking\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"tour_name\":\""+str(row[1])+"\","
                response +=  "\"city_id\":"+str(row[2])+","
                response +=  "\"date\":\""+str(row[3])+"\","
                response +=  "\"start_time\":\""+str(row[4])+"\","
                response +=  "\"number_of_people\":"+str(row[5])+","
                response +=  "\"discount\":"+str(row[6])+","
                response +=  "\"payment_type_id\":"+str(row[7])+","
                response +=  "\"channel_id\":"+str(row[8])+","
                response +=  "\"guest_id\":"+str(row[9])+","
                response +=  "\"booking_reference\":\""+str(row[10])+"\","
                response +=  "\"storyteller_id\":"+str(row[11])+"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "booking_channel"):
            cursor = conn.execute(query)
            response += "{\"booking_channel\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"details\":\""+str(row[2])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "city"):
            cursor = conn.execute(query)
            response += "{\"city\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "guest"):
            cursor = conn.execute(query)
            response += "{\"guest\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"mobile_number\":\""+str(row[2])+"\","
                response +=  "\"email\":\""+str(row[3])+"\","
                response +=  "\"details\":\""+str(row[4])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "ops_executive"):
            cursor = conn.execute(query)
            response += "{\"ops_executive\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":\""+str(row[0])+"\","
                response +=  "\"password\":\""+str(row[1])+"\","
                response +=  "\"name\":\""+str(row[2])+"\","
                response +=  "\"designation\":\""+str(row[3])+"\","
                response +=  "\"city_id\":"+str(row[4])+","
                response +=  "\"email\":\""+str(row[5])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "payment_type"):
            cursor = conn.execute(query)
            response += "{\"payment_type\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "story_teller"):
            cursor = conn.execute(query)
            response += "{\"story_teller\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"city_id\":"+str(row[2])+","
                response +=  "\"exp_level\":"+str(row[3])+","
                response +=  "\"salary_per_month\":"+str(row[4])+","
                response +=  "\"cash_holding\":"+str(row[5])+","
                response +=  "\"number_of_tours\":"+str(row[6])+","
                response +=  "\"per_tour_fee\":"+str(row[7])+","
                response +=  "\"per_paid_tour_fee\":"+str(row[8])+"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")
		
        elif (tablename == "storyteller_avaliability"):
            cursor = conn.execute(query)
            response += "{\"storyteller_avaliability\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"date\":\""+str(row[0])+"\","
                response +=  "\"story_teller_ids\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")
		
        elif (tablename == "tour"):
            cursor = conn.execute(query)
            response += "{\"tour\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\","
                response +=  "\"type_id\":"+str(row[2])+","
                response +=  "\"city_id\":"+str(row[3])+","
                response +=  "\"start_time\":\""+str(row[4])+"\","
                response +=  "\"duration\":\""+str(row[5])+","
                response +=  "\"price\":"+str(row[6])+"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        elif (tablename == "tour_type"):
            cursor = conn.execute(query)
            response += "{\"tour_type\":\"["
            for row in cursor:
                flag = True
                response +=  "{\"id\":"+str(row[0])+","
                response +=  "\"name\":\""+str(row[1])+"\"},"
            response += "]\"}"
            if(flag == True):
                response = self.removeCharFromString(response, -4)
            print(response+"\n")

        return response

    def executeSQLquery(self, query):
        global conn
        try:
            conn.execute(query)
            conn.commit()
            status = "Query executed successfully"
        except:
            status = "Query failed"

        return status

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        #self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    
    def do_GET(self):
        #self._set_headers()
        #self.wfile.write("<html><body><h1>hi!</h1></body></html>")
        if self.path == '/':
            self.path = 'ytsqlinterface.html'
        #return BaseHTTPRequestHandler.do_GET(self)

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print post_data
        sqlobj = SQLoperations()
        self._set_headers()
        if (post_data.find('SELECT') != -1): 
            print ("Performing SELECT operation")
            post_data_list = post_data.split()
            
            # Check for WHERE(For including WHERE API...) 
            if(post_data.find('WHERE') != -1):
                print post_data_list
                value = ""
                for idx,data in enumerate(post_data_list):
                    if idx>6:
                        value+=data
                        if idx!=len(post_data_list)-1:
                            value+=" "
                status = sqlobj.fetchFilteredData(post_data_list[3],post_data_list[5],value);
            else:	
            	status = sqlobj.fetchData(post_data_list[-1])
            self.wfile.write(status)
        elif (post_data.find('INSERT') != -1): 
            print ("Performing INSERT operation")
            self.wfile.write("Performing INSERT operation")
            status = sqlobj.executeSQLquery(post_data)
            self.wfile.write(status)
        elif (post_data.find('UPDATE') != -1): 
            print ("Performing UPDATE operation")
            self.wfile.write("Performing UPDATE operation")
            status = sqlobj.executeSQLquery(post_data)
            self.wfile.write(status)
        elif (post_data.find('DELETE') != -1): 
            print ("Performing DELETE operation")
            self.wfile.write("Performing DELETE operation")
            status = sqlobj.executeSQLquery(post_data)
            self.wfile.write(status)
        else: 
            print ("Invalid Query")
            self.wfile.write("Invalid Query")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    global conn
    print 
    conn = sqlite3.connect('/home/ubuntu/ytserver/ytdatabase.db')
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
    conn.close()
