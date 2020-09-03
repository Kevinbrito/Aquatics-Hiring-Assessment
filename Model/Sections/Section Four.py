from Model.DataFrames import Applicant_DataFrame
import os

os.chdir('../..')
current_working_directory = os.getcwd()
data_frame_directory = os.path.join(current_working_directory, "DataFrames")
file_name = os.path.join(data_frame_directory, "Applicant_History.csv")


def first_aid(file, custom_id, *scene_points):
    points_added = 0
    for points in scene_points:
        points_added += points
    Applicant_DataFrame.add_points(file, custom_id, points_added)

