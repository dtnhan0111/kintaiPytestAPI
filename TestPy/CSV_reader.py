import csv
import json


def account_test():
    with open('Account/STG_account_role.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        staff_id = []
        company_code = []
        password = []
        for row in csv_reader:
            # if line_count == 0:
            #     staff_id[row] = row[row]
            #     line_count += 1
            # else:
            #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            #     line_count += 1
            staff_id.append(row[0])
            company_code.append(row[1])
            password.append(row[2])
    return staff_id, company_code, password

