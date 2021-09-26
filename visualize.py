import json
import matplotlib.pyplot as plt
import numpy as np

with open("raw-public/json-files/total_aggregate.json") as json_file:
    data = json.load(json_file)

total_durations = []
total_causes = []
total_implications = []
total_fixes = []
total_planned = []

causes = []
fixes = []
implications = []

causes_categories = ['admin', 'bug', 'cap', 'config', 'cross', 'fail', 'natdis', 'upgrade', 'sec', 'unk']
implications_categories = ['loss', 'down', 'op', 'perf', 'sec', 'stale', 'unk']
fixes_categories = ['maint', 'restart', 'fix', 'add', 'restore', 'cross']
planned_categories = ['Yes', 'No']

for values in data.values():
    for value in values:
        total_durations.append(value['duration'])
        total_planned.append(value['planned'])
        causes.append(value['causes'])
        implications.append(value['implications'])
        fixes.append(value['fixes'])

for cause in causes:
    entry = []
    if len(cause) != 0:
        for i in range(len(cause)):
            entry.append(cause[i]['cause'])
        total_causes.append(entry)
    else:
        total_causes.append(entry)

for fix in fixes:
    entry = []
    if len(fix) != 0:
        for i in range(len(fix)):
            entry.append(fix[i]['fix'])
        total_fixes.append(entry)
    else:
        total_fixes.append(entry)

for implication in implications:
    entry = []
    if len(implication) != 0:
        for i in range(len(implication)):
            entry.append(implication[i]['implication'])
        total_implications.append(entry)
    else:
        total_implications.append(entry)

config_duration_count = []
admin_duration_count = []
bug_duration_count = []
cap_duration_count = []
cross_duration_count = []
fail_duration_count = []
natdis_duration_count = []
upgrade_duration_count = []
sec_duration_count = []
unk_duration_count = []

for i in range(len(total_causes)):
    if not total_causes[i] == []: 
        if total_durations[i] != -1:
            for c in total_causes[i]:
                if c == 'config':
                    config_duration_count.append(total_durations[i])
                elif c == 'admin':
                    admin_duration_count.append(total_durations[i])
                elif c == 'bug':
                    bug_duration_count.append(total_durations[i])
                elif c == 'cap':
                    cap_duration_count.append(total_durations[i])
                elif c == 'cross':
                    cross_duration_count.append(total_durations[i])
                elif c == 'fail':
                    fail_duration_count.append(total_durations[i])
                elif c == 'natdis':
                    natdis_duration_count.append(total_durations[i])
                elif c == 'upgrade':
                    upgrade_duration_count.append(total_durations[i])
                elif c == 'sec':
                    sec_duration_count.append(total_durations[i])
                else:
                    unk_duration_count.append(total_durations[i])

config_count = 0
admin_count = 0
bug_count = 0
cap_count = 0
cross_count = 0
fail_count = 0
natdis_count = 0
upgrade_count = 0
sec_count = 0
unk_count = 0

for i in range(len(total_causes)):
    if not total_causes[i] == []: 
            for c in total_causes[i]:
                if c == 'config':
                    config_count += 1
                elif c == 'admin':
                    admin_count += 1
                elif c == 'bug':
                    bug_count += 1
                elif c == 'cap':
                    cap_count += 1
                elif c == 'cross':
                    cross_count += 1 
                elif c == 'fail':
                    fail_count += 1
                elif c == 'natdis':
                    natdis_count += 1
                elif c == 'upgrade':
                    upgrade_count += 1
                elif c == 'sec':
                    sec_count += 1
                else:
                    unk_count += 1

causes_duration = [sum(admin_duration_count), sum(bug_duration_count), sum(cap_duration_count), sum(config_duration_count), sum(cross_duration_count), sum(fail_duration_count), sum(natdis_duration_count), sum(upgrade_duration_count), sum(sec_duration_count), sum(unk_duration_count)]
plt.pie(causes_duration, labels = causes_categories, shadow = True)
plt.show()

cause_counts = [admin_count, bug_count, cap_count, config_count, cross_count, fail_count, natdis_count, upgrade_count, sec_count, unk_count]
plt.pie(cause_counts, labels = causes_categories, shadow = True)
plt.show()

planned_graph = [total_planned.count("yes"), total_planned.count("no")]
plt.pie(planned_graph, labels = planned_categories, shadow = True)
plt.show()
