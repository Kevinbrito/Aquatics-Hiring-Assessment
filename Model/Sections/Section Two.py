from Model.DataFrames import Applicant_DataFrame
import os

A = B = C = D = E = F = G = H = I = J = K = L = True
os.chdir('../..')
current_working_directory = os.getcwd()
data_frame_directory = os.path.join(current_working_directory, "DataFrames")
file_name = os.path.join(data_frame_directory, "Applicant_History.csv")


def distressed_victim_rescue(file, custom_id, *deductions):
    points_added = 5
    # candidate starts with 5 possible points and loses them based on performance
    for case in deductions:
        if case: points_added -= 1
    # then we add the points
    if points_added < 0: points_added = 0
    Applicant_DataFrame.add_points(file, custom_id, points_added)


def active_victim_rescue(file, custom_id, *deductions):
    points_added = 10
    # candidate starts with 10 possible points and loses them based on performance
    for case in deductions:
        if case: points_added -= 1
    # then we add the points
    if points_added < 0: points_added = 0
    Applicant_DataFrame.add_points(file, custom_id, points_added)


def deep_water_spinal_rescue(file, custom_id, *deductions):
    points_added = 9
    # candidate starts with 10 possible points and loses them based on performance
    for case in deductions:
        if case: points_added -= 2
    # then we add the points
    if points_added < 0: points_added = 0
    Applicant_DataFrame.add_points(file, custom_id, points_added)


def deep_water_spinal_boarding(file, custom_id, *deductions):
    points_added = 9
    # candidate starts with 10 possible points and loses them based on performance
    for case in deductions:
        if case: points_added -= 1
    # then we add the points
    if points_added < 0: points_added = 0
    Applicant_DataFrame.add_points(file, custom_id, points_added)


def submerged_victim_rescue(file, custom_id, *deductions):
    points_added = 5
    # candidate starts with 10 possible points and loses them based on performance
    for case in deductions:
        if case: points_added -= 1
    # then we add the points
    if points_added < 0: points_added = 0
    Applicant_DataFrame.add_points(file, custom_id, points_added)


def submerged_victim_removal(file, custom_id, *deductions):
    points_added = 5
    # candidate starts with 10 possible points and loses them based on performance
    for case in deductions:
        if case: points_added -= 1
    # then we add the points
    if points_added < 0: points_added = 0
    Applicant_DataFrame.add_points(file, custom_id, points_added)

# distressed_victim_rescue(file_name, "1", A)
# deep_water_spinal_boarding(file_name, "1", A)
# Applicant_DataFrame.update_applicant(file_name, '1', 'Points', 0)
# deep_water_spinal_rescue(file_name, '1', A)
