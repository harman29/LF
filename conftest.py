# pylint: disable=redefined-outer-name
'''
Common fixtures for all tests are defined here
'''

import pytest
from lidar_filters import LidarSensors

@pytest.fixture(scope='session', autouse=True)
def lidar_sensor_obj():
    '''
    creates and returns object with odd number of previous
    scans(3 in this case)
    :return: LidarSensors object
    '''
    lidar_sensor_obj = LidarSensors(3)
    return lidar_sensor_obj
