from Model.DataFrames import Applicant_DataFrame
import os

os.chdir('../..')
current_working_directory = os.getcwd()
data_frame_directory = os.path.join(current_working_directory, "DataFrames")
file_name = os.path.join(data_frame_directory, "Applicant_History.csv")


def multiple_choice(file, custom_id, points):
    Applicant_DataFrame.add_points(file, custom_id, points)
    return

# multiple_choice(file_name, '1', 15)
