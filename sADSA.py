import csv

mee = []

while True:
    liniya = input()
    if not liniya:
        break
    chast = liniya.split('_')
    if len(chast) != 4:
        continue

    who_met, appearance, place, result = chast

    if appearance == 'human':
        oc = len(who_met) + len(appearance) + len(place) + int(result)
        mee.append((place, who_met, result, oc))

with open('meeting.csv', mode='w', newline='') as a:
    d = csv.writer(a)
    d.writerow(['no', 'place', 'who_met', 'result', 'outcome'])

    for index, (place, who_met, result, outcome) in enumerate(mee, start=1):
        d.writerow([index, place, who_met, result, outcome])
