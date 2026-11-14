from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
    <title>Device Properties</title>
</head>
<body bgcolor="lavender">

<h1 align="center">Sathya</h1>
<h2 align="center">26018933</h2>

<table border="1" cellspacing="10" cellpadding="10">
<caption>Device Properties</caption>

<tr bgcolor="yellow">
    <th>S.No</th>
    <th>Device Info</th>
    <th>Device Property</th>
</tr>

<tr>
    <td>1</td>
    <td>Device Name</td>
    <td>HP Laptop 15</td>
</tr>

<tr>
    <td>2</td>
    <td>Installed RAM</td>
    <td>8.0 GB (7.7 GB usable)</td>
</tr>

<tr>
    <td>3</td>
    <td>Graphics Card</td>
    <td>Intel UHD Graphics (256 MB)</td>
</tr>

<tr>
    <td>4</td>
    <td>Storage</td>
    <td>150 GB of 512 GB used</td>
</tr>

<tr>
    <td>5</td>
    <td>Processor</td>
    <td>Intel Core i5 (2.40 GHz)</td>
</tr>

</table>
</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)

print("My own webserver is running successfully...")
httpd.serve_forever()