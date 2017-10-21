# banner_grabbing
Used to tell about server used by any website running on internet

## How it works

`banner_grabbing.py` uses the socket module to create a TCP connection to a
user entered host. This creates the connection by using the `gethostbyname`
function of socket which resolves the Fully Qualified Domain Name (FQDN) to
and IP address via DNS.

On resolving the IP address, a TCP connection is made and a generic HTTP request
message is sent. If the webserver is not serving multiple hosts this will result
in the remote webserver providing a return. 

### Note

If the webserver is using virtual hosts, this will result in a `400` status code 
being returned due to requiring a `host` header to specify the virtualhost being 
reached. The connection will be closed, thus resulting in an `Unable to grab any
information` to be printed on the screen.
