import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'rate':3, 'sales_in_first_month':550, 'sales_in_second_month':180})

print(r.json())