# pylint: disable=redefined-outer-name
"""
Unit tests for range filter
"""


def test_rf_valid_input(lidar_sensor_obj):
    """
    Test for range filter with valid input.
    """
    input_scan_range_filter = [0.01, 5, 10.4, 10, 48, 34.6, 57.3, 50]
    print "\n"
    print "Start New Test - test_range_filter_valid_input"
    print("INPUT SCAN: ", input_scan_range_filter)
    output_scan = lidar_sensor_obj.update_range_filter(input_scan_range_filter)
    print("Range Filter Output Scan", output_scan)
    assert output_scan == [0.03, 5, 10.4, 10, 48, 34.6, 50.0, 50]
    print "END Test"


def test_rf_negative_input(lidar_sensor_obj):
    """
    Test for range filter with negative values for scans.
    This will test if negative values are bumped up to minimum value.
    """
    input_scan_range_filter = [0.01, -5, 10.4, 10, -100, 34.6, 57.3, 2000]
    print "\n"
    print "Start New Test - test_range_filter_negativeInput"
    print ("INPUT SCAN: ", input_scan_range_filter)
    output_scan = lidar_sensor_obj.update_range_filter(input_scan_range_filter)
    print ("Range Filter Output Scan", output_scan)
    assert output_scan == [0.03, 0.03, 10.4, 10, 0.03, 34.6, 50.0, 50.0]
    print "END Test"


def test_rf_null_input(lidar_sensor_obj):
    """
    Test for range filter with null input for scan
    This will make sure, empty list is returned
    """
    input_scan_range_filter = []
    print "\n"
    print "Start New Test - test_range_filter_nullInput"
    print ("INPUT SCAN: ", input_scan_range_filter)
    output_scan = lidar_sensor_obj.update_range_filter(input_scan_range_filter)
    print ("Range Filter Output Scan", output_scan)
    assert output_scan == input_scan_range_filter
    print "END Test"


def test_rf_invalid_input_str(lidar_sensor_obj):
    """
    Test for range filter with invalid input, a string when list is expected.
    Should return None when exception occurs if a string is given as input
    """
    input_scan_range_filter = "SomeInvalidString"
    print "\n"
    print "Start New Test - test_range_filter_invalid_input_str"
    print ("INPUT SCAN: ", input_scan_range_filter)
    output_scan = lidar_sensor_obj.update_range_filter(input_scan_range_filter)
    print ("Range Filter Output Scan", output_scan)
    assert output_scan is None
    print "END Test"


# Should return None when exception occurs if an integer is given as input
def test_rf_invalid_input_int(lidar_sensor_obj):
    """
    Test for range filter with invalid input, a string when list is expected.
    Should return None when exception occurs if a integer is given as input
    """
    input_scan_range_filter = 10
    print "\n"
    print "Start New Test - test_range_filter_invalidinput_Int"
    print ("INPUT SCAN: ", input_scan_range_filter)
    output_scan = lidar_sensor_obj.update_range_filter(input_scan_range_filter)
    print ("Range Filter Output Scan", output_scan)
    assert output_scan is None
    print "END Test"
