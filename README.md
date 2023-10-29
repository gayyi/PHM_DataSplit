# PHM_DataSplit
Split raw data in PHM RUL dataset in a reasonable way, prepared for further development in RUL prediction.
Gayyi is a freshman in github and python programming. He establishes this project mainly for having a try on the use of Github.

# Intro
The data_split file serves to split the data in PHM RUL data set, this prevalent open source data set is collected by FEMTO-ST and was
utilized as the learning and test data set in a challenging competition in 2012. You can easily get access to detail informations on 
https://github.com/Lucky-Loek/ieee-phm-2012-data-challenge-dataset.

# Why this is created
As a junior student in UESTC, I joined a laboratory, working on designing specified NPU to diagnose fault in running machines and predicting their remaining useful life. Spliting PHM data set through a reasonable way is a task assgined by my junior supervisor.
During the process of processing data, I found format error in some .csv files and also I learned how to split the data in PHM into subsets according to the working conditions specified on the official website. I establish this repository mainly for commemorate my struggling age in my third year in college and I hope people see my word can give your valuble advice and point out my mistakes or shortcomings in codes.

# Function of code
1. "demo_fix_error"
When processing the PHM data, I found problems in its .csv files and "demo_fix_error.py" file is used to fix errors in .csv files. The error is that, some of the acc.csv files should have 6 columns but they werenot. 6 colums of data was squeeze into one columns and all stored in the first columns, divided by semicolon ";".
2. "data_split"
The main task was to split the data. The PHM data record the acceleration changes and temperatuer vibrations of bearings the on the experiment platform, so that people can predict the RUL of these bearings by analysing their vibration features. According to the arrangement of data, I first merge all data in Learning data set and Test data set(for they can both be taken as raw data) and store them in Full data set. Followng that, I divided the merged data in accordance with their working condition(Distinguished by "Bearing1", "Bearing2", "Bearing3"), within 'channel1' and 'channel2', the acceleration in the horizontal and verticle direction are stored. The data is transformed to .py format.
3. "rawdata_github"
This file is to download the rawdata from the website.
