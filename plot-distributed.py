import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm


def process_dict(benchmark_data_dict):
    # Go stores benchmark results in nanoseconds. Convert all results to seconds.
    benchmark_data_dict['time'] /= 1e+9

    # Use the name of the benchmark to extract the number of worker threads used.
    #  e.g. "Filter/16-8" used 16 worker threads (goroutines).
    # Note how the benchmark name corresponds to the regular expression 'Filter/\d+_workers-\d+'.
    # Also note how we place brackets around the value we want to extract.
    benchmark_data_dict['threads'] = benchmark_data_dict['name'].str.extract(r'L/512x512x100-(\d+)-\d+').apply(pd.to_numeric)
    benchmark_data_dict['cpu_cores'] = benchmark_data_dict['name'].str.extract(r'L/512x512x100-\d+-(\d+)').apply(pd.to_numeric)


if __name__ == '__main__':
    # Read in the saved CSV data.
    # my_font = fm.FontProperties(fname="/usr/share/fonts/wqy-microhei/wqy-microhei.ttc")
    benchmark_1_server = pd.read_csv('results-1s.csv', header=0, names=['name', 'time', 'range'])
    benchmark_2_server = pd.read_csv('results-2s.csv', header=0, names=['name', 'time', 'range'])
    benchmark_3_server = pd.read_csv('results-3s.csv', header=0, names=['name', 'time', 'range'])
    process_dict(benchmark_1_server)
    process_dict(benchmark_2_server)
    process_dict(benchmark_3_server)

    print(benchmark_1_server)
    print("\n")
    print(benchmark_2_server)
    print("\n")
    print(benchmark_3_server)

    # # Plot a bar chart.
    # ax = sns.barplot(data=benchmark_data, x='threads', y='time')
    #
    # # Set descriptive axis lables.
    # ax.set(xlabel='Worker threads used', ylabel='Time taken (s)')

    # Display the full figure.
    x = range(len(benchmark_1_server))
    # fig, axes = plt.subplots(1, 1, figsize=(8, 4))
    ln1 = plt.plot(benchmark_1_server['threads'], benchmark_1_server['time'],
                   color='red', label="1 server", marker="x")
    ln2 = plt.plot(benchmark_2_server['threads'], benchmark_2_server['time'],
                   color='green', label="2 servers", marker="x")
    ln3 = plt.plot(benchmark_3_server['threads'], benchmark_3_server['time'],
                   color='blue', label="3 servers", marker="x")
    # plt.legend(handles=[ln1, ln2], labels=['old, without mod', 'receive randomly, without mod'])
    # ln1.set_label('Label via method')
    plt.legend()
    plt.show()
