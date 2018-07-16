import math
import csv

cancer_data = []

with open('cancerdata.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        cancer_data.append(row)

data_train = cancer_data[0:450]
data_test = cancer_data[451:len(cancer_data)]

def calc_dist(test, train):
    dist = 0
    for i in range(1, len(test)-1):
        dist += math.sqrt((int(test[i]) - int(train[i])) ** 2)
    return(dist)

def train(test_data):
    correct = 0
    dist_data = []
    for num in range(0, len(data_train)):
        dist_data.append([calc_dist(test_data, data_train[num]), int(data_train[num][10])])
        sorted_list = sorted(dist_data, key=lambda x: x[0])

    if sorted_list[0][1] == int(test_data[10]):
        return("Match")
    else:
        return("Not match")
    
correct = 0

for val in range(0, len(data_test)):
    if train(data_test[val]) == "Match":
        correct += 1
    else:
        print("Not match")

accuracy = correct / len(data_test)

print(f"The accuracy is {accuracy * 100}%")
