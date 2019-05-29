import requests
url = 'http://192.168.1.2/api/machines'
r = requests.get(url)
js = r.json()
res1 = 'Wire Rope Slings'

for data in js:
    final = []
    nam = data['name']
    # print(nam)
    nam = nam.lower()
    nam = list(nam)
    print(nam)
    for j in nam:
        
        val = 0
        
        # nam_split = list(j.split())
        # print(nam_split)
        res_split = list(res1.split())
        # print(res_split)
        for response1 in res_split:
            if response1 in nam:
                val = val + 1
        if val == len(res_split):
            ''.join(nam)
            final.append(nam_split)
print(final)
    


