import csv

with open('profiles.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['user'])
        # if 'user' in line['user']:
        #     print('yes')

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['user', 'password']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)