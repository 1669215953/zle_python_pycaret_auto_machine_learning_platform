import json
import csv


def parse_json(inflie=r"D:/codeprogram/教学/data.json",outfile="data.csv"):
    with open(outfile, "w", newline="") as csvfile:
        with open(inflie, "r") as f:
            for line in f:
                if "totalcount" in line:
                    print("成功格式化该json文件")
                    break
                jsondata=json.loads(line) 
                jobinfos=jsondata["resultbody"]["job"]["items"]
                for job in jobinfos:
                        try:
                            jobName = job["jobName"]
                        except:
                            jobName = ''
                            print('no jobName')

                        try:
                            jobTags = job["jobTags"]
                        except:
                            jobTags = ''

                        try:
                            jobAreaString = job["jobAreaString"]
                        except:
                            jobAreaString = ''

                        try:
                            jobAreaLevelDetail = job["jobAreaLevelDetail"]
                        except:
                            jobAreaLevelDetail = ''

                        try:
                            provideSalaryString = job["provideSalaryString"]
                        except:
                            provideSalaryString = ''

                        try:
                            workYearString = job["workYearString"]
                        except:
                            workYearString = ''

                        try:
                            degreeString = job["degreeString"]
                        except:
                            degreeString = ''

                        try:
                            fullCompanyName = job["fullCompanyName"]
                        except:
                            fullCompanyName = ''

                        try:
                            companyTypeString = job["companyTypeString"]
                        except:
                            companyTypeString = ''

                        try:
                            companySizeString = job["companySizeString"]
                        except:
                            companySizeString = ''

                        try:
                            industryType1Str = job["industryType1Str"]
                        except:
                            industryType1Str = ''

                        try:
                            jobHref = job["jobHref"]
                        except:
                            jobHref = ''
                        data = [
                            [jobName, jobTags, jobAreaString, jobAreaLevelDetail, provideSalaryString, workYearString, degreeString,
                            fullCompanyName, companyTypeString, companySizeString, industryType1Str, jobHref]
                            ]
                        writer = csv.writer(csvfile)

                        # 写入数据行
                        writer.writerows(data)
                    
parse_json()
