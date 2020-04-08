import sys
import os
import requests
import csv
import tqdm
def get_data_from_csv(filename):
    with open(filename, 'r', encoding='utf8') as f:
        all_data=f.read()
    lines=all_data.split('\n')

    data_rows=[]    
    for l in  csv.reader(lines, quotechar='"', delimiter=',',
        quoting=csv.QUOTE_ALL, skipinitialspace=False):
        data_rows.append(l)

    return data_rows


def download(csv_file, folder, epub_also = False):
    data_rows = get_data_from_csv(csv_file)

    print('Download started.')
    for line in tqdm.tqdm(data_rows[1:]):
        url = line[18]
        title = line[0]
        author = line[1]
        pk_name = line[11]

        print(title)
        new_folder = folder + pk_name + '/'

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        r = requests.get(url) 
        new_url = r.url

        new_url = new_url.replace('/book/','/content/pdf/')

        new_url = new_url.replace('%2F','/')
        new_url = new_url + '.pdf'

        final = new_url.split('/')[-1]
        final = title.replace(',','-').replace('.','').replace('/',' ') + ' - ' + author.replace(',','-').replace('.','').replace('/',' ') + ' - ' + final

        myfile = requests.get(new_url, allow_redirects=True)
        open(new_folder+final, 'wb').write(myfile.content)
            
        #download epub version too if exists
        if(epub_also):

            new_url = r.url

            new_url = new_url.replace('/book/','/download/epub/')
            new_url = new_url.replace('%2F','/')
            new_url = new_url + '.epub'

            final = new_url.split('/')[-1]
            final = title.replace(',','-').replace('.','').replace('/',' ') + ' - ' + author.replace(',','-').replace('.','').replace('/',' ') + ' - ' + final
            
            request = requests.get(new_url)
            if request.status_code == 200:
                myfile = requests.get(new_url, allow_redirects=True)
                open(new_folder+final, 'wb').write(myfile.content)
    
    print('Download finished.')
