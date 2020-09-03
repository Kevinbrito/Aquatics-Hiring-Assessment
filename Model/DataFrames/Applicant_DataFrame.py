import pandas as pd
from datetime import date
from Model.Classes import Applicants

today = date.today()
applicant_date = None


def create_data_frame():
    applicant_info = {'First_Name': ['Kevin'], 'Last_Name': ['Brito'],
                      'Email_Address': ['kevinbri@buffalo.edu'], 'Custom_ID': [0o0001],
                      'Points': [100], 'P/F': ['P'], 'Date': [today]
                      }
    applicant_data = pd.DataFrame(data=applicant_info)
    applicant_data.to_csv('Applicant_History.csv')
    return


def add_applicant(file, first_name, last_name, email_address, pf):
    applicant_data = pd.read_csv(file, index_col=0)
    if email_address in applicant_data.values:
        print("An applicant with that email address already exists!")
        return
    applicant = Applicant(first_name, last_name, email_address)
    row_list = {'First_Name': [first_name], 'Last_Name': [last_name],
                'Email_Address': [email_address], 'Custom_ID': [applicant.custom_id],
                'Points': [applicant.points], 'P/F': [pf], 'Date': [today]
                }
    new_row = pd.DataFrame(row_list,
                           columns=['First_Name', 'Last_Name', 'Email_Address',
                                    'Custom_ID', 'Points', 'P/F', 'Date']
                           )
    applicant_data = applicant_data.append(new_row, ignore_index=True)
    applicant_data.to_csv(file)
    return


def update_applicant(file, custom_id, column, change):
    applicant_data = pd.read_csv(file, index_col=0)
    index = applicant_data.index[applicant_data['Custom_ID'] == custom_id]
    applicant_data.at[index, column] = change
    applicant_data.to_csv(file)
    return


def delete_applicant(file, custom_id):
    applicant_data = pd.read_csv(file, index_col=0)
    index = applicant_data.index[applicant_data['Custom_ID'] == custom_id]
    applicant_data = applicant_data.drop(index=index)
    applicant_data.to_csv(file)
    return


def add_points(file, custom_id, points):
    applicant_data = pd.read_csv(file, index_col=0)
    current_points = applicant_data[applicant_data['Custom_ID'] == custom_id].Points[0]
    print(current_points)
    index = applicant_data.index[applicant_data['Custom_ID'] == custom_id]
    applicant_data.at[index, 'Points'] = current_points + points
    applicant_data.to_csv(file)
    return


# update_applicant("Applicant_History.csv", "1", "Points", 0)
# add_applicant("Applicant_History.csv", 'Lissett', 'Delgado', 'lissettdelgado98@gmail.com', 'P')
# delete_applicant("Applicant_History.csv", 'L341021D')
# html = pd.read_excel('Contact_List.xlsx', index_col=0).to_html('Contact_List.html')
