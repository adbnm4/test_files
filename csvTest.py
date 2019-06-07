import csv

with open('profiles.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['user'])
        # if 'user' in line['user']:
        #     print('yes')

    with open('profiles.csv', 'a+', newline='') as new_file:
        fieldnames = ['user', 'password']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writerow({'user': 'user6', 'password': 'password6'})
