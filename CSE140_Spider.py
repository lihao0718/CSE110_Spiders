# http://cseweb.ucsd.edu/classes/wi16/cse140-a/syllabus.html

#(([abcdefghijklmnopqrstuvwxyz, ])*)

import re
import urllib2
def read_task_info_CSE140(x):

    url = 'http://cseweb.ucsd.edu/classes/wi16/cse140-a/syllabus.html'
    request = urllib2.Request(url)

    response = urllib2.urlopen(request)



    data=(response.read()).replace('\n',"")

    #Ten Weeks Task in total
    task_Regex = re.compile(r'<table.*</table>')
    all_Task_Table = re.findall(task_Regex,data)
    task_Spliter = re.compile(r'<tr.*?</tr>')
    task_Spliter2 = re.compile(r'<td>[0-9\s]*</td>.*?</tr>')
    lines = re.findall(task_Spliter2,all_Task_Table[0])
    regex_spilt_Single_Line = re.compile(r'<td.*?</td>')
    anchor_extractor = re.compile(r'<a.*?</a>')
    regex_extractContents = re.compile(r'<.*?>')
    solution_extractor = re.compile('\[Solution\]')

    print(len(lines))
    for line in lines[1:]:
        cells = re.findall(regex_spilt_Single_Line,line)
        second = cells[2]
        while (regex_extractContents.search(second)):
            second = re.sub(regex_extractContents, "", second)
            while (solution_extractor.search(second)):
                second = re.sub(solution_extractor, "", second)
                print(second[1:])
        third = cells[3]
        while (regex_extractContents.search(third)):
            third = re.sub(regex_extractContents, "", third)
        if(third != "" and third != " "):
            print("[Reading]"+third)


read_task_info_CSE140(1)