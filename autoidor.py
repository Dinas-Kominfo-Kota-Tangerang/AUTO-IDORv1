# Coded By NAuliajati - Dinas Kominfo Kota Tangerang
# Use your own Risk
# Under BSD 3-Clause License
# Compiled with Python 3.5
import requests

url = 'https://redacted.com:443/admin/pubs/val/14/'

ses = {
    'Cookie': 'ci_session=XXXX',
    'Referer': 'https://redacted.com/pubs/ajax_list?type=pubs'
}

r = requests.get(url, ses, allow_redirects=False)
print(r.status_code)
