
#######################################
#     CRM ENV 78 - DUMP GENERATOR     #
#     @author - Maxi Carranza         #
#             30/12/2019              #
#             version. 1              #
#######################################
# UPDATE - 15/06/2020: Add sys module to invoke process with flags parameters.
# UPDATE - 26/05/2021: Cambia nombre script y path donde se generan los archivos dmp

import sys
import os
import datetime as dt
import commands
import time

def exporting(filename):
    directory = "/tefuser2/tef/crm/tefcrm78/dmp/"+ filename
    log_file = open(directory, 'r')
    read_log = log_file.read()
    export = [' - Exporting - ', '~  Exporting  ~']
    e = 0
    successfully = "Export terminated successfully without warnings."
    warning = "Export terminated successfully with warnings."
    exception = "EXP-"
    exception_ora = "ORA-"
    while successfully not in read_log and warning not in read_log and exception not in read_log and exception_ora not in read_log:
        
        if e == 0:
            com = 'printf \r"\033[93m>> %s"' % export[1]
            e = 1
        else:
            com = 'printf \r"\033[93m>> %s"' % export[0]
            e = 0

        read_log = log_file.read()
        time.sleep(0.5)
        os.system(com)
    date = dt.datetime.now()
    if successfully in read_log:
        com = 'printf \r"\033[93m\033[1m>> Export done.\n\033[92m\033[1m>> Dump generated successfully! :D  @ [ %s ]\n>> Dump File: %s \033[0m\n"' %(date, connect.DMP_FOLDER + filename.replace(".log",".dmp"))
        os.system(com)
    elif warning in read_log:
        com = 'printf \r"\033[93m\033[1m>> Dump generated with warnings! :O  @ [ %s ]\n>> Please check log: %s  \033[0m\n"' % (date,connect.DMP_FOLDER + filename)
        os.system(com)
    else:
        com = 'printf \r"\033[91m\033[1m>> Dump generated with errors! :(  @ [ %s ]\n>> Please check log: %s \033[0m\n"' % (date, connect.DMP_FOLDER + filename)
        os.system(com)



    log_file.close()

def create_name(name, version, number, path):

    if name in path:
        list_dump = name.split("_")
        index_bpt_ver = [i for i, s in enumerate(list_dump) if "BPT" in s][0]
        list_dump[index_bpt_ver] =  "BPT" + str(number) + "v" + str(version)
        name = "_".join(list_dump)
        return create_name(name, version+1, number, path)
    else:
        batcmd = sql_stringconn(connect.SA, "getActiveOwner.sql") #"SA/SA@dbt3epct04:1521/EPCMCRM4 @getActiveOwner.sql"

        status, output = commands.getstatusoutput(batcmd)
        if connect.SAREF1 in output:
            com = exp_stringconn(connect.SAREF1, name)
            return os.system(com)
        elif connect.SAREF2 in output:
            com = exp_stringconn(connect.SAREF2, name)
#            print com
            os.popen(com)
            created_files = os.listdir("/tefuser2/tef/crm/tefcrm78/dmp/")
            while name not in created_files:
        #        print "."
                created_files = os.listdir("/tefuser2/tef/crm/tefcrm78/dmp/")
            else:
                return exporting(name.replace(".dmp", ".log"))


def exp_stringconn(user, dump_name):
    log_name = dump_name.replace(".dmp", ".log")
    if user == connect.SAREF1:
        return "nohup exp %s/%s@%s file=%s%s %s log=%s%s compress=n buffer=409600000 feedback=10000 statistics=none > /dev/null 2> /dev/null &" %(connect.SAREF1, connect.SAREF1, connect.SID, connect.DMP_FOLDER, dump_name, connect.TABLES_PAR, connect.DMP_FOLDER, log_name)
    elif user == connect.SAREF2:
        return "nohup exp %s/%s@%s file=%s%s %s log=%s%s compress=n buffer=409600000 feedback=10000 statistics=none > /dev/null 2> /dev/null &" %(connect.SAREF2, connect.SAREF2, connect.SID, connect.DMP_FOLDER, dump_name, connect.TABLES_PAR, connect.DMP_FOLDER, log_name)

def sql_stringconn(user, script):
    if script != "":
        if user == connect.SAREF1:
            return "sqlplus -s %s/%s@%s:%s/%s @%s" %(connect.SAREF1, connect.SAREF1, connect.HOST, connect.PORT, connect.SID, script)
        elif user == connect.SAREF2:
            return "sqlplus -s %s/%s@%s:%s/%s @%s" %(connect.SAREF2, connect.SAREF2, connect.HOST, connect.PORT, connect.SID, script)
        elif user == connect.SA:
            return "sqlplus -s %s/%s@%s:%s/%s @%s" %(connect.SA, connect.SA, connect.HOST, connect.PORT, connect.SID, script)
            
class connect:
    DMP_FOLDER = "$HOME/dmp/"
    SAREF1 = "SAREF1"
    SAREF2 = "SAREF2"
    SA = "SA"
    HOST = "dbt3epct04"
    PORT = "1521"
    SID= "EPCMCRM4"
    TABLES_PAR = "parfile=ref_tables_list.par"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system("clear")
print;bcolors.HEADER +  '+###############################+'
print;bcolors.HEADER +  '#  CRM ENV 78 - DUMP GENERATOR  #'
print;bcolors.HEADER +  '#                               #'
print;bcolors.HEADER +  '#     %s ------------------%s       #' %(bcolors.FAIL,bcolors.HEADER)
print bcolors.HEADER +  '#     %s| Enter -1 to exit |%s      #' %(bcolors.FAIL,bcolors.HEADER)
print bcolors.HEADER +  '#     %s ------------------%s       #' %(bcolors.FAIL,bcolors.HEADER)
print bcolors.WARNING +  '#                               #'
print bcolors.WARNING +  '#-------------------------------#'
print bcolors.WARNING +  '#                               #'
print bcolors.WARNING + '# Si  se  ingresa  el  mismo    #'
print bcolors.WARNING + '# Nro. Dump se creara una nueva #'
print bcolors.WARNING + '# version  del  archivo  .dmp   #'
print bcolors.WARNING +  '#                               #'
print bcolors.WARNING +  '#------------------------------ #'
print bcolors.WARNING +  '#                               #'
print bcolors.WARNING +  '# con %s"dmps"%s se va a la carpeta #' %(bcolors.BOLD,bcolors.ENDC+bcolors.WARNING)
print bcolors.WARNING +  '# contenedora de los dumps      #'
print bcolors.WARNING +  '#                               #'
print bcolors.WARNING + '+###############################+'

print bcolors.ENDC
# os.system("clear")
now_date = str(dt.date.today()).replace("-", ".")
list_dir = os.listdir("/tefuser2/tef/crm/tefcrm78/dmp/")
number = 0
if len(sys.argv) == 2:
        print ('Executing with parameters!!')
        number = sys.argv[1]
else:
        number = int(raw_input(">> Nro. Dump: "))
if number == -1:
    print "Exit!"
    exit()

dump = "EPCMCRM4_CRM_Phase3_SWP6_Dump_For_BPT%s_P3_%s.dmp" %(number, now_date)
print 'starting...'
create_name(dump, 2, number, list_dir)

time.sleep(120)

print 'end!'
