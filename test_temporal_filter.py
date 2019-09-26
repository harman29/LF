# pylint: disable=redefined-outer-name
'''
Unit tests for temporal filter
'''

import random
import itertools
import pytest
from lidar_filters import LidarSensors


@pytest.fixture(scope='session', autouse=True)
def lidar_sensor_obj_even_2():
    '''
    creates and returns object with even number of previous
    scans(2 in this case)
    :return: LidarSensors object
    '''
    lidar_sensor_obj_even_2 = LidarSensors(2)
    return lidar_sensor_obj_even_2


@pytest.fixture(scope='session', autouse=True)
def lidar_sensor_obj_0():
    '''
    creates and returns object with zero previous scans
    scans(3 in this case)
    :return: LidarSensors object
    '''
    lidar_sensor_obj_0 = LidarSensors(0)
    return lidar_sensor_obj_0


@pytest.fixture(scope='session', autouse=True)
def lidar_sensor_obj_negative():
    '''
    Tries to create an object with negative number of
    previous scans - tests the part where it should be defaulted to 0.
    :return: LidarSensors object
    '''
    lidar_sensor_obj_negative = LidarSensors(-10)
    return lidar_sensor_obj_negative


def test_tf_assignment_input(lidar_sensor_obj):
    '''
    Tests temporal filter function with example given in assignment.
    :return: LidarSensors object
    '''
    input_tf = [[0., 1., 2., 1., 3., 6], [1., 5., 7., 1., 3., 9],
                [2., 3., 4., 1., 0., 10], [3., 3., 3., 1., 3., 34],
                [10., 2., 4., 0., 0., 12]]
    print "\n"
    for k, scan_tf in enumerate(input_tf):
        print("Input to Temporal Filter:", scan_tf, "O/P Temporal Filter: ",
              lidar_sensor_obj.update_temporal_filter(input_tf[k]))


def test_tf_1000_entry_scans(lidar_sensor_obj):
    '''
    Tests temporal filter function with scans having 1000 entries as that is
    upper limit of typical scan as per assignment
    '''
    input_tf = []
    input_tf_single_scan = []
    # for i in range(0, 50):
    for _ in itertools.repeat(None, 50):
        for _ in itertools.repeat(None, 1000):
            random_float_val = round(random.uniform(0.3, 50.0), 2)
            input_tf_single_scan.append(random_float_val)
        input_tf.append(input_tf_single_scan)
        input_tf_single_scan = []

    print "\n"
    for k, scan_tf in enumerate(input_tf):
        print("Input to Temporal Filter:", scan_tf, "O/P Temporal Filter: ",
              lidar_sensor_obj.update_temporal_filter(input_tf[k]))


def test_tf_even_2_prev_scans(lidar_sensor_obj_even_2):
    '''
    Tests temporal filter function with even number of previous scans being
    used for comparisons
    '''
    input_tf = []
    input_tf_single_scan = []
    for _ in itertools.repeat(None, 6):
        for _ in itertools.repeat(None, 10):
            random_float_val = round(random.uniform(0.3, 50.0), 2)
            input_tf_single_scan.append(random_float_val)
        input_tf.append(input_tf_single_scan)
        input_tf_single_scan = []

    print "\n"
    for k, scan_tf in enumerate(input_tf):
        print("Input to Temporal Filter:", scan_tf, "O/P Temporal Filter: ",
              lidar_sensor_obj_even_2.update_temporal_filter(input_tf[k]))


def test_tf_zero_prev_scans(lidar_sensor_obj_0):
    '''
    Tests temporal filter function with zero passed as number of previous
    scans to be used for comparisons.
    '''
    input_tf = []
    input_tf_single_scan = []
    for _ in itertools.repeat(None, 6):
        for _ in itertools.repeat(None, 10):
            random_float_val = round(random.uniform(0.3, 50.0), 2)
            input_tf_single_scan.append(random_float_val)
        input_tf.append(input_tf_single_scan)
        input_tf_single_scan = []

    print "\n"
    for k, scan_tf in enumerate(input_tf):
        print("Input to Temporal Filter:", scan_tf, "O/P Temporal Filter: ",
              lidar_sensor_obj_0.update_temporal_filter(input_tf[k]))


def test_tf_neg_prev_scans_def_0(lidar_sensor_obj_negative):
    '''
    Tests temporal filter function with negative number passed as number of previous
    scans to be used for comparisons. Default value for previous number of scans
    should kick in which is 0.
    '''
    input_tf = []
    input_tf_single_scan = []
    for _ in itertools.repeat(None, 6):
        for _ in itertools.repeat(None, 10):
            random_float_val = round(random.uniform(0.3, 50.0), 2)
            input_tf_single_scan.append(random_float_val)
        input_tf.append(input_tf_single_scan)
        input_tf_single_scan = []

    print "\n"
    for k, scan_tf in enumerate(input_tf):
        print("Input to Temporal Filter:", scan_tf, "O/P Temporal Filter: ",
              lidar_sensor_obj_negative.update_temporal_filter(input_tf[k]))
