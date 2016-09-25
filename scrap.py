import requests
import random

def getStudentInfo(id):
	# http://www.neaea.gov.et/Student/StudentDetail?admissionNumber=761168&_=1474836467444
	return requests.get("http://www.neaea.gov.et/Student/StudentDetail?admissionNumber=" + str(id) + "&_=" + str(random.randint(1000000000000,9900000000000))).text

def write2File(text, filename):
	text_file = open(filename, "w")
	text_file.write(text)
	text_file.close()

write2File (getStudentInfo(762650))