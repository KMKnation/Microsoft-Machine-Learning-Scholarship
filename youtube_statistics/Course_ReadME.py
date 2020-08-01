import json


def get_youtube_url(id):
    return "https://www.youtube.com/watch?v={}".format(id)


with open('resource/udacity_azure.json', 'r') as cfile:
    content = json.load(cfile)

with open('Course_ReadME.md', 'w') as file:
    file.write('# Microsoft Azure Machine Learning | Udacity\n')

    for lesson in content:
        index = str(lesson['index'])
        chapters = lesson['chapters']
        for i in range(len(chapters)):
            index += '-' + str(i)
            name = index + ' ' +chapters[i]['name']
            URL = chapters[i]['youtube']
            print(chapters[i])

            file.write('#### {}\n'.format(name))
            file.write('\n')
            html_content = '<div align="center"> \n' \
                           ' <a href="https://www.youtube.com/watch?v={}"> \n' \
                           '<img src="https://img.youtube.com/vi/{}/0.jpg" alt="{}" style="width:100%;"> \n' \
                           ' </a> \n' \
                           ' </div>'.format(URL, URL, name)
            file.write(html_content)
            file.write('\n')
            file.write('\n')
            index = str(lesson['index'])
            '''
            #### TITLE  
            <div align="center">
                 <a href="https://www.youtube.com/watch?v={}">
                 <img src="https://img.youtube.com/vi/{}/0.jpg" alt="{}" style="width:100%;">
                  </a>
            </div>
            '''
