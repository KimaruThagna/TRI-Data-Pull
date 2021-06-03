# YourStake Take Away Exercise
**Purpose**:
Pull data from TRI websites and generate a CSV file with companies, facilities and air pollution data
# Script Structure and Purpose
1. `get_states_list.py`- Get all the states from the interface using selenium. This will allow automated looping and getting data for all states

2. `data_pull.py`- Pull and download actual excel files from site using Selenium. Save to `data/` folder
3. `data_processing.py`- Refining of the excel data to get the results we want. Filter out only air pollution
data, use `find_parent_company.py` script to find the parent company name using selenium and finally, sort the records and save to `final_output/` as csv denoted with current **date_time**

# Challenges and work arounds
1. Intermittent Popups- The site had some popups displaying intermittently(no consistency) To work
around this, I implemented a try-catch block with the `TimeoutException`. This allows the program to gracefully handle the presence or absence of the popup
2. Long and non deterministic loading times between tasks- The website takes quite a while to load the
search facility and also results. This leads to unnecessary timeouts. To navigate this, I used Python's `time.sleep()` function to wait an arbitrary amount of time before executing a click or navigation. This is however to the detriment of program speed. The load time is also arbitrary. I was not able to find a near exact number of seconds the data took. For example, retrieving data for the state of **American Samoa** took longer than the rest.
3. Parent Company Data not readily available- This had to be fetched from another page designated by the `TRID`. This therefore required severl selenium executions equal to the number of unique TRIDs available.
4. Parent Company name is not Guaranteed- Upon loading of the facility details page, The parent company name is not always guaranteed. Since there is seemingly no other way to get this data, the parent company column in the CSV is recorded as NA. 

I have used this to be consistent with the site. In the absence of the name, NA is displayed on the table. A possible heuristic might involve deriving the parent company name from the facility name. Looking at the data, there are several facility names that have the parent name in them. 

5. Inconsistent facility column in dataset- To derive the TRID from the dataset, I am splitting the facility name by the hyphen(-) and getting the TRID. The naming is however inconsistent since some facility names have hyphens in them. The work around for this is choosing the last item in the `split()` list since you are assured that this is the TRID. The final cleanup involves stripping whitespaces that are present.

# Making Code Robust to run unsupervised

Below are techniques and tools I would use to ensure the script doesnt fail or if it does, 
it is fault tolerant.
1. Automated workflows with failure management- For this, I would use a tool such as **APACHE AIRFLOW**.
Its ability to manage workflows in a preset order, trigger automatic retries in case of failure and also event notification would be ideal for this use case.
The task dependency would be as described below
```
get_states_list>>data_pull>>[data_processing,find_parent_company]>>env_cleanup
**there would be an xcom push from get_states_list to data_pull
```

2. Anticipate changes in website structure- HTML elements may change but the most reliable item to use in finding elements is most likely the ID. For this reason, as a principle I try to use the element ID first then the link_text in the absence of the ID.
3. Anticipate longer wait periods from website- Since the website is an aggregation site, it is expected that over time as more data is aggregated, loading time may be longer unless the host implements better strategies. For this, the work around currently is an arbitrary `time.sleep()` but it would be more robust implementing an async type of wait. Selenium's `wait_until` does not seem to peform as expected with this site's long loading times.

# Quality Checks
Below are checks that I would test my script against when putting it into a web app.


- That the task runs as a scheduled background task. It takes quite a while anc hence should run in the background.
- All operations likely to fail are in try catch blocks with appropriate exceptions.
- Minimizing the `find_parent_company` task by finding the unique TRIDs from a downloaded dataset first instead of looping through entire dataset.