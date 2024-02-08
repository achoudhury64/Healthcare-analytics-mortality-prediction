import time
import pandas as pd
import numpy as np

# PLEASE USE THE GIVEN FUNCTION NAME, DO NOT CHANGE IT

def read_csv(filepath):
    '''
    TODO : This function needs to be completed.
    Read the events.csv and mortality_events.csv files. 
    Variables returned from this function are passed as input to the metric functions.
    '''
    events = pd.read_csv(filepath + 'events.csv')
    mortality = pd.read_csv(filepath + 'mortality_events.csv')

    return events, mortality

def event_count_metrics(events, mortality):
    '''
    TODO : Implement this function to return the event count metrics.
    Event count is defined as the number of events recorded for a given patient.
    '''
    combine = pd.merge(events, mortality, on='patient_id',how='left')
    #Filter the LOJ dataframe to those who are dead(label > 0)
    ############For dead###############################
    dead = combine[combine['label'] == 1]
    #print(combine)
    #Find the count of the patients who are dead
    count_dead =  dead.patient_id.nunique()
    #print("count of dead", count_dead)
    #Find the total events by dead patients (total lines of dataframe dead)
    total_dead = len(dead)
    #print("total_dead", total_dead)
    #Calculate avg_dead_event_count
    avg_dead_event_count = total_dead/count_dead
    print("avg_dead_event_count----->", avg_dead_event_count)
    #count of events for each dead patient and convert to dataframe
    dead_value_count= dead['patient_id'].value_counts()
    dead_value_count = dead_value_count.to_frame().reset_index()
    dead_value_count.columns = ['patient_id','count']
    #calculate max_dead_event_count and min_dead_event_count
    max_dead_event_count = dead_value_count['count'].max()
    min_dead_event_count = dead_value_count['count'].min()
    #print(dead_value_count)
    print("max_dead_event_count----->", max_dead_event_count)
    print("min_dead_event_count----->", min_dead_event_count)
    
    ############For alive###############################
    alive = combine[combine['label'] != 1]
    #Find the count of the patients who are alive
    count_alive =  alive.patient_id.nunique()
    #print("count of dead", count_dead)
    #Find the total events by dead patients (total lines of dataframe dead)
    total_alive = len(alive)
    #print("total_alive", total_alive)
    #Calculate avg_dead_event_count
    avg_alive_event_count = total_alive/count_alive
    print("avg_alive_event_count----->", avg_alive_event_count)
    #count of events for each alive patient and convert to dataframe
    alive_value_count= alive['patient_id'].value_counts()
    alive_value_count = alive_value_count.to_frame().reset_index()
    alive_value_count.columns = ['patient_id','count']
    #calculate max_alive_event_count and min_alive_event_count
    max_alive_event_count = alive_value_count['count'].max()
    min_alive_event_count = alive_value_count['count'].min()
    #print(alive_value_count)
    print("max_alive_event_count----->", max_alive_event_count)
    print("min_alive_event_count----->", min_alive_event_count)
    
    

    return min_dead_event_count, max_dead_event_count, avg_dead_event_count, min_alive_event_count, max_alive_event_count, avg_alive_event_count

def encounter_count_metrics(events, mortality):
    '''
    TODO : Implement this function to return the encounter count metrics.
    Encounter count is defined as the count of unique dates on which a given patient visited the ICU. 
    '''
    combine = pd.merge(events, mortality, on='patient_id',how='left')
    #Filter the LOJ dataframe to those who are dead(label > 0)
    ############For dead###############################
    
    dead = combine[combine['label'] == 1]
    #print(dead.columns.values)
    #Find the count of unique dates of hospital visits for each patient and convert ot dataframe
    dead_patient_count_hosp_visit = dead.groupby('patient_id').timestamp_x.nunique()
    dead_patient_count_hosp_visit = dead_patient_count_hosp_visit.to_frame().reset_index()
    dead_patient_count_hosp_visit.columns = ['patient_id','no_of_unique_timestamp']
    #For Average encounter count###########
    count_dead =  dead.patient_id.nunique() ##calculates the total dead patients
    sum_patient_unique = dead_patient_count_hosp_visit['no_of_unique_timestamp'].sum()
    avg_dead_encounter_count = sum_patient_unique/count_dead
    
    #for max_dead_encounter_count
    max_dead_encounter_count = dead_patient_count_hosp_visit['no_of_unique_timestamp'].max()
    
    #for min_dead_encounter_count
    min_dead_encounter_count = dead_patient_count_hosp_visit['no_of_unique_timestamp'].min()
    
    #print("count of dead", count_dead)
    #print("sum_patient_unique", sum_patient_unique)
    print("avg_dead_encounter_count----->", avg_dead_encounter_count)
    print("max_dead_encounter_count----->", max_dead_encounter_count)
    print("min_dead_encounter_count----->", min_dead_encounter_count)
    #return dead_patient_count_hosp_visit
    
    ############For alive###############################
    
    alive = combine[combine['label'] != 1]
    #print(alive)
    #Find the count of unique dates of hospital visits for each patient and convert ot dataframe
    alive_patient_count_hosp_visit = alive.groupby('patient_id').timestamp_x.nunique()
    alive_patient_count_hosp_visit = alive_patient_count_hosp_visit.to_frame().reset_index()
    alive_patient_count_hosp_visit.columns = ['patient_id','no_of_unique_timestamp']
    
    #For Average encounter count###########
    count_alive =  alive.patient_id.nunique() ##calculates the total alive patients
    sum_patient_unique = alive_patient_count_hosp_visit['no_of_unique_timestamp'].sum()
    avg_alive_encounter_count = sum_patient_unique/count_alive
    
    #for max_alive_encounter_count
    max_alive_encounter_count = alive_patient_count_hosp_visit['no_of_unique_timestamp'].max()
    
    #for min_alive_encounter_count
    min_alive_encounter_count = alive_patient_count_hosp_visit['no_of_unique_timestamp'].min()
    
    #print("count of dead", count_dead)
    #print("sum_patient_unique", sum_patient_unique)
    print("avg_alive_encounter_count----->", avg_alive_encounter_count)
    print("max_alive_encounter_count----->", max_alive_encounter_count)
    print("min_alive_encounter_count----->", min_alive_encounter_count)
    
   


    return min_dead_encounter_count, max_dead_encounter_count, avg_dead_encounter_count, min_alive_encounter_count, max_alive_encounter_count, avg_alive_encounter_count

def record_length_metrics(events, mortality):
    '''
    TODO: Implement this function to return the record length metrics.
    Record length is the duration between the first event and the last event for a given patient. 
    '''
    combine = pd.merge(events, mortality, on='patient_id',how='left')
    #Filter the LOJ dataframe to those who are dead(label > 0)
    
    ############For dead###############################
    
    dead = combine[combine['label'] == 1]
    #print(dead.columns.values)
    #print(dead)
    
    ###### Find the max date and min date for each dead patient Id
    df = dead.groupby(['patient_id'])
    dead_patient_min_max_date = df.agg(minimum_date=('timestamp_x', np.min), maximum_date=('timestamp_x', np.max))
    #Changing the index of the dataframe to column patient_id
    dead_patient_min_max_date.reset_index(inplace=True)
    dead_patient_min_max_date = dead_patient_min_max_date.rename(columns = {'index':'patient_id'})
    #Converting the max date and min date to date time format
    dead_patient_min_max_date['minimum_date'] = pd.to_datetime(dead_patient_min_max_date['minimum_date'])
    dead_patient_min_max_date['maximum_date'] = pd.to_datetime(dead_patient_min_max_date['maximum_date'])
    
    ###### Find the duration(days) of each patient id by subtracting the min date from max date
    dead_patient_min_max_date['duration'] = dead_patient_min_max_date['maximum_date'] - dead_patient_min_max_date['minimum_date']
    #print("These are the columns------>", dead_patient_min_max_date.columns.values)
    
    #For avg_dead_rec_len###########
    count_dead =  dead.patient_id.nunique() ##calculates the total dead patients
    sum_dead_patient_min_max_date = dead_patient_min_max_date['duration'].sum()
    avg_dead_rec_len = sum_dead_patient_min_max_date/count_dead
    print('avg_dead_rec_len----->', avg_dead_rec_len)
    
    #For max_dead_rec_len ######################
    
    max_dead_rec_len = dead_patient_min_max_date['duration'].max()
    print("max_dead_rec_len----->", max_dead_rec_len)
    
    #For min_dead_rec_len ######################
    
    min_dead_rec_len = dead_patient_min_max_date['duration'].min()
    print("min_dead_rec_len----->", min_dead_rec_len)
    
    
    ############For alive######################################################
    
    alive = combine[combine['label'] != 1]
    #print(alive)
    
    ###### Find the max date and min date for each alive patient Id
    df = alive.groupby(['patient_id'])
    alive_patient_min_max_date = df.agg(minimum_date=('timestamp_x', np.min), maximum_date=('timestamp_x', np.max))
    #Changing the index of the dataframe to column patient_id
    alive_patient_min_max_date.reset_index(inplace=True)
    alive_patient_min_max_date = alive_patient_min_max_date.rename(columns = {'index':'patient_id'})
    #Converting the max date and min date to date time format
    alive_patient_min_max_date['minimum_date'] = pd.to_datetime(alive_patient_min_max_date['minimum_date'])
    alive_patient_min_max_date['maximum_date'] = pd.to_datetime(alive_patient_min_max_date['maximum_date'])
    
    ###### Find the duration(days) of each patient id by subtracting the min date from max date
    alive_patient_min_max_date['duration'] = alive_patient_min_max_date['maximum_date'] - alive_patient_min_max_date['minimum_date']
    #print("These are the columns------>", alive_patient_min_max_date.columns.values)
    
    #For avg_alive_rec_len###########
    count_alive =  alive.patient_id.nunique() ##calculates the total alive patients
    sum_alive_patient_min_max_date = alive_patient_min_max_date['duration'].sum()
    avg_alive_rec_len = sum_alive_patient_min_max_date/count_alive
    print('avg_alive_rec_len----->', avg_alive_rec_len)
    
    #For max_alive_rec_len ######################
    
    max_alive_rec_len = alive_patient_min_max_date['duration'].max()
    print("max_alive_rec_len----->", max_alive_rec_len)
    
    #For min_alive_rec_len ######################
    
    min_alive_rec_len = alive_patient_min_max_date['duration'].min()
    print("min_alive_rec_len----->", min_alive_rec_len)

    
    
    


    return min_dead_rec_len, max_dead_rec_len, avg_dead_rec_len, min_alive_rec_len, max_alive_rec_len, avg_alive_rec_len

def main():
    '''
    DO NOT MODIFY THIS FUNCTION.
    '''
    # You may change the following path variable in coding but switch it back when submission.
    train_path = '/users/abhik/'

    # DO NOT CHANGE ANYTHING BELOW THIS ----------------------------
    events, mortality = read_csv(train_path)

    #Compute the event count metrics
    start_time = time.time()
    event_count = event_count_metrics(events, mortality)
    end_time = time.time()
    print(("Time to compute event count metrics: " + str(end_time - start_time) + "s"))
    print(event_count)

    #Compute the encounter count metrics
    start_time = time.time()
    encounter_count = encounter_count_metrics(events, mortality)
    end_time = time.time()
    print(("Time to compute encounter count metrics: " + str(end_time - start_time) + "s"))
    print(encounter_count)

    #Compute record length metrics
    start_time = time.time()
    record_length = record_length_metrics(events, mortality)
    end_time = time.time()
    print(("Time to compute record length metrics: " + str(end_time - start_time) + "s"))
    print(record_length)
    
if __name__ == "__main__":
    main()
