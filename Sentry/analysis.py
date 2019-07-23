import sentry_sdk  # Importing sentry

import csv
import statistics

records = []
total = []
hos_code = "4321"
payer_slade_code = "457"


# Introducing delibearate issue
division_by_zero = 1 / 0


while True:
    gender = str(input("Key \"M\" for Male and \"F\" for Female  "))
    if gender in ["F", "M"]:
        break


with open('claims_data.csv') as f:
    reader = csv.reader(f, delimiter="|")

    print("\nFETCHING DATA...\n")
    All_clients = []
    for row in reader:

        if row[2] == hos_code and row[1] == gender and row[4] == payer_slade_code:
            ttl = row[6]

            total.append(float(ttl))
            All_clients.append(row)

total.sort()
total_sum = sum(total)
Median = statistics.median(total)
Mean = sum(total) / len(total)
Standard_Deviation = statistics.stdev(total)

high_outliers = []
low_outliers = []
for i in All_clients:
    if float(i[6]) > (Mean + (2 * Standard_Deviation)):
        outlier = i[0]
        high_outliers.append(outlier)

    elif float(i[6]) < (Mean - (2 * Standard_Deviation)):
        outlier = i[0]
        low_outliers.append(outlier)

print("The total summation for all {} in {} is {} \n".format(
    gender, payer_slade_code, total_sum))
print("The Median for all {} in {} is {} \n".format(
    gender, payer_slade_code, Median))
print("The Mean for all {} in {} is {} \n".format(
    gender, payer_slade_code, Mean))
print("The Standard Deviation for all {} in {} is {} \n".format(
    gender, payer_slade_code, Standard_Deviation))
print("The Highest Outlier for {} is in {} {} \n".format(
    gender, payer_slade_code, high_outliers[-5:]))
print("The Low Outliers for {} in {} is {} \n".format(
    gender, payer_slade_code, low_outliers[-5:]))
