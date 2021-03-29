This is documentation file for Task3

To make a HTTP request we must first install the requests module. In 'cmd' type "pip install requests" to install the module.

The GET method indicates that you’re trying to get or retrieve data from a specified resource. To make a GET request, invoke requests.get().

POST method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it.

The PUT method requests that the enclosed entity be stored under the supplied URI. If the URI refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.

PATCH is used for modify capabilities. The PATCH request only needs to contain the changes to the resource, not the complete resource.

The DELETE method deletes the specified resource.


HTTP Status Codes:
200: OK
400: Bad Request
403: Forbidden
404: Not found
