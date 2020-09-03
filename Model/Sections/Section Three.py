from Model.DataFrames import Applicant_DataFrame
import os

os.chdir('../..')
current_working_directory = os.getcwd()
data_frame_directory = os.path.join(current_working_directory, "DataFrames")
file_name = os.path.join(data_frame_directory, "Applicant_History.csv")


def swim_laps(file, custom_id, time):
    points_added = 0
    if time < 4.00:
        points_added += 6
    elif 4.00 < time < 4.11:
        points_added += 5
    elif 4.10 < time < 4.21:
        points_added += 4
    elif 4.20 < time < 4.31:
        points_added += 3
    elif 4.30 < time < 4.46:
        points_added += 2
    elif 4.45 < time < 4.56:
        points_added += 1
    else:
        points_added = 0
    Applicant_DataFrame.add_points(file, custom_id, points_added)


def treading(file, custom_id, P):
    if P:
        Applicant_DataFrame.add_points(file, custom_id, 3)


def lap_with_tube(file, custom_id, time):
    points_added = 0
    if time < 24:
        points_added += 4
    elif 24 < time < 29:
        points_added += 3
    elif 28 < time < 32:
        points_added += 2
    else:
        points_added += 1
    Applicant_DataFrame.add_points(file, custom_id, points_added)


def brick_retrieval(file, custom_id, time):
    points_added = 0
    if time < 1.00:
        points_added += 7
    elif 1.00 < time < 1.07:
        points_added += 6
    elif 1.06 < time < 1.16:
        points_added += 5
    elif 1.15 < time < 1.21:
        points_added += 4
    elif 1.20 < time < 1.26:
        points_added += 3
    elif 1.25 < time < 1.31:
        points_added += 2
    else:
        points_added += 1
    Applicant_DataFrame.add_points(file, custom_id, points_added)

#swim_laps(file_name, '1', 3)
