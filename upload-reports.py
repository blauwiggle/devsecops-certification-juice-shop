import requests

headers = {
    'Authorization': 'Token 0999704965ee8fe519d46909c38327e6c4022997'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': 'Gitleaks Scan',
    'minimum_severity': 'Low',
    'engagement': 43,
}

files = {
    'file': open('gitleaks.json', 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Successfully uploaded report')
else:
    print('Failed to upload report')
    print(response.content)