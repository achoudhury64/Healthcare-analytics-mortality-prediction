# Healthcare-analytics-mortality-prediction

We you will use clinical data as raw input to perform Mortality Prediction.
The data provided in events.csv are event sequences. Each line of this file consists of a tuple with the format (patient id, event id, event description, timestamp, value).

Descriptive Statistics 
Before starting analytic modeling, it is a good practice to get descriptive statistics of the input raw data. In this section, you need to write code that computes various metrics on the data described previously. A skeleton code is provided to you as a starting point.
The definition of terms used in the result table are described below:
• Event count: Number of events recorded for a given patient. Note that every line in the input file is an event.
• Encounter count: Count of unique dates on which a given patient visited the hospital. All the events - DIAG, LAB and DRUG - should be considered as hospital visiting events.
• Record length: Duration (in number of days) between the first event and last event for a given patient.
    
For example, if the first event is on 2014-05-21 and the last event is on 2014-05-24, the duration is 3 days. If a patient has only one event, the duration is 0.

Feature construction
It is a common practice to convert raw data into a standard data format before running real machine learning models. Observation Window: The time interval you will use to identify relevant events. Only events present in this window should be included while constructing feature vectors. The size of observation window is 2000 days inclusively, i.e., includes the index day and day of index date - 2000.
• Prediction Window: A fixed time interval that is to be used to make the prediction. Events in this interval should not be included in constructing feature vectors. The size of prediction window is 30 days inclusively.
• Index date: The day on which mortality is to be predicted. Index date is evaluated as follows:
– For deceased patients: Index date is 30 days prior to the death date (timestamp field) in data/train/mortality events.csv.
– For alive patients: Index date is the last event date in data/train/events.csv for each alive patient.

Filter events 
Consider an observation window (2000 days) and prediction window (30 days). Remove the events that occur outside the observation window.

Aggregate events
To create features suitable for machine learning, we will need to aggregate the events for each patient as follows:
• sum values for diagnostics and medication events (i.e. event id starting with DIAG and DRUG).
• count occurences for lab events

Further, in machine learning algorithm like logistic regression, it is important to normalize different features into the same scale using an approach like min-max normalization (hint: if x is a value of a feature for one patient, we define min(x) is always 0, and max(x) to be the largest value of that feature, thus, the scale equation become x/max(x)).
