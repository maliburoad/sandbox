# version 2023.08.01
# grzegorz.ros.ext@rfswtest.com

import re
import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

home_folder = Path("C:/SOAPTALKER")
who = ["BTS_OM", "BTS_OM_master_0", "BTS_OM_master_1"]

def main():
    folder_name = input("Please provide scenario name: ")

    file = getXmlFromDirectory()
    print("File name to slice: " + file)
    file = open(file)
    fileStr = file.read()
    soap_slice(fileStr, folder_name)
    if not os.path.exists('Soaps'):
        os.makedirs('Soaps')
    src_soap = Path(os.getcwd()) / "Soaps" /folder_name
    dst_soap = home_folder / "messages" / folder_name
    print("Output folders:")
    print(src_soap)
    print(dst_soap)
    shutil.copytree(src_soap, dst_soap)
    Goodbye=input("Press any button to exit")
    return None
def getXmlFromDirectory():
    xml_list=[]
    for file in os.listdir():
                if re.search('\.xml$', file):
                    xml_list.append(file)
    return xml_list[0]

def getOperation(xmlBody):
    modifyParameterReq = xmlBody.find('modifyParameterReq')
    if (modifyParameterReq == None):
        return ""
    managedObject = modifyParameterReq.find('managedObject')
    if (managedObject != None):
        operation = managedObject.find('operation').text
        if (operation == 'update_parm'):
            parameter = managedObject.find('parameter')
            name = parameter.find('parameterName').text + parameter.find('newValue').text
        else:
            name = operation
        name += "_" + managedObject.get('distName')
        return name.replace(":", "_")
    return ""

def soap_slice(fileStr,folder_name):
    openTag = '<SOAP-ENV:Envelope'
    endTag = '</SOAP-ENV:Envelope>'
    endTagSize = len(endTag)
    endIndex = 0
    notEndOfFile = True
    soapNr = 1


    while (notEndOfFile):
        beginIndex =  fileStr.find(openTag, endIndex)
        endIndex = fileStr.find(endTag, endIndex+1)
    #	print (beginIndex, endIndex)
        if (beginIndex != -1) and (endIndex != -1):
            soapMessage = fileStr[beginIndex:endIndex + endTagSize]
            root = ET.fromstring(soapMessage)
            header = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Header')
            sender = header.find('from').text
    #		print (sender)
            if (sender != None):
                if sender in who:
                    if not os.path.exists(Path("Soaps") / folder_name):
                        os.makedirs(Path("Soaps") / folder_name)
                    body = root.find('{http://schemas.xmlsoap.org/soap/envelope/}Body')
                    if (body.find('moduleReadyInd') == None):
                        operation = getOperation(body)
                        fileName = str(soapNr).zfill(3) + "_" + operation + ".xml"
                        file = open(Path("Soaps") / folder_name / fileName, 'w')
                        file.write(soapMessage)
                        soapNr = soapNr + 1
        else:
            print (str(soapNr-1) + " SOAPs created")

            notEndOfFile = False
    return None

if __name__ == '__main__':
    main()
