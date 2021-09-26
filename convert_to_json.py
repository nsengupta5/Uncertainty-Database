import json
import os
import codecs
import re

def convert_to_time(duration):
    if duration == "unk":
        return -1

    total_min = 0
    d_index = duration.find('d')
    if d_index != -1:
        if d_index == 1:
            total_min += int(duration[0]) * 1440
        else:
            total_min += int(duration[0:2]) * 1440
    h_index = duration.find('h')
    if h_index != -1:
        if duration[h_index-2:h_index].isdigit():
            total_min += int(duration[h_index-2:h_index]) * 60
        else:
            total_min += int(duration[h_index-1:h_index]) * 60
    m_index = duration.find('m')
    if duration[m_index-2:m_index].isdigit():
        total_min += int(duration[m_index-2:m_index])
    else:
        total_min += int(duration[m_index-1:m_index])
    return total_min

def main():
    directory = "./raw-public/txt-files"

    total_result = {}

    for files in os.listdir(directory):
        file = os.path.join(directory, files)
        if os.path.isfile(file):

            # Result dictionary
            result = {}
            entries = []
            case = 0
            fields = ['date', 'title', 'links', 'duration', 'planned', 'causes', 'implications', 'fixes']

            with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as ad:
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
                                tmp = line.strip()[2:]
                                duration = convert_to_time(tmp)
                                line = ad.readline()
                            else:
                                break

                        entry[fields[3]] = duration
                        entry[fields[4]] = planned
                        entry[fields[5]] = causes
                        entry[fields[6]] = implications
                        entry[fields[7]] = fixes

                        entries.append(entry)
                        result["Case " + str(case)] = entry

            total_result[file[:-4]] = entries
            out_file = open(file[:-4] + ".json", "w")
            json.dump(result, out_file, indent = 4)
            out_file.close()

    out_file = open("total_aggregate.json", "w")
    json.dump(total_result, out_file, indent = 4)
    out_file.close()

if __name__ == "__main__":
    main()
