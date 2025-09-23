# py3
import os,lxml.builder,sys,time
class Scenario():    
    def __init__(self,path,name,timeout):
        self.path=path
        self.name=name
        self.timeout=timeout
    def build_scenario(self):
        E = lxml.builder.ElementMaker()
        scenario = E.scenario
        step = E.step
        the_doc=scenario()
        for i in os.listdir(self.path):
            if i == 'SoapTalkerScenario_Creator.py':
                continue
            if i == 'SoapParser.py':
                continue
            if i == 'BTSLog.xml':
                continue
            if i == 'UnitOAM_SOAP_Log.xml':
                continue
            the_doc.append(step(name=i[:-4],type='SOAP_SEND',set=self.name,timeout=self.timeout))
        f=open(s.name+'.xml', 'wb')
        f.write(lxml.etree.tostring(the_doc,pretty_print=True))
try:
    temp=[]
    for x in os.listdir('.'):
        temp.append(x)
    if len(temp) > 3:
        path=str(os.getcwd())
        name=str(os.path.basename(path))
        timeout='1000'
    s=Scenario(path,name,timeout)
    s.build_scenario()
except:
    print ("""Description:\nFill parameters: file location, scenario name, timeout. Remember to send it as a string like that -> 'exmaple'""")
    print ("It is also possible to copy paste script to folder with messages and reexecute it again")
    print ("""\nTemplate:
    Give me a file location where we could find all soaps: 'C:\\Sysmon_AZNCorAZNB'
    Give me a scenario name it have to be the same like folder with soaps: 'Sysmon_AZNCorAZNB'
    Give me a timeout in miliseconds which should be used: '500'""")

    path=input('\nGive me a file location where we could find all soaps: ')
    name=input('\nGive me a scenario name it have to be the same like folder with soaps: ')
    timeout=input('\nGive me a timeout in miliseconds which should be used: ')
    s=Scenario(path,name,timeout)
            
    ##s=Scenario('C:\\Sysmon_AZNCorAZNB','Sysmon_AZNCorAZNB','500',)
    s.build_scenario()
print ('\nDone. Have fun with SoalpTalker. You have to create folder in C:\SoapTalker 1.4.2\scenarios\.\nThe name of folder have to be the same like scenario name.\nFolder with messages have to exist here: C:\SoapTalker 1.4.2\messages')
