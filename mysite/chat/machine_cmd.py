machine_cmd=['get','machine','information']
machine_cmd_all=['all machine','all']

output=output.split()

def machine_info():
    # url = 'http://192.168.1.2/api/machines'
    # r = requests.get(url)
    # js = r.json()
    print('Machine name -- '+data['name'] + '\n')
    print('ID :'+data['id']+'\n')
    print('Incharge  \n')
    print('Name :'+ data['incharge']['name'] + '\n')
    print('Phone :' + data['incharge']['phone'] + '\n')
    print('Email :' + data['incharge']['email'] + '\n')
    print('Supplier ' + data['supplier']['name'] + '\n')
    print("Checkup \n")
    print('Interval :' + str(data['checkup']['interval']['value']) +' '+ data['checkup']['interval']['unit']+'\n\n')

def get_json_all():
    url = 'http://192.168.1.2/api/machines'
    r = requests.get(url)
    if output in machine_cmd_all:
        js = r.json()
        for data in js:
            print('Machine name -- '+data['name'] + '\n')
            print('ID :'+data['id']+'\n')
            print('Incharge  \n')
            print('Name :'+ data['incharge']['name'] + '\n')
            print('Phone :' + data['incharge']['phone'] + '\n')
            print('Email :' + data['incharge']['email'] + '\n')
            print('Supplier ' + data['supplier']['name'] + '\n')
            print("Checkup \n")
            print('Interval :' + str(data['checkup']['interval']['value']) +' '+ data['checkup']['interval']['unit']+'\n\n')

def get_json_byName():
    url = 'http://192.168.1.2/api/machines'
    r = requests.get(url)
    js = r.json()
    for data in js:
        final = []
        nam = data['name']
        nam = nam.lower()
        for j in nam:
            val = 0
            nam_split = list(j.split())
            for response1 in output:
                if response1 in nam_split:
                    val = val + 1
            if val == len(res_split):
                ''.join(nam_split)
                final.append(nam_split)
    print(final)


if len(output) >2 and output==p:
    print('Which machine information you want')
    print('record func')
    if output in q:
        
        print('All json data')
        get_json_all()
    else:
        get_json_byName()
        print("Related machine detains")
        if len(final)>1:
            for y in range(0,len(final)):
                print(y+1)
                print(final[y])
            print('Record func')
            for z in range(200):
                if output==z:
                    sm=final[z-1] #selected machine =sm
                    url = 'http://192.168.1.2/api/machines'
                    r = requests.get(url)
                    js = r.json()
                    for data in js:
                        if data['name']==sm:
                            machine_info()


        elif len(final)==1:
            sm=final[0] #selected machine =sm
            url = 'http://192.168.1.2/api/machines'
            r = requests.get(url)
            js = r.json()
            for data in js:
                if data['name']==sm:
                    machine_info()

            
        elif len(final)==0:
            print("No machine found\n Try again")
            print("record func")
        else:

else:
    print('Didn\'t get that \n Say again')
    print('go to record func again')
    
