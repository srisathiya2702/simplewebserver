 http.server import HTTPServer, BaseHTTPRequestHandler
from
content = """
<html>
<head>
    <title>Details of Laptop</title>
</head>
<body>

<p><b>Sathya (26018933)</b></p>

<table border="4" cellspacing="5" cellpadding="20">
<caption><b>Laptop Device Information</b></caption>

<tr>
    <th>S.No</th>
    <th>Device Type</th>
    <th>Device Information</th>
</tr>

<tr>
    <td>1</td>
    <td>Device Name</td>
    <td>HP-laptop 15</td>
</tr>

<tr>
    <td>2</td>
    <td>Processor</td>
    <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
</tr>

<tr>
    <td>3</td>
    <td>Installed RAM</td>
    <td>16.0 GB (15.7 GB usable)</td>
</tr>

<tr>
    <td>4</td>
    <td>Graphics Card</td>
    <td>Intel(R) Graphics (256 MB)</td>
</tr>

<tr>
    <td>5</td>
    <td>Storage</td>
    <td>145 GB of 477 GB used</td>
</tr>

<tr>
    <td>6</td>
    <td>Device ID</td>
    <td>8A72C5D1-45F9-42B6-91A3-7D2E6F123456</td>
</tr>

<tr>
    <td>7</td>
    <td>Product ID</td>
    <td>00342-42954-11675-AAOEM</td>
</tr>

<tr>
    <td>8</td>
    <td>System Type</td>
    <td>64-bit operating system, x64-based processor</td>
</tr>

<tr>
    <td>9</td>
    <td>Pen and Touch</td>
    <td>No pen or touch input is available for this display</td>
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