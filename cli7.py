import os
try:
    import urllib3
except:
    print("urllib3 kurulu degil?!")
    os.system("pip3 install urllib3")
    import urllib3

try:
    import requests
except:
    print("requests kurulu degil?!")
    os.system("pip3 install requests")
    import requests

import json
import random
import time

try:
    from colorama import Fore, Back, Style
except:
    print("colorama kurulu degil?!")
    os.system("pip3 install colorama")
    from colorama import Fore, Back, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

banner = '''
[107;40m[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;m.[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;m.[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m.[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m [38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m,[38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;152m%[38;5;253m&[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;025m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;015m@[38;5;015m@[38;5;029m,[38;5;029m,[38;5;015m@[38;5;025m,[38;5;025m,[38;5;025m,[38;5;m [38;5;m [38;5;m [38;5;m 
[38;5;m [38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;029m,[38;5;253m&[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;m [38;5;m 
[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;025m,[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m.[38;5;025m,[38;5;m [38;5;025m,[38;5;m [38;5;m [38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,[38;5;025m,

               _   _ ______ 
              | | (_)____  |
         ___  | |  _    / / 
        / __| | | | |  / /  
       | (__  | | | | / /   
        \___| |_| |_|/_/    
[0m                        
'''

info = '''
 YED??TEPE ??N??VERS??TES?? KOMUT SATIRI ????RENC?? B??LG??LEND??RME S??STEM??
 Geli??tirici: Emrecan ??KS??M (ben@emreoksum.com.tr || emrecan.oksum@std.yeditepe.edu.tr)
 Geli??tirilme tarihi: 17.01.2022

'''
__verbose__ = False

TOKEN_DIR = "token.txt"

# M7 GENERAL AP??'LER
M7_LOGIN_API = "https://apim7.yeditepe.edu.tr/user/authenticate"
M7_EDUCATIONS_API = "https://apim7.yeditepe.edu.tr/student/educations/" # EDonusum ID concat input
M7_SEMESTERS_API = "https://apim7.yeditepe.edu.tr/student/semesters/" # Department ID concat input
M7_COURSES_API = "https://apim7.yeditepe.edu.tr/student/courses/" # Semester ID concat input
M7_SCHEDULE_API = "https://apim7.yeditepe.edu.tr/student/schedule/" # Semester ID concat input
M7_DEP_INFO_API = "https://apim7.yeditepe.edu.tr/student/education-info/" # Department ID concat input

# M7 MESAJ API'LER??
M7_TOTAL_MESSAGES_API = "https://apim7.yeditepe.edu.tr/student/message-total/" # EDonusum ID concat input
M7_MESSAGES_API = "https://apim7.yeditepe.edu.tr/student/messages/" # EDonusum ID concat input
M7_FULL_MSG_BODY_API = "https://apim7.yeditepe.edu.tr/student/message/" # Message ID concat input
M7_MAVITIK_API = "https://apim7.yeditepe.edu.tr/student/message-read/" # Message ID concat input (HTTP POST)

default_headers = {"X-Requested-With":"tr.edu.yeditepe.yeditepemobil"}

# YARDIMCI FONKS??YONLARIN BA??LANGICI

def verbosity(log):
    if __verbose__:
        print(log)

def randomForeColor():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    return random.choice(colors)

def randomBackColor():
    colors = [Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
    return random.choice(colors)

def getToken():
    token = ""
    if os.path.isfile("token.txt"):
        with open(TOKEN_DIR, "r") as tfh:
            token = tfh.read()
        try:
            token = token.strip()
            token = json.loads(token)
            return token
        except:
            verbosity("Token okunamadi! Yerel depolamadan okunan veri: {0}".format(token))
            try:
                os.unlink(TOKEN_DIR)
            except:
                pass
            pass
    return False
    
def setToken(tokenfull):
    tokenfull = json.dumps(tokenfull)
    with open(TOKEN_DIR, "w") as tfh:
        tfh.write(tokenfull)
    return True

def login(user, passw):
    token = ""
    try:
        h = requests.post(M7_LOGIN_API, headers=default_headers, data={"username":user, "password":passw}, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        token = data
        userinfo = token["user"]
    except:
        verbosity("Token cekilemedi! Donen veri: {0}".format(data))
        return {"token":False, "msg":"Token cekilemedi! Lutfen girdiginiz kullanici adi ve sifreyi, eger dogruysa internet baglantinizi kontrol ediniz!"}
    return {"token":token, "msg":"Giris basarili!"}
    
def education_info(USERID, headers):
    USERID = str(USERID)
    try:
        h = requests.get(M7_EDUCATIONS_API + USERID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        educations = data
    except:
        verbosity("B??l??mler cekilemedi! Donen veri: {0}".format(data))
        return {"educations":False, "msg":"B??l??mler cekilemedi!"}
    return {"educations":educations, "msg":"B??l??mler cekildi!"}

def getSemesters(DEP_ID, headers):
    DEP_ID = str(DEP_ID)
    try:
        h = requests.get(M7_SEMESTERS_API + DEP_ID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        semesters = data
    except:
        verbosity("D??nemler cekilemedi! Donen veri: {0}".format(data))
        return {"semesters":False, "msg":"D??nemler cekilemedi!"}
    return {"semesters":semesters, "msg":"D??nemler cekildi!"}

def getCourses(SEMESTER_ID, headers):
    SEMESTER_ID = str(SEMESTER_ID)
    try:
        h = requests.get(M7_COURSES_API + SEMESTER_ID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        courses = data
    except:
        verbosity("Dersler cekilemedi! Donen veri: {0}".format(data))
        return {"courses":False, "msg":"Dersler cekilemedi!"}
    return {"courses":courses, "msg":"Dersler cekildi!"}

def getMessageCount(USERID, headers):
    USERID = str(USERID)
    try:
        h = requests.get(M7_TOTAL_MESSAGES_API + USERID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        messageCount = data[0]["unread"]
    except:
        verbosity("Okunmamis mesaj sayisi cekilemedi! Donen veri: {0}".format(data))
        return {"messageCount":False, "msg":"Okunmamis mesaj sayisi cekilemedi!"}
    return {"messageCount":messageCount, "msg":"Okunmamis mesaj sayisi cekildi!"}

def getMessages(USERID, headers):
    USERID = str(USERID)
    try:
        h = requests.get(M7_MESSAGES_API + USERID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        messages = data
    except:
        verbosity("Mesajlar cekilemedi! Donen veri: {0}".format(data))
        return {"messages":False, "msg":"Mesajlar cekilemedi!"}
    return {"messages":messages, "msg":"Mesajlar cekildi!"}

def getMessage(MSG_ID, headers):
    MSG_ID = str(MSG_ID)
    try:
        h = requests.get(M7_FULL_MSG_BODY_API + MSG_ID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        message = data
    except:
        verbosity("Mesaj icerigi cekilemedi! Donen veri: {0}".format(data))
        return {"message":False, "msg":"Mesaj icerigi cekilemedi!"}
    return {"message":message, "msg":"Mesaj icerigi cekildi!"}

def sendMaviTik(MSG_ID, headers):
    MSG_ID = str(MSG_ID)
    try:
        h = requests.post(M7_MAVITIK_API + MSG_ID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = data.strip()
        if data == "Success!":
            verbosity("Mesaj okundu bilgisi basariyla iletildi!")
            return
        verbosity("Mesaj okundu bilgisi iletilemedi!")
        return
    except Exception as e:
        verbosity("Mesaj okundu bilgisi iletilirken bir hata meydana geldi! Hata: {0}".format(e))
        return

def getSchedule(SEMESTER_ID, headers):
    SEMESTER_ID = str(SEMESTER_ID)
    try:
        h = requests.get(M7_SCHEDULE_API + SEMESTER_ID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        schedule = data
    except:
        verbosity("Ders programi cekilemedi! Donen veri: {0}".format(data))
        return {"schedule":False, "msg":"Ders programi cekilemedi!"}
    return {"schedule":schedule, "msg":"Ders programi cekildi!"}

def convertScheduleDays(dayNum):
    if dayNum == 1:
        return "PAZARTESI"
    elif dayNum == 2:
        return "SALI"
    elif dayNum == 3:
        return "CARSAMBA"
    elif dayNum == 4:
        return "PERSEMBE"
    elif dayNum == 5:
        return "CUMA"
    elif dayNum == 6:
        return "CUMARTESI"
    elif dayNum == 7:
        return "PAZAR"
    else:
        return "???"

def getStudentInfoByDepartment(DEP_ID, headers):
    DEP_ID = str(DEP_ID)
    try:
        h = requests.get(M7_DEP_INFO_API + DEP_ID, headers=headers, verify=False, timeout=60)
        data = h.text
        data = json.loads(data)
        stdinfo = data
    except:
        verbosity("B??l??m bilgisi ??zerinden ??grenci bilgisi cekilemedi! Donen veri: {0}".format(data))
        return {"stdinfo":False, "msg":"B??l??m bilgisi ??zerinden ??grenci bilgisi cekilemedi!"}
    return {"stdinfo":stdinfo, "msg":"B??l??m bilgisi ??zerinden ??grenci bilgisi cekildi!"}

# YARDIMCI FONKSIYONLARIN B??T??????
# ANA FONKS??YONLARIN BA??LANGICI

def getCourseInfo(userid, default_headers):
    departments = education_info(userid, default_headers)
    if not departments["educations"]:
        print(departments["msg"])
        time.sleep(5)
        return main()
    departments = departments["educations"]
    print("Devam etmek icin lutfen b??l??m seciniz")
    for key, department in enumerate(departments):
        print("(" + str(key+1) + ") " + " (" + str(department["id"]) + ") " + department["name"] + " / " + department["nameEn"])
    secim = input("B??l??m numarasi: ").strip()
    secim = int(secim)-1
    selDepartment = departments[secim]
    selDepartment = selDepartment["id"]
    
    semesters = getSemesters(selDepartment, default_headers)
    if not semesters["semesters"]:
        print(semesters["msg"])
        time.sleep(5)
        return main()
    semesters = semesters["semesters"]
    print("Devam etmek icin lutfen d??nem seciniz")
    for key, semester in enumerate(semesters):
        print("(" + str(key+1) + ") " + " (" + str(semester["id"]) + ") " + str(semester["year"]) + " / " + semester["semester"])
    secim = input("B??l??m numarasi: ").strip()
    secim = int(secim)-1
    selSemester = semesters[secim]
    selSemester = selSemester["id"]
    
    courses = getCourses(selSemester, default_headers)
    if not courses["courses"]:
        print(courses["msg"])
        time.sleep(5)
        return main()
    courses = courses["courses"]
    print("Secilen d??neminiz icin ders kayitlari listelenmistir: ")
    print("DERS KODU | DERS ISMI | DERSTEKI SECTION | DERS KREDISI | HARF NOTU")
    for key, course in enumerate(courses):
        print(course["courseCode"] + " (" + str(course["year"]) + ") | " + course["courseNameEn"] + " | " + str(course["section"]) + " | " + str(course["courseCredit"]) + " | " + str(course["letter"]))

def getMessagesInfo(USERID, headers):
    messages = getMessages(USERID, headers)
    if not messages["messages"]:
        print(messages["msg"])
        time.sleep(5)
        return main()
    messages = messages["messages"]
    messages = list(reversed(messages))
    os.system("clear")
    os.system("cls")
    print("_" * 30)
    print("Gelen Kutusu: ")
    for key, msg in enumerate(messages):
        print("(" + str(key+1) + ") " + str(msg["fullName"]) + " (" + str(msg["course"]) + ") " + str(msg["date"]) + "\n" + str(msg["message"]) + "...")
        print("\n")
    print("L??tfen okumak istediginiz mesajin numarasini tuslayiniz")
    secim = input("Mesaj numarasi: ").strip()
    secim = int(secim)-1
    selMessage = messages[secim]
    selMessage = selMessage["messageId"]
    os.system("clear")
    os.system("cls")
    msgBody = getMessage(selMessage, headers)
    if not msgBody["message"]:
        print(msgBody["msg"])
        time.sleep(5)
        return main()
    msgBody = msgBody["message"][0]
    print("G??nderilme tarihi: " + msgBody["date"])
    print(msgBody["message"])
    sendMaviTik(selMessage, headers)
    print()
    print("Bundan sonra yapmak istediginiz islemi secmeniz gerekmektedir.\n1-) Gelen Kutusuna geri d??n\n2-) Ana men??ye geri d??n\n3-) Uygulamadan cikis yap")
    secim = input("Islem numarasi: ").strip()
    if secim == "1":
        return getMessagesInfo(USERID, headers)
    elif secim == "2":
        return main()
    elif secim == "3":
        print("G??le G??le :)")
        print(Style.RESET_ALL)
        exit(1)
    else:
        print("Hatali tuslama yaptiniz!")
        time.sleep(5)
        return main()

def getScheduleInfo(userid, headers):
    departments = education_info(userid, default_headers)
    if not departments["educations"]:
        print(departments["msg"])
        time.sleep(5)
        return main()
    departments = departments["educations"]
    print("Devam etmek icin lutfen b??l??m seciniz")
    for key, department in enumerate(departments):
        print("(" + str(key+1) + ") " + " (" + str(department["id"]) + ") " + department["name"] + " / " + department["nameEn"])
    secim = input("B??l??m numarasi: ").strip()
    secim = int(secim)-1
    selDepartment = departments[secim]
    selDepartment = selDepartment["id"]
    
    semesters = getSemesters(selDepartment, default_headers)
    if not semesters["semesters"]:
        print(semesters["msg"])
        time.sleep(5)
        return main()
    semesters = semesters["semesters"]
    print("Devam etmek icin lutfen d??nem seciniz")
    for key, semester in enumerate(semesters):
        print("(" + str(key+1) + ") " + " (" + str(semester["id"]) + ") " + str(semester["year"]) + " / " + semester["semester"])
    secim = input("B??l??m numarasi: ").strip()
    secim = int(secim)-1
    selSemester = semesters[secim]
    selSemester = selSemester["id"]
    schedule = getSchedule(selSemester, headers)
    if not schedule["schedule"]:
        print(semesters["msg"])
        time.sleep(5)
        return main()
    schedule = schedule["schedule"]
    
    pzt = []
    sli = []
    crs = []
    prs = []
    cma = []
    cmt = []
    pzr = []
    
    for key, day in enumerate(schedule):
        whichDay = convertScheduleDays(day["day"])
        if whichDay == "PAZARTESI":
            pzt.append(day)
        elif whichDay == "SALI":
            sli.append(day)
        elif whichDay == "CARSAMBA":
            crs.append(day)
        elif whichDay == "PERSEMBE":
            prs.append(day)
        elif whichDay == "CUMA":
            cma.append(day)
        elif whichDay == "CUMARTESI":
            cmt.append(day)
        elif whichDay == "PAZAR":
            pzr.append(day)
    os.system("clear")
    os.system("cls")
    print("\n")
    print("=" * 6, "PAZARTESI", "=" * 6)
    for course in pzt:
        print(str(course["startHour"]) + " - " + str(course["endHour"]) + " arasinda " + course["building"] + " Kat " + str(course["floor"]) + " Oda " + str(course["room"]) + "'da " + course["courseCode"] + " - " + course["courseNameEn"] + " (" + course["firstName"] + " " + course["lastName"] + ")")
    print("\n")
    print("=" * 6, "SALI", "=" * 6)
    for course in sli:
        print(str(course["startHour"]) + " - " + str(course["endHour"]) + " arasinda " + course["building"] + " Kat " + str(course["floor"]) + " Oda " + str(course["room"]) + "'da " + course["courseCode"] + " - " + course["courseNameEn"] + " (" + course["firstName"] + " " + course["lastName"] + ")")
    print("\n")
    print("=" * 6, "CARSAMBA", "=" * 6)
    for course in crs:
        print(str(course["startHour"]) + " - " + str(course["endHour"]) + " arasinda " + course["building"] + " Kat " + str(course["floor"]) + " Oda " + str(course["room"]) + "'da " + course["courseCode"] + " - " + course["courseNameEn"] + " (" + course["firstName"] + " " + course["lastName"] + ")")
    print("\n")
    print("=" * 6, "PERSEMBE", "=" * 6)
    for course in prs:
        print(str(course["startHour"]) + " - " + str(course["endHour"]) + " arasinda " + course["building"] + " Kat " + str(course["floor"]) + " Oda " + str(course["room"]) + "'da " + course["courseCode"] + " - " + course["courseNameEn"] + " (" + course["firstName"] + " " + course["lastName"] + ")")
    print("\n")
    print("=" * 6, "CUMA", "=" * 6)
    for course in cma:
        print(str(course["startHour"]) + " - " + str(course["endHour"]) + " arasinda " + course["building"] + " Kat " + str(course["floor"]) + " Oda " + str(course["room"]) + "'da " + course["courseCode"] + " - " + course["courseNameEn"] + " (" + course["firstName"] + " " + course["lastName"] + ")")
    print("\n")
    print("=" * 6, "CUMARTESI", "=" * 6)
    for course in cmt:
        print(str(course["startHour"]) + " - " + str(course["endHour"]) + " arasinda " + course["building"] + " Kat " + str(course["floor"]) + " Oda " + str(course["room"]) + "'da " + course["courseCode"] + " - " + course["courseNameEn"] + " (" + course["firstName"] + " " + course["lastName"] + ")")
    print("\n")
    print("=" * 6, "PAZAR", "=" * 6)
    for course in pzr:
        print(str(course["startHour"]) + " - " + str(course["endHour"]) + " arasinda " + course["building"] + " Kat " + str(course["floor"]) + " Oda " + str(course["room"]) + "'da " + course["courseCode"] + " - " + course["courseNameEn"] + " (" + course["firstName"] + " " + course["lastName"] + ")")
    print("\n\n")
    print("Bundan sonra yapmak istediginiz islemi secmeniz gerekmektedir.\n1-) Ana men??ye geri d??n\n2-) Uygulamadan cikis yap")
    secim = input("Islem numarasi: ").strip()
    if secim == "1":
        return main()
    elif secim == "2":
        print("G??le G??le :)")
        print(Style.RESET_ALL)
        exit(1)
    else:
        print("Hatali tuslama yaptiniz!")
        time.sleep(5)
        return main()

def getEducationInfo(userid, headers):
    departments = education_info(userid, default_headers)
    if not departments["educations"]:
        print(departments["msg"])
        time.sleep(5)
        return main()
    departments = departments["educations"]
    print("Devam etmek icin lutfen b??l??m seciniz")
    for key, department in enumerate(departments):
        print("(" + str(key+1) + ") " + " (" + str(department["id"]) + ") " + department["name"] + " / " + department["nameEn"])
    secim = input("B??l??m numarasi: ").strip()
    secim = int(secim)-1
    selDepartment = departments[secim]
    selDepartment = selDepartment["id"]
    stdinfo = getStudentInfoByDepartment(selDepartment, headers)
    if not stdinfo["stdinfo"]:
        print(stdinfo["msg"])
        time.sleep(5)
        return main()
    stdinfo = stdinfo["stdinfo"][0]
    os.system("clear")
    os.system("cls")
    print("Fak??lteniz: " + str(stdinfo["faculty"]))
    print("B??l??m??n??z: " + str(stdinfo["department"]))
    print("??grenci Numaraniz: " + str(stdinfo["studentNo"]))
    print("M??fredat: " + str(stdinfo["schedule"]))
    print("Egitim D??zeyi: " + str(stdinfo["level"]))
    print("Kayit Durumu: " + str(stdinfo["status"]))
    print("Burs Orani: " + str(stdinfo["scholarship"]))
    print("Danisman: " + str(stdinfo["advisor"]))
    print("Baslangic tarihi: " + str(stdinfo["startDate"]))
    print("CGPA: " + str(stdinfo["cgpa"]))
    print("Krediler: " + str(stdinfo["credits"]))
    print("ECTS: " + str(stdinfo["ects"]))
    print("\n\n")
    print("Bundan sonra yapmak istediginiz islemi secmeniz gerekmektedir.\n1-) Ana men??ye geri d??n\n2-) Uygulamadan cikis yap")
    secim = input("Islem numarasi: ").strip()
    if secim == "1":
        return main()
    elif secim == "2":
        print("G??le G??le :)")
        print(Style.RESET_ALL)
        exit(1)
    else:
        print("Hatali tuslama yaptiniz!")
        time.sleep(5)
        return main()
# ANA FONKSIYONLARIN B??T??????
# "MAIN" BA??LANGICI

def main():
    os.system("clear")
    os.system("cls")
    print(banner)
    fc = randomForeColor()
    print(fc)
    print(info)
    print("1-) Farkli renkle devam et\n2-) Giris yap\n3-) Uygulamadan cik\n")
    secim = input("Seciminiz: ").strip()
    if secim == "1":
        return main()
    elif secim == "2":
        pass
    elif secim == "3":
        print("G??le G??le! :)")
        print(Style.RESET_ALL)
        exit(1)
    else:
        print("Ge??ersiz islem tusladiniz!")
        time.sleep(5)
        return main()
    token = getToken()
    if not token:
        print("L??tfen devam etmek icin giris yapiniz:")
        user = input("??grenci numarasi VEYA kullanici adi: ")
        passw = input("??grenci hesap sifresi: ")
        lresponse = login(user, passw)
        token = lresponse["token"]
        if not token:
            print(lresponse["msg"])
            return main()
        setToken(token)
    else:
        user = "?"
    default_headers["Authorization"] = "Bearer " + token["token"]
    userid = token["user"]["id"]
    fullname = token["user"]["fullname"]
    os.system("clear")
    os.system("cls")
    print("Tekrardan hosgeldiniz sayin " + fullname + " (" + user + ")")
    okunmamisMesajlar = getMessageCount(userid, default_headers)
    okunmamisMesajlar = okunmamisMesajlar["messageCount"]
    if okunmamisMesajlar and okunmamisMesajlar > 0:
        print("Okunmamis " + str(okunmamisMesajlar) + " adet mesajiniz var. \"Mesajlarim\" islemini secerek okuyabilirsiniz.")
    print("L??tfen yapmak istediginiz islemi seciniz:\n1-) Akademik Bilgilerim (Ders Notlari, Kayitli Dersler)\n2-) Mesajlarim\n3-) Ders Programim\n4-) Kisisel Bilgilerim\n5-) Geri d??n")
    secim = input("Seciminiz: ").strip()
    if secim == "1":
        getCourseInfo(userid, default_headers)
    elif secim == "2":
        getMessagesInfo(userid, default_headers)
    elif secim == "3":
        getScheduleInfo(userid, default_headers)
    elif secim == "4":
        getEducationInfo(userid, default_headers)
    elif secim == "5":
        return main()
    else:
        print("Ge??ersiz islem tusladiniz!")
        time.sleep(5)
    d = input("Devam etmek icin ENTER tusuna basin...")
    print(Style.RESET_ALL)
    return main()

if __name__ == "__main__":
    main()

# Her ??eyin sonu :)