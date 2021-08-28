import json
import codecs
import re

# Sample file
amazon_data = "./raw-public/amazon-com.txt"

# Result dictionary
result = {}
case = 0
fields = ['date', 'title', 'links', 'duration', 'planned', 'causes', 'implications', 'fixes']

with codecs.open(amazon_data, 'r', encoding='utf-8', errors='ignore') as ad:
    while True:
        line = ad.readline()
        if not line:
            break

        if re.search("^\d{2}\/\d{2}\/\d{4}", line):
            case += 1
            entry = {}
            entry[fields[0]] = line.strip()
            line = ad.readline()
            entry[fields[1]] = line.strip()

            links = []
            line = ""
            while True:
                line = ad.readline()
                if re.search("^http", line):
                    link = {}
                    link["url"] = line.strip()
                    links.append(link)
                else:
                    break

            entry[fields[2]] = links
            
            causes = []
            implications = []
            fixes = []
            planned = ""
            duration = ""
            while True:
                if re.search("^r", line):
                    cause = {}
                    cause["cause"] = line.strip()[2:]
                    causes.append(cause)
                    line = ad.readline()
                elif re.search("^p", line):
                    planned = line.strip()[2:]
                    line = ad.readline()
                elif re.search("^i", line):
                    implication = {}
                    implication["implication"] = line.strip()[2:]
                    implications.append(implication)
                    line = ad.readline()
                elif re.search("^f", line):
                    fix = {}
                    fix["fix"] = line.strip()[2:]
                    fixes.append(fix)
                    line = ad.readline()
                elif re.search("^t", line):
                    duration = line.strip()[2:]
                    line = ad.readline()
                else:
                    break

            entry[fields[3]] = duration
            entry[fields[4]] = planned
            entry[fields[5]] = causes
            entry[fields[6]] = implications
            entry[fields[7]] = fixes
        
            result["Case " + str(case)] = entry

out_file = open("test.json", "w")
json.dump(result, out_file, indent = 4)
out_file.close()
