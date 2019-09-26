# pylint: disable=redefined-outer-name
'''
Unit test for range and temporal filter
'''

import random
import itertools

def test_range_tf_validinput(lidar_sensor_obj):
    '''
    Test with both range and temporal filter
    '''
    input_range_tf = []
    input_range_tf_single_scan = []
    for _ in itertools.repeat(None, 10):
        for _ in itertools.repeat(None, 10):
            random_float_val = round(random.uniform(-10.3, 100.5), 2)
            input_range_tf_single_scan.append(random_float_val)
        input_range_tf.append(input_range_tf_single_scan)
        input_range_tf_single_scan = []

    print "\n"
    for k, scan_tf in enumerate(input_range_tf):
        print "\n"
        print("Range Filter Input:", scan_tf)
        print("Range Filter O/P : ",
              lidar_sensor_obj.update_range_filter(input_range_tf[k]))
        print "\n"
        print("Input to Temporal Filter:", scan_tf, "O/P Temporal Filter: ",
              lidar_sensor_obj.update_temporal_filter(input_range_tf[k]))
