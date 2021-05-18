from apiritif import http

response = http.get("http://127.0.0.1:5000/ali")
print(response.text)
