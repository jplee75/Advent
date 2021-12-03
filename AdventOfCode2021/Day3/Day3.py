gamma_rate=0
epsilon_rate=0

def binaryToDecimal(n):

    return int(n,2)

def ExtractColumn(lst,column):

    return [item[column] for item in lst]

diagnostic_report=[]

with open(".\Input\Input3.txt","r") as input_file:

    while (line := input_file.readline().rstrip()):

        diagnostic_report.append(list(map(str,line)))


gamma_binary = []

epsilon_binary =[]

for row in diagnostic_report[0:1]:
    i=0
    for number in row:
        current_column = ExtractColumn(diagnostic_report,i)
        gamma_binary.append(max(current_column,key=current_column.count))
        epsilon_binary.append(min(current_column,key=current_column.count))
        i+=1


gamma_rate = binaryToDecimal("".join(gamma_binary))
epsilon_rate = binaryToDecimal("".join(epsilon_binary))
#print(gamma_rate)
#print(epsilon_rate)
#print(gamma_rate*epsilon_rate)

#part deux

life_support_rating=0
O2_gen_rating=0
CO2_scrub_rating=0

diagnostic_report_O2 = diagnostic_report.copy()
diagnostic_report_CO2 = diagnostic_report.copy()

for row in diagnostic_report[0:1]:
    i=0
    for number in row:
        if len(diagnostic_report_O2)>1:
            current_column_O2 = ExtractColumn(diagnostic_report_O2,i)
            O2_zero_count = current_column_O2.count('0')
            O2_one_count = current_column_O2.count('1')
            if O2_zero_count>O2_one_count:
                oxygen_filter = '0'
            else:
                oxygen_filter = '1'
            diagnostic_report_O2 = [x for x in diagnostic_report_O2 if x[i]==oxygen_filter]

        if len(diagnostic_report_CO2)>1:
            current_column_C02 = ExtractColumn(diagnostic_report_CO2,i)
            CO2_zero_count = current_column_C02.count('0')
            CO2_one_count = current_column_C02.count('1')
            if CO2_one_count<CO2_zero_count:
                co2_filter = '1'
            else:
                co2_filter = '0'
            diagnostic_report_CO2 = [x for x in diagnostic_report_CO2 if x[i]==co2_filter]

        i+=1


O2_gen_rating = binaryToDecimal("".join(diagnostic_report_O2[0]))
print(O2_gen_rating)
CO2_scrub_rating = binaryToDecimal("".join(diagnostic_report_CO2[0]))
print(CO2_scrub_rating)
life_support_rating = O2_gen_rating*CO2_scrub_rating
print(life_support_rating)