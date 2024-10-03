from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import django
import numpy as np
from sqlalchemy import Null, create_engine
from django.db import models
import pandas as pd
import os
import time
from django.db import connection
from psycopg2 import sql
from django.db import IntegrityError
# Create your models here.

class Credentials(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=150)

    class Meta:
        db_table = 'Credentials'

    def __str__(self):
        return self.username
    
import hashlib

def hash_number_sha256(number):
    # Convert number to string and encode it
    number_str = str(number).encode()
    # Create SHA-256 hash object
    hash_object = hashlib.sha256(number_str)
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

def hash_number_sha256(card_number):
    return hashlib.sha256(card_number.encode()).hexdigest()

def applying_conditions_on_df(df):
    global number_of_alert_generated, emv_based_transaction, non_emv_based_transaction, non_emv_successful_transaction, non_emv_unsuccessful_transaction, date, number_of_alerts_taken_up_with_branch
    df['TOTAL_TXN_AMOUNT'] = 0
    df['DATETIME_LOCAL_TXN'] = pd.to_datetime(df['DATETIME_LOCAL_TXN'])
    df['DATELOGGED'] = pd.to_datetime(df['DATELOGGED'])
    date = df['DATETIME_LOCAL_TXN'].dt.date.iloc[0]

    df['CARDNUMBER'] = df['CARDNUMBER'].astype(str)
    df['PROCESSING_CODE'] = df['PROCESSING_CODE'].astype(str)
    df['STAN'] = df['STAN'].astype(str)
    
    number_of_alert_generated = df.shape[0]
    emv_based_transaction = df[df['POS_ENTRY_MODE'] == 51].shape[0]

    df = df[df['POS_ENTRY_MODE'] != 51]

    non_emv_based_transaction = df.shape[0]
    non_emv_unsuccessful_transaction = df[df['TXN_ACTION_CODE'] != '00'].shape[0]
    df = df[df['TXN_ACTION_CODE'] == '00']
    non_emv_successful_transaction = df.shape[0]
    print(df)
    date_filter_df_1 = df[(df['DATETIME_LOCAL_TXN'].dt.time >= pd.to_datetime('00:00:00').time()) & (df['DATETIME_LOCAL_TXN'].dt.time <= pd.to_datetime('05:00:00').time())]
    date_filter_df = df[df['CARDNUMBER'].isin(date_filter_df_1['CARDNUMBER'])]

    df = df[~df.index.isin(date_filter_df.index)]

    frequent_numbers_df = df.groupby('CARDNUMBER').filter(lambda x: len(x) > 2)
    frequent_numbers = frequent_numbers_df['CARDNUMBER']

    filtered_df = df[df['CARDNUMBER'].isin(frequent_numbers)]

    filtered_df = pd.concat([date_filter_df, filtered_df])
    df = df[~df.index.isin(filtered_df.index)]

    grouped_df = df.groupby('CARDNUMBER')['TXN_AMOUNT'].sum().reset_index()
    filtered_group_df = grouped_df[grouped_df['TXN_AMOUNT'] > 50000]
    
    filtered_1 = pd.DataFrame()
    for name, group in filtered_group_df.groupby('CARDNUMBER'):
        filtered = df[df['CARDNUMBER'] == name]
        filtered['TOTAL_TXN_AMOUNT'] = group['TXN_AMOUNT'].iloc[0]
        filtered_1 = pd.concat([filtered_1, filtered])
    fraud_df = pd.concat([filtered_df, filtered_1])
    number_of_alerts_taken_up_with_branch = fraud_df.shape[0]
    print(fraud_df.info())
    copy_df = fraud_df.copy()
    copy_df['CARDNUMBER'] = copy_df['CARDNUMBER'].apply(hash_number_sha256)
    
    # for index, row in copy_df.iterrows():
    #     print(index)
    #     Transaction.objects.create(
    #         org_name=row['ORG_NAME'],
    #         channel=row['CHANNEL'],
    #         txn_id=row['TXN_ID'],
    #         case_id=row['CASE_ID'],
    #         processing_code=row['PROCESSING_CODE'],
    #         datetime_local_txn=row['DATETIME_LOCAL_TXN'],
    #         datelogged=row['DATELOGGED'],
    #         txn_amount=row['TXN_AMOUNT'],
    #         settlement_amount=row['SETTLEMENT_AMOUNT'],
    #         reversal_status=row['REVERSAL_STATUS'],
    #         txn_action_code=row['TXN_ACTION_CODE'],
    #         mti=row['MTI'],
    #         rule_score=row['RULE_SCORE'],
    #         model_score=row['MODEL_SCORE'],
    #         merch_cat=row['MERCH_CAT'],
    #         pos_entry_mode=row['POS_ENTRY_MODE'],
    #         acceptor_name=row['ACCEPTOR_NAME'],
    #         acceptor_city=row['ACCEPTOR_CITY'],
    #         acceptor_state=row['ACCEPTOR_STATE'],
    #         acceptor_country=row['ACCEPTOR_COUNTRY'],
    #         acq_country=row['ACQ_COUNTRY'],
    #         acceptor_termid=row['ACCEPTOR_TERMID'],
    #         acq_bin=row['ACQ_BIN'],
    #         rrn=row['RRN'],
    #         acceptor_id=row['ACCEPTOR_ID'],
    #         stan=row['STAN'],
    #         cardnumber=row['CARDNUMBER'],
    #         txn_sub_code=row['TXN_SUB_CODE'],
    #         product_indicator=row['PRODUCT_INDICATOR'],
    #         deposit_id=row['DEPOSIT_ID'],
    #         matched_rule=row['MATCHED_RULE'],
    #         total_txn_amount=row['TOTAL_TXN_AMOUNT']
    #     )

    # print("Data inserted successfully.")

    # frequent_numbers_df.to_sql('frequent_numbers', engine, if_exists='replace', index=False)
    # filtered_group_df.to_sql('filtered_group', engine, if_exists='replace', index=False)
    rules()
    return fraud_df

def segregation_data_sending_to_branch_code(unique_rows):
    unique_rows['last_4_digits'] = unique_rows['CARDNUMBER'].str[6:10]
    filtered_df = unique_rows.groupby('last_4_digits')
    for name, group in filtered_df:
        folder_name = name
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        filename = f'{name}/Branch_Code_{name}_{date}.xlsx'

        filtered = unique_rows[unique_rows['CARDNUMBER'].isin(group['CARDNUMBER'])]
        filtered.to_excel(filename, index=False, engine='openpyxl')

def create_summary_file(date, number_of_alert_generated, non_emv_based_transaction, emv_based_transaction, non_emv_successful_transaction, non_emv_unsuccessful_transaction, number_of_alerts_taken_up_with_branch, summary_file_path):
    data_to_append = {
        'DATE': [date],
        'NUMBER OF ALERT GENERATED': [number_of_alert_generated],
        'EMV BASED TRANSACTION': [emv_based_transaction],
        'NON EMV BASED TRANSACTION': [non_emv_based_transaction],
        'NON EMV SUCCESSFUL TRANSACTION': [non_emv_successful_transaction],
        'NON EMV UNSUCCESSFUL TRANSACTION': [non_emv_unsuccessful_transaction],
        'NUMBER OF ALERTS TAKEN UP WITH BRANCH': [number_of_alerts_taken_up_with_branch]
    }
    df_summary = pd.DataFrame(data_to_append)
    
    # Save summary data to Excel file
    if os.path.exists(summary_file_path):
        df_existing = pd.read_excel(summary_file_path, engine='openpyxl')
        
        if date in df_existing['DATE'].dt.date.values:
            print(f"Data for {date} is already present. No new data appended.")
        else:
            df_combined = pd.concat([df_existing, df_summary], ignore_index=True)
            df_combined.to_excel(summary_file_path, index=False, engine='openpyxl')
            print(f"Summary data for {date} has been appended to {summary_file_path}")
    else:
        df_summary.to_excel(summary_file_path, index=False, engine='openpyxl')
        print(f"Summary data for {date} has been written to {summary_file_path}")

    # Insert summary data into PostgreSQL
    # insert_summary_report_into_postgres(summary_file_path)

# Function to read Excel file with appropriate engine
def read_excel_file(file_path):
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path, engine='openpyxl')
    elif file_path.endswith('.xls'):
        return pd.read_excel(file_path, engine='xlrd')
    else:
        raise ValueError("Unsupported file format")

def dashboard_model():
    smtp_server = 'smtp.example.com'
    email_from = 'your_email@example.com'
    email_to = 'recipient@example.com'
    pswd = 'your_password'
    subject = 'Transaction Alert Report' 
    # Read the Excel file into a DataFrame
    file_path = 'static/datafile.xlsx'

    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        df = read_excel_file(file_path)
        start_time = time.time()
        unique_rows = applying_conditions_on_df(df)
        segregation_data_sending_to_branch_code(unique_rows)
        summary_file_path = 'SUMMARY_REPORT_FILE.xlsx'
        create_summary_file(date, number_of_alert_generated, non_emv_based_transaction, emv_based_transaction, non_emv_successful_transaction, non_emv_unsuccessful_transaction, number_of_alerts_taken_up_with_branch, summary_file_path)
        #insert_summary_report_into_postgres(summary_file_path)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")

    except FileNotFoundError as fnf:
        print(f"FileNotFoundError: {fnf}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    context = {
        "var1" : number_of_alert_generated,
        "var2" : non_emv_based_transaction,
        "var3" : emv_based_transaction,
        "var4" : non_emv_successful_transaction,
        "var5" : non_emv_unsuccessful_transaction
    }
    return context

def transactiontable():
    with connection.cursor() as cursor:
        # Execute a raw SQL query
        cursor.execute("SELECT * FROM transactions_new")
        # Fetch all rows
        rows = cursor.fetchall()

    # Get column names
    columns = [desc[0] for desc in cursor.description]
    context = {
        "rows": rows,
        "columns": columns
    }
    return context

class suspicious_transaction(models.Model):
    org_name = models.CharField(max_length=50)
    channel = models.CharField(max_length=100)
    txn_id = models.CharField(max_length=255, unique=True)  # Unchecked
    case_id = models.CharField(max_length=255)
    processing_code = models.CharField(max_length=255)
    date_time_local_txn = models.DateTimeField()
    date_logged = models.DateTimeField()
    txn_amount = models.DecimalField(max_digits=15, decimal_places=2)
    settlement_amount = models.DecimalField(max_digits=15, decimal_places=2)
    reversal_status = models.CharField(max_length=255)
    txn_action_code = models.CharField(max_length=255)
    mti = models.CharField(max_length=255)
    rule_score = models.CharField(max_length=255)
    model_score = models.CharField(max_length=255)
    merch_cat = models.CharField(max_length=255)
    pos_entry_mode = models.CharField(max_length=255)
    acceptor_name = models.CharField(max_length=255)
    acceptor_city = models.CharField(max_length=255)
    acceptor_state = models.CharField(max_length=255)
    acceptor_country = models.CharField(max_length=255)
    acq_country = models.CharField(max_length=255)
    acceptor_termid = models.CharField(max_length=255)
    acq_bin = models.CharField(max_length=255)
    rrn = models.CharField(max_length=255)
    acceptor_id = models.CharField(max_length=255)
    stan = models.CharField(max_length=255)
    cardnumber = models.CharField(max_length=255)
    txn_sub_code = models.CharField(max_length=255)
    product_indicator = models.CharField(max_length=255)
    deposit_id = models.CharField(max_length=255)
    matched_rule = models.CharField(max_length=255)
    rule_id = models.BigIntegerField()
    rule_name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'suspicious_transaction'

    def __str__(self):
        return self.txn_id
    
class Rule(models.Model):
    STATUS_CHOICES = [
        ('Activate', 'Activate'),
        ('Deactivate', 'Deactivate'),
    ]
    ruleName = models.CharField(max_length=255, unique=True)
    rule_details = models.CharField(max_length=255)
    rule_desc = models.TextField(max_length=1000)
    rule_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Activate')
    rule_created_date = models.DateTimeField()
    rule_expiry_date = models.DateTimeField()

    class Meta:
        db_table = 'Rule'

    def __str__(self):
        return self.ruleName

def display_data_of_fraud_transactions():
    with connection.cursor() as cursor:
        # Execute a raw SQL query
        cursor.execute("SELECT * FROM [FRM].[dbo].[Transaction]")
        # Fetch all rows
        rows = cursor.fetchall()

    # Get column names
    columns = [desc[0] for desc in cursor.description]
    context = {
        "rows": rows,
        "columns": columns
    }
    return context

from django.db import DatabaseError

def my_daily_job():
    # Logic for checking rules, flagging fraud, etc.

    df = pd.read_excel('static/datafile.xlsx')


    # Convert numeric columns and handle NaNs
    df['RULE_SCORE'] = pd.to_numeric(df['RULE_SCORE'], errors='coerce').fillna(0)
    df['MODEL_SCORE'] = pd.to_numeric(df['MODEL_SCORE'], errors='coerce').fillna(0)
    df['TXN_AMOUNT'] = pd.to_numeric(df['TXN_AMOUNT'], errors='coerce').fillna(0.0)
    df['SETTLEMENT_AMOUNT'] = pd.to_numeric(df['SETTLEMENT_AMOUNT'], errors='coerce').fillna(0.0)

    # Handle all NaN values
    df.fillna({
        'ORG_NAME': 'Unknown',
        'CHANNEL': 'Unknown',
        'TXN_ID': 'Unknown',
        'CASE_ID': 'Unknown',
        'PROCESSING_CODE': 0,
        'DATETIME_LOCAL_TXN': pd.Timestamp('1970-01-01'),
        'DATELOGGED': pd.Timestamp('1970-01-01'),
        'REVERSAL_STATUS': False,
        'TXN_ACTION_CODE': 'Unknown',
        'MTI': 0,
        'MERCH_CAT': 0,
        'POS_ENTRY_MODE': 0,
        'ACCEPTOR_NAME': 'Unknown',
        'ACCEPTOR_CITY': 'Unknown',
        'ACCEPTOR_STATE': 'Unknown',
        'ACCEPTOR_COUNTRY': 'Unknown',
        'ACQ_COUNTRY': 0,
        'ACCEPTOR_TERMID': 'Unknown',
        'ACQ_BIN': 0,
        'RRN': 'Unknown',
        'ACCEPTOR_ID': 'Unknown',
        'STAN': 0,
        'CARDNUMBER': 'Unknown',
        'TXN_SUB_CODE': 'Unknown',
        'PRODUCT_INDICATOR': 'Unknown',
        'DEPOSIT_ID': 'Unknown',
        'MATCHED_RULE': 'Unknown'
    }, inplace=True)

    # Prepare the insert query
    insert_query = """
           INSERT INTO [FRM].[dbo].[TransactionData] (
               org_name, channel, txn_id, case_id, processing_code, 
               date_time_local_txn, date_logged, txn_amount, settlement_amount, 
               reversal_status, txn_action_code, mti, rule_score, model_score, 
               merch_cat, pos_entry_mode, acceptor_name, acceptor_city, 
               acceptor_state, acceptor_country, acq_country, acceptor_termid, 
               acq_bin, rrn, acceptor_id, stan, cardnumber, txn_sub_code, 
               product_indicator, deposit_id, matched_rule
           ) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)
       """

    data = [(
        row['ORG_NAME'],
        row['CHANNEL'],
        row['TXN_ID'],
        row['CASE_ID'],
        row['PROCESSING_CODE'],
        row['DATETIME_LOCAL_TXN'],
        row['DATELOGGED'],
        (row['TXN_AMOUNT']),
        (row['SETTLEMENT_AMOUNT']),
        row['REVERSAL_STATUS'],
        row['TXN_ACTION_CODE'],
        row['MTI'],
        row['RULE_SCORE'],
        row['MODEL_SCORE'],
        row['MERCH_CAT'],
        row['POS_ENTRY_MODE'],
        row['ACCEPTOR_NAME'],
        row['ACCEPTOR_CITY'],
        row['ACCEPTOR_STATE'],
        row['ACCEPTOR_COUNTRY'],
        row['ACQ_COUNTRY'],
        row['ACCEPTOR_TERMID'],
        row['ACQ_BIN'],
        row['RRN'],
        row['ACCEPTOR_ID'],
        row['STAN'],
        row['CARDNUMBER'],
        row['TXN_SUB_CODE'],
        row['PRODUCT_INDICATOR'],
        row['DEPOSIT_ID'],
        row['MATCHED_RULE']
    ) for index, row in df.iterrows()]
    print(insert_query)
    print(data)
    try:
        with connection.cursor() as cursor:
            cursor.executemany(insert_query, data)
            print("Data inserted successfully")
    except DatabaseError as e:
        print(f"Error occurred: {e}")

def rules():
    fraud_df = pd.DataFrame()
    # Query to fetch data
    query = "SELECT * FROM [FRM].[dbo].[Rule] WHERE [rule_status] = 'Activate'"

    # Fetch data into a DataFrame
    rule = pd.read_sql(query, connection)
    #rule_descriptions = rule['rule_desc'].tolist()
    print(rule.info())
    for index, row in rule.iterrows():
        df = pd.read_sql(row['rule_desc'], connection)
        print("rules_df")
        print(df)
        df['rule_id'] = row['id']
        df['rule_name'] = row['ruleName']
        fraud_df = pd.concat([fraud_df,df]) 

    for index, row in fraud_df.iterrows():
        print(index)
        try:
            suspicious_transaction.objects.create(
                org_name=row['org_name'],
                channel=row['channel'],
                txn_id=row['txn_id'],
                case_id=row['case_id'],
                processing_code=row['processing_code'],
                date_time_local_txn=row['date_time_local_txn'],  
                date_logged=row['date_logged'],                  
                txn_amount=row['txn_amount'],
                settlement_amount=row['settlement_amount'],
                reversal_status=row['reversal_status'],
                txn_action_code=row['txn_action_code'],
                mti=row['mti'],
                rule_score=row['rule_score'],
                model_score=row['model_score'],
                merch_cat=row['merch_cat'],
                pos_entry_mode=row['pos_entry_mode'],
                acceptor_name=row['acceptor_name'],
                acceptor_city=row['acceptor_city'],
                acceptor_state=row['acceptor_state'],
                acceptor_country=row['acceptor_country'],
                acq_country=row['acq_country'],
                acceptor_termid=row['acceptor_termid'],
                acq_bin=row['acq_bin'],
                rrn=row['rrn'],
                acceptor_id=row['acceptor_id'],
                stan=row['stan'],
                cardnumber=row['cardnumber'],
                txn_sub_code=row['txn_sub_code'],
                product_indicator=row['product_indicator'],
                deposit_id=row['deposit_id'],
                matched_rule=row['matched_rule'],
                rule_id=row['rule_id'],                          
                rule_name=row['rule_name']                       
            )
        except IntegrityError:
            print(f"Duplicate entry for txn_id {row['txn_id']}. Skipping.")

    print("Data inserted successfully.")

    # # Display the DataFrame
    # print(fraud_df)

def dashboard_details():

    print("Displayed...")
