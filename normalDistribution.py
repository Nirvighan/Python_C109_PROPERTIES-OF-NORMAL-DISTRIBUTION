import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")

height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

print(height_list)
print(weight_list)

# MEAN,MEDIAN AND MODE  FOR HEIGHT AND WEIGHT

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

# PRINT MEAN , MEDIAN AND MODE FOR HEIGHT

print("MEAN , MEDIAN AND MODE FOR HEIGHT IS {},{} AND {} RESPECTIVELY".format(height_mean,height_median,height_mode))

# PRINT MEAN , MEDIAN AND MODE FOR WEIGHT

print("MEAN , MEDIAN AND MODE FOR WEIGHT IS {},{} AND {} RESPECTIVELY".format(weight_mean,weight_median,weight_mode))


# CALCULATE STANDARD DEVIATION FOR HEIGHT AND WEIGHT

height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)

# 1,2 AND 3 STANDARD DEVIATIONS FOR HEIGHT

height_1_std_deviation_start,height_1_std_deviation_end = height_mean-height_std_deviation,height_mean+height_std_deviation
height_2_std_deviation_start,height_2_std_deviation_end = height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_3_std_deviation_start,height_3_std_deviation_end = height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)

# 1,2 AND 3 STANDARD DEVIATIONS FOR WEIGHT

weight_1_std_deviation_start,weight_1_std_deviation_end = weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_2_std_deviation_start,weight_2_std_deviation_end = weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_3_std_deviation_start,weight_3_std_deviation_end = weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)

print(weight_1_std_deviation_start)
print(weight_1_std_deviation_end)
# % OF DATA WITHIN 1,2 AND 3 STANDARD DEVIATIONS FOR HEIGHT

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_1_std_deviation_start and result < height_1_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_2_std_deviation_start and result < height_2_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_3_std_deviation_start and result < height_3_std_deviation_end]

print(len(height_list_of_data_within_1_std_deviation))
# % OF DATA WITHIN 1,2 AND 3 STANDARD DEVIATIONS FOR WEIGHT

weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_1_std_deviation_start and result < weight_1_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_2_std_deviation_start and result < weight_2_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_3_std_deviation_start and result < weight_3_std_deviation_end]


# PRINT THE DATA
print("{}% OF DATA FOR HEIGHT LIES WITHIN 1 STANDARD DEVIATION ".format(len(height_list_of_data_within_1_std_deviation)* 100/len(height_list)))
print("{}% OF DATA FOR HEIGHT LIES WITHIN 2 STANDARD DEVIATION ".format(len(height_list_of_data_within_2_std_deviation)* 100/len(height_list)))
print("{}% OF DATA FOR HEIGHT LIES WITHIN 3 STANDARD DEVIATION ".format(len(height_list_of_data_within_3_std_deviation)* 100/len(height_list)))

print("{}% OF DATA FOR WEIGHT LIES WITHIN 1 STANDARD DEVIATION ".format(len(weight_list_of_data_within_1_std_deviation)* 100/len(weight_list)))
print("{}% OF DATA FOR WEIGHT LIES WITHIN 2 STANDARD DEVIATION ".format(len(weight_list_of_data_within_2_std_deviation)* 100/len(weight_list)))
print("{}% OF DATA FOR WEIGHT LIES WITHIN 3 STANDARD DEVIATION ".format(len(weight_list_of_data_within_3_std_deviation)* 100/len(weight_list)))


