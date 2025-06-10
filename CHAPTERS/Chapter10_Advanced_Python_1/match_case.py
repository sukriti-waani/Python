def http_status(status):
  match status:
    case 200:
      return "OK"
    case 201:
      return "Not Found"
    case 400:
      return "Bad Request"
    case _:
      return "Unknown Status Code"
    
print(http_status(201))