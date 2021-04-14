# Send data to a server using urllib

# TODO: import the request and parse modules
import urllib.request
import urllib.parse

def main():
    url = "http://httpbin.org/get"

    # TODO: create some data to pass to the GET request
    args = {
            "name": "Muhammad Salisu Ali",
            "is_author": True
            }

    # TODO: the data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)

    print(f"Url encoded data: {data}")

    # TODO: issue the request with the data params as part of the URL
    # result = ullib.request.urlopen(url + "?" + data)

    # TODO: issue the request with a data parameter to use POST
    url = "http://httbin.org/post"
    data = data.encode()

    print(f"Encoded data: {data}")

    result = urllib.request.urlopen(url, data=data)

    print(f"Result code: {result.status}")
    print("Returned data: ---------------------------------------------")
   
    print(result.read().decode('utf-8'))

if __name__ == '__main__':
        main()