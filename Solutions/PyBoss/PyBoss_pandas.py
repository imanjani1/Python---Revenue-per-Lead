# Import required packages
import os
import pandas as pd

# Files to load and output (Remember to change these)
file_to_load = os.path.join('raw_data', 'employee_data1.csv')
file_to_output = os.path.join('analysis',
                              'employee_data_pandas_reformatted1.csv')

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Read csv file and create a dataframe
df = pd.read_csv(file_to_load)

# Split first name and last name
names_df = pd.DataFrame(df['Name'].str.split().tolist(),
                        columns=['First Name', 'Last Name'])

# Create new columns
df['First Name'] = names_df['First Name']
df['Last Name'] = names_df['Last Name']
# Delete Name column
del df['Name']

# Re-order columns
df = df[['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]

# Replace State by State Abbreviation
df['State'].replace(us_state_abbrev, inplace=True)

# Replace SSN
df['SSN'] = df['SSN'].str.replace(r'\d\d\d-\d\d-', '***-**-')

# Change date format
df['DOB'] = pd.to_datetime(df['DOB']).dt.strftime("%m/%d/%Y")

# Write output file
df.to_csv(file_to_output, index=False)
