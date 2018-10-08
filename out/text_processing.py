

def write_wdbc_GA_stats():
	with open("WDBC_GA_avg_stats_fewer_its.csv", 'a') as write_f_avg:
		write_f_avg.write("Population, Crossover, Mutate, Iteration, Train Accuracy Avg, Test Accuracy Avg, Train Time Avg, Train Accuracy Best, Test Accuracy Best, Train Time Best\n")
		with open("WDBC_GA_stats_fewer_its.csv", 'a') as write_f:
			write_f.write("Population, Crossover, Mutate, Iteration, Trial Num, Train Accuracy, Test Accuracy, Train Time\n")
			with open("WDBC_GA_fewer_iterations.txt") as f:
				iteration = ""
				trial_num = ""
				train_acc = ""
				test_acc = ""
				train_time = ""
				pop = ""
				crossover = ""
				mutation = ""
				train_acc_avg = []
				test_acc_avg = []
				train_time_avg = []
				count = 0
				for line in f:
					line = line.strip('\n')
					if "Trial" in line:
						trial_line = line.split("#")
						trial_num = str(int(trial_line[1]) + 1)
					if "Iteration" in line:
						iteration_line = line.split("#")
						iteration = (iteration_line[1])
					if "Train Accuracy" in line:
						line.replace(" ", "")
						acc_line = line.split(":")
						train_acc = (acc_line[1])
						train_acc_avg.append(float(acc_line[1]))
					if "Test Accuracy" in line:
						line.replace(" ", "")
						acc_line = line.split(":")
						test_acc = (acc_line[1])
						test_acc_avg.append(float(acc_line[1]))
						count += 1
					if "Train Time" in line:
						line.replace(" ", "")
						acc_line = line.split(":")
						train_time = (acc_line[1])
						train_time_avg.append(float(acc_line[1]))
					if "GA" in line:
						sa_line = line.split("_")
						pop = (sa_line[1])
						crossover = (sa_line[2])
						mutation = sa_line[3]
					if "Test Time" in line:
						if count == 3:
							avg_time = sum(train_time_avg)/3
							avg_test = sum(test_acc_avg)/3
							avg_train = sum(train_acc_avg)/3
							write_f_avg.write(pop + "," + crossover + "," + mutation + "," + iteration + "," + str(avg_train) + "," + str(avg_test) + "," + str(avg_time) + "," + str(max(train_acc_avg)) + "," + str(max(test_acc_avg)) + "," + str(min(train_time_avg)) + "\n")
							count = 0
							train_time_avg.clear()
							test_acc_avg.clear()
							train_acc_avg.clear()
						write_f.write(pop + "," + crossover + "," + mutation + "," + iteration + "," + trial_num + "," + train_acc + "," + test_acc + "," + train_time + "\n")



def write_wdbc_SA_stats():
	with open("WDBC_SA_avg_stats.csv", 'a') as write_f_avg:
		write_f_avg.write("Initial Temp, Cooling Rate, Iteration, Train Accuracy Avg, Test Accuracy Avg, Train Time Avg, Train Accuracy Best, Test Accuracy Best, Train Time Best\n")
		with open("WDBC_SA_stats.csv", 'a') as write_f:
			write_f.write("Initial Temp, Cooling Rate, Iteration, Trial Num, Train Accuracy, Test Accuracy, Train Time\n")
			with open("WDBC_SA_stats.txt") as f:
				iteration = ""
				trial_num = ""
				train_acc = ""
				test_acc = ""
				train_time = ""
				temp = ""
				cooling_rate = ""
				train_acc_avg = []
				test_acc_avg = []
				train_time_avg = []
				count = 0
				for line in f:
					line = line.strip('\n')
					if "Trial" in line:
						trial_line = line.split("#")
						trial_num = str(int(trial_line[1]) + 1)
					if "Iteration" in line:
						iteration_line = line.split("#")
						iteration = (iteration_line[1])
					if "Train Accuracy" in line:
						line.replace(" ", "")
						acc_line = line.split(":")
						train_acc = (acc_line[1])
						train_acc_avg.append(float(acc_line[1]))
					if "Test Accuracy" in line:
						line.replace(" ", "")
						acc_line = line.split(":")
						test_acc = (acc_line[1])
						test_acc_avg.append(float(acc_line[1]))
						count += 1
					if "Train Time" in line:
						line.replace(" ", "")
						acc_line = line.split(":")
						train_time = (acc_line[1])
						train_time_avg.append(float(acc_line[1]))
					if "SA" in line:
						sa_line = line.split("_")
						temp = (sa_line[1])
						cooling_rate = (sa_line[2])
					if "Test Time" in line:
						if count == 3:
							avg_time = sum(train_time_avg)/3
							avg_test = sum(test_acc_avg)/3
							avg_train = sum(train_acc_avg)/3
							write_f_avg.write(temp + "," + cooling_rate + "," + iteration + "," + str(avg_train) + "," + str(avg_test) + "," + str(avg_time) + "," + str(max(train_acc_avg)) + "," + str(max(test_acc_avg)) + "," + str(min(train_time_avg)) + "\n")
							count = 0
							train_time_avg.clear()
							test_acc_avg.clear()
							train_acc_avg.clear()
						write_f.write(temp + "," + cooling_rate + "," + iteration + "," + trial_num + "," + train_acc + "," + test_acc + "," + train_time + "\n")

write_wdbc_GA_stats()

