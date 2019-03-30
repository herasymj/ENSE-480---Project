import csv


with open('creditcard.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    count = 0
    for row in csvReader:
        if count == 0:
            continue
        new_transaction = Transaction(
            time=row[0],
            v1=row[1],
            v2=row[2],
            v3=row[3],
            v4=row[4],
            v5=row[5],
            v6=row[6],
            v7=row[7],
            v8=row[8],
            v9=row[9],
            v10=row[10],
            v11=row[11],
            v12=row[12],
            v13=row[13],
            v14=row[14],
            v15=row[15],
            v16=row[16],
            v17=row[17],
            v18=row[18],
            v19=row[19],
            v20=row[20],
            v21=row[21],
            v22=row[22],
            v23=row[23],
            v24=row[24],
            v25=row[25],
            v26=row[26],
            v27=row[27],
            v28=row[28],
            amount=row[29],
            fraud=row[30]
        )
        print(str(count))
        count += 1
