print('importing libraries...')
import gspread
import time
print('running all rawl sql queries...')
start1 = time.time()
import DJbehaviour_execute_query
end1 = time.time()
print('finished running queries in', end1 - start1,'seconds')
from oauth2client.service_account import ServiceAccountCredentials

print('accessing google spreadsheet api...')
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/9480/Documents/VIBBIDI/2021/Python project/VIBBIDI_marketing_f8f3d0002af3.json', scope)

client = gspread.authorize(creds)
print('opening worksheet...')
# sheet = client.open('DJ_userbehavior').worksheet('DJ_statistics')
urls = client.open_by_url('https://docs.google.com/spreadsheets/d/1qxoNvkSvDfmIhoJgs9XFucN01kCZsd-1TkVJSzRj-CA/edit#gid=0')
sheet = urls.worksheet('DJ_statistics')

# print('getting all values from worksheet...')
# data = sheet.get_all_values()
# df = pd.DataFrame(data)
# print(df)

print('updating dates in worksheet...')
cell_yesterday4 = sheet.find(str(DJbehaviour_execute_query.yesterday_4))#tìm vị trí của yesterday4
cell_date = sheet.find('Date')#tìm vị trí column date
sheet.update_cell(cell_yesterday4.row+1,cell_date.col,str(DJbehaviour_execute_query.yesterday_3))#update ngày của yesterday3
cell_yesterday3 = sheet.find(str(DJbehaviour_execute_query.yesterday_3))#tìm vị trí của ngày yesterday3
sheet.update_cell(cell_yesterday4.row+2,cell_date.col,str(DJbehaviour_execute_query.yesterday_2))#update ngày của yesterday2
cell_yesterday2 = sheet.find(str(DJbehaviour_execute_query.yesterday_2))#tìm vị trí của ngày yesterday2
sheet.update_cell(cell_yesterday4.row+3,cell_date.col,str(DJbehaviour_execute_query.yesterday))#update ngày của yesterday
cell_yesterday = sheet.find(str(DJbehaviour_execute_query.yesterday))#tìm vị trí của ngày yesterday

def KPI1():
    print("KPI1 is running...")
    start2 = time.time()

    cell_uniquedj = sheet.find('Unique DJ')
    cell_newdj = sheet.find('New DJ')
    cell_uniquelistener = sheet.find('Unique Listener')
    cell_newlistener = sheet.find('New Listener')
    cell_djandlistening = sheet.find('DJ as well as listening')
    cell_userdjcomment = sheet.find('No of users who DJ comment')
    cell_dailydjcomment = sheet.find('Total daily DJ comments')
    cell_chatroomnewjoiner = sheet.find('No of users who create/join new DM chat room')
    cell_userdmcomment = sheet.find('No of users who DM comment')
    cell_dailydmcomment = sheet.find('Total daily DM comments')
    cell_djtotalhour = sheet.find('DJ total hours of play (days)')#tìm vị trí của column cần tìm

    cell_list_uniquedj = sheet.range(int(cell_yesterday4.row),int(cell_uniquedj.col),int(cell_yesterday.row),int(cell_uniquedj.col))
    cell_list_newdj = sheet.range(int(cell_yesterday4.row),int(cell_newdj.col),int(cell_yesterday.row),int(cell_newdj.col))
    cell_list_uniquelistener = sheet.range(int(cell_yesterday4.row),int(cell_uniquelistener.col),int(cell_yesterday.row),int(cell_uniquelistener.col))
    cell_list_newlistener = sheet.range(int(cell_yesterday4.row),int(cell_newlistener.col),int(cell_yesterday.row),int(cell_newlistener.col))
    cell_list_djandlistening = sheet.range(int(cell_yesterday4.row),int(cell_djandlistening.col),int(cell_yesterday.row),int(cell_djandlistening.col))
    cell_list_userdjcomment = sheet.range(int(cell_yesterday4.row),int(cell_userdjcomment.col),int(cell_yesterday.row),int(cell_userdjcomment.col))
    cell_list_dailydjcomment = sheet.range(int(cell_yesterday4.row),int(cell_dailydjcomment.col),int(cell_yesterday.row),int(cell_dailydjcomment.col))
    cell_list_chatroomnewjoiner = sheet.range(int(cell_yesterday4.row),int(cell_chatroomnewjoiner.col),int(cell_yesterday.row),int(cell_chatroomnewjoiner.col))
    cell_list_userdmcomment = sheet.range(int(cell_yesterday4.row),int(cell_userdmcomment.col),int(cell_yesterday.row),int(cell_userdmcomment.col))
    cell_list_dailydmcomment = sheet.range(int(cell_yesterday4.row),int(cell_dailydmcomment.col),int(cell_yesterday.row),int(cell_dailydmcomment.col))
    cell_list_djtotalhour = sheet.range(int(cell_yesterday4.row),int(cell_djtotalhour.col),int(cell_yesterday.row),int(cell_djtotalhour.col))

    for i, val in enumerate(DJbehaviour_execute_query.uniquedj):  #gives us a tuple of an index and value
            cell_list_uniquedj[i].value = val    #use the index on cell_list and the val from cell_values
    sheet.update_cells(cell_list_uniquedj)

    for i, val in enumerate(DJbehaviour_execute_query.newdj):  
            cell_list_newdj[i].value = val    
    sheet.update_cells(cell_list_newdj)

    for i, val in enumerate(DJbehaviour_execute_query.uniquelistener):  
            cell_list_uniquelistener[i].value = val    
    sheet.update_cells(cell_list_uniquelistener)

    for i, val in enumerate(DJbehaviour_execute_query.newlistener):  
            cell_list_newlistener[i].value = val    
    sheet.update_cells(cell_list_newlistener)

    for i, val in enumerate(DJbehaviour_execute_query.djandlistening):  
            cell_list_djandlistening[i].value = val    
    sheet.update_cells(cell_list_djandlistening)

    for i, val in enumerate(DJbehaviour_execute_query.userdjcomment):  
            cell_list_userdjcomment[i].value = val    
    sheet.update_cells(cell_list_userdjcomment)

    for i, val in enumerate(DJbehaviour_execute_query.dailydjcomment):  
            cell_list_dailydjcomment[i].value = val    
    sheet.update_cells(cell_list_dailydjcomment)

    for i, val in enumerate(DJbehaviour_execute_query.chatroomnewjoiner):  
            cell_list_chatroomnewjoiner[i].value = val    
    sheet.update_cells(cell_list_chatroomnewjoiner)

    for i, val in enumerate(DJbehaviour_execute_query.userdmcomment):  
            cell_list_userdmcomment[i].value = val    
    sheet.update_cells(cell_list_userdmcomment)

    for i, val in enumerate(DJbehaviour_execute_query.dailydmcomment):  
            cell_list_dailydmcomment[i].value = val    
    sheet.update_cells(cell_list_dailydmcomment)

    for i, val in enumerate(DJbehaviour_execute_query.djtotalhour):  
            cell_list_djtotalhour[i].value = val    
    sheet.update_cells(cell_list_djtotalhour)
    
    end2 = time.time()
    print('finished running KPI1 in', end2 - start2,'seconds')

def KPI2():
    print("KPI2 is running...")
    start3 = time.time()
    time.sleep(20)

    cell_djreturn7 = sheet.find('Returning DJ 7+ days')
    cell_djreturn14 = sheet.find('Returning DJ 14+ days')
    cell_djreturn30 = sheet.find('Returning DJ 30+ days')
    cell_followers = sheet.find('Follow/followee action')
    cell_videocollect = sheet.find('# of video collection')
    cell_albumcollect = sheet.find('# of album collection')
    cell_artistcollect = sheet.find('# of artist collection')
    cell_blockers = sheet.find('No of blockers')
    cell_1stdate = sheet.find('2020-09-14')
    cell_blockstartdate = sheet.find('2020-11-30')

    cell_list_followers = sheet.range(int(cell_1stdate.row),int(cell_followers.col),int(len(DJbehaviour_execute_query.followers))+int(cell_1stdate.row)-1,int(cell_followers.col))
    cell_list_videocollect = sheet.range(int(cell_1stdate.row),int(cell_videocollect.col),int(len(DJbehaviour_execute_query.videocollect))+int(cell_1stdate.row)-1,int(cell_videocollect.col))
    cell_list_albumcollect = sheet.range(int(cell_1stdate.row),int(cell_albumcollect.col),int(len(DJbehaviour_execute_query.albumcollect))+int(cell_1stdate.row)-1,int(cell_albumcollect.col))
    cell_list_artistcollect = sheet.range(int(cell_1stdate.row),int(cell_artistcollect.col),int(len(DJbehaviour_execute_query.artistcollect))+int(cell_1stdate.row)-1,int(cell_artistcollect.col))
    cell_list_blockers = sheet.range(int(cell_blockstartdate.row),int(cell_blockers.col),int(len(DJbehaviour_execute_query.blockers))+int(cell_blockstartdate.row)-1,int(cell_blockers.col))

    cell_list_djreturn7 = sheet.range(int(cell_yesterday3.row),int(cell_djreturn7.col),int(cell_yesterday.row),int(cell_djreturn7.col))
    cell_list_djreturn14 = sheet.range(int(cell_yesterday3.row),int(cell_djreturn14.col),int(cell_yesterday.row),int(cell_djreturn14.col))
    cell_list_djreturn30 = sheet.range(int(cell_yesterday3.row),int(cell_djreturn30.col),int(cell_yesterday.row),int(cell_djreturn30.col))

    for i, val in enumerate(DJbehaviour_execute_query.djreturn[0]):  
        cell_list_djreturn7[i].value = val    
    sheet.update_cells(cell_list_djreturn7)

    for i, val in enumerate(DJbehaviour_execute_query.djreturn[1]):  
        cell_list_djreturn14[i].value = val    
    sheet.update_cells(cell_list_djreturn14)

    for i, val in enumerate(DJbehaviour_execute_query.djreturn[2]):  
        cell_list_djreturn30[i].value = val    
    sheet.update_cells(cell_list_djreturn30)

    for i, val in enumerate(DJbehaviour_execute_query.followers):  
        cell_list_followers[i].value = val    
    sheet.update_cells(cell_list_followers)

    for i, val in enumerate(DJbehaviour_execute_query.videocollect):  
        cell_list_videocollect[i].value = val    
    sheet.update_cells(cell_list_videocollect)

    for i, val in enumerate(DJbehaviour_execute_query.albumcollect):  
        cell_list_albumcollect[i].value = val    
    sheet.update_cells(cell_list_albumcollect)

    for i, val in enumerate(DJbehaviour_execute_query.artistcollect):  
        cell_list_artistcollect[i].value = val    
    sheet.update_cells(cell_list_artistcollect)

    for i, val in enumerate(DJbehaviour_execute_query.blockers):  
        cell_list_blockers[i].value = val    
    sheet.update_cells(cell_list_blockers)

    end3 = time.time()
    print('finished running KPI2 in', end3 - start3,'seconds')

def KPI3():
    print("KPI3 is running...")
    start4 = time.time()
    time.sleep(20)
    
    cell_videocontribute = sheet.find('# of video contribution')
    cell_albumcontribute = sheet.find('# of album contribution')
    cell_artistcontribute = sheet.find('# of artist contribution')

    cell_list_videocontribute = sheet.range(int(cell_yesterday3.row),int(cell_videocontribute.col),int(cell_yesterday.row),int(cell_videocontribute.col))
    cell_list_albumcontribute = sheet.range(int(cell_yesterday3.row),int(cell_albumcontribute.col),int(cell_yesterday.row),int(cell_albumcontribute.col))
    cell_list_artistcontribute = sheet.range(int(cell_yesterday3.row),int(cell_artistcontribute.col),int(cell_yesterday.row),int(cell_artistcontribute.col))

    for i, val in enumerate(DJbehaviour_execute_query.contribute[0]):  
        cell_list_videocontribute[i].value = val    
    sheet.update_cells(cell_list_videocontribute)

    for i, val in enumerate(DJbehaviour_execute_query.contribute[1]):  
        cell_list_albumcontribute[i].value = val    
    sheet.update_cells(cell_list_albumcontribute)

    for i, val in enumerate(DJbehaviour_execute_query.contribute[2]):  
        cell_list_artistcontribute[i].value = val    
    sheet.update_cells(cell_list_artistcontribute)

    end4 = time.time()
    print('finished running KPI3 in', end4 - start4,'seconds')

KPI1()
KPI2()
KPI3()
print("The file is done processing!")