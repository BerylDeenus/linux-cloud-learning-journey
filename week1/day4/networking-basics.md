browser : Initiates an HTTP GET(read only) request when you enter http://localhost.

localhost  (ip): The OS resolves localhost to the loopback IP address, keeping all traffic internal to your machine.

port 80 : The request targets TCP port 80, the standard port for unencrypted HTTP web traffic.it is the usual port for web servers

Nginx : Operating system routes the incoming packet to Nginx cuz it is actively listening on port 80. Nginx processes the request and send back the responce.

HTTP Response : Nginx sends back an HTTP response containing headers (status 200 OK, server info, content type) and the body (HTML webpage content) back to the client.(curl for body curl -I for headers)
