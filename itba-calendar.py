#body = input_data.get('campusmail')
import re
txt = input_data.get('campusmail')
activity_type = ['Assessments', 'Assignments', 'Gradebook']
non_activities = ['Announcements', 'Other new content', 'Blogs']
output = {'activityType': [], 'activityName': [], 'dueDate':[], 'course':[]}
flag = False
txt_list = txt.split('\r\n')
#print(txt_list)


for i in txt_list:
    #print(i)
    #####READ ACTIVITY TYPE######
    if i in activity_type:
        output['activityType'].append(i)
        flag = True
    elif i in non_activities:
        flag = False
        
        
    #####READ ACTIVITY NAME######
    if (i not in activity_type) and (i.find('due soon') != -1) and flag == True:
        activityname = re.sub('<[^>]+>', '', i)
        output['activityName'].append(activityname.split('  due')[0])
    
    
    #####READ DUE DATE######   
    if (i not in activity_type) and (i.find('due soon') != -1) and flag == True:
        duedate = re.sub('<[^>]+>', '', i)
        output['dueDate'].append(duedate.split('  due soon: ')[1][:-4])
        #day = duedate.split('  due soon: ')[1]
        #n = day.find(',', day.find(',')+1)+6
        #startDay = day[:n]+' 08:00:00 AM'
        #output['dueStartDate'].append(startDay)

    
    #####READ COURSE######    
    if re.search(r'\((\d+)Q\)', i[:8]) and flag == True:
        courseName = i
        output['course'].append(courseName)
    
#print(output)
#print(initial_day)