"""
Take Home Assignment by Brain Corp.

Author: Harmandeep Singh

Date Submitted: 9/25/2019

Description: You have been assigned to write filters to reduce noise in the data
coming from a LIDAR sensor attached to your robot. The LIDAR generates scans at
a certain rate. Each scan is an array of length N of float values representing
distance measurements. N is typically in a range of ~[200, 1000] measurements, and
it is fixed. Measured distances are typically in a range of [0.03, 50] meters. Each
time a scan is received, it will be passed on to the filters. Each filter object
should have an update method, that takes a length-N array of ranges and returns
a filtered length-N array of ranges.

Range Filter
The range filter crops all the values that are below range_min (resp. above range_max),
and replaces them with the range_min value (resp. range_max)

Temporal Filter
The temporal median filter returns the median of the current and the previous D scans:
y(i)(t) = median(x(i)(t), x(i)(t-1), ... , x(i)(t-D))

where x and y are input and output length-N scans and i ranges from 0 to N-1. The number
of previous scans D is a parameter that should be given when creating a new temporal median
filter. Note that, although the update method will receive a single scan, the returned array
depends on the values of previous scans. Note also that the for the first D scans, the
filter is expected to return the median of all the scans so far

Here is a short example of the result (Y) of a temporal median filter object with D=3 for an input
(X) of dimension N=5, for the first five updates:

T (time)	X (input scan)	         Y (return of the update)
0	       [0., 1., 2., 1., 3.]	     [0., 1., 2., 1., 3.]
1	       [1., 5., 7., 1., 3.]	     [0.5, 3. , 4.5, 1. , 3. ]
2	       [2., 3., 4., 1., 0.]      [ 1., 3., 4., 1., 3.]
3          [3., 3., 3., 1., 3.]      [ 1.5, 3. , 3.5, 1. , 3. ]
4	       [10., 2., 4., 0., 0.]     [ 2.5, 3. , 4. , 1. , 1.5]
"""

import numpy as np


class LidarSensors(object):
    """
    Class to encapsulate a LidarSensor and its methods to update rangeFilter and TemporalFilter
    """
    min = 0.03
    max = 50.0

    def __init__(self, num_of_prev_scans):
        # Setting Default number of scans to 0, otherwise what user passed as param.
        if num_of_prev_scans < 0:
            self.num_of_prev_scans = 0
        else:
            self.num_of_prev_scans = num_of_prev_scans
        self.list_of_scans = []

    def getmedian(self):
        """
            Return the median of all elements at a specific index of current and finite number of
            previous scans
        """
        all_scans_at_indexes = []
        filter_output = []
        num_of_elements_in_each_scan = len(self.list_of_scans[0])
        for distance in range(0, num_of_elements_in_each_scan):
            for scan_at_index in range(0, len(self.list_of_scans)):
                all_scans_at_indexes.append(self.list_of_scans[scan_at_index][distance])
            array_of_scans = np.array(all_scans_at_indexes)
            # append to list, the median of all elements at index (scan_at_index), rounded to 2 digits after
            # decimal for readability purposes
            filter_output.append(round(np.median(array_of_scans), 2))
            # empty the list to get median of elements at next index
            all_scans_at_indexes = []

        return filter_output

    def update_temporal_filter(self, scan):
        """
            method to update temporal filter when a new scan comes.
            Uses lists pop function to remove first element at index 0 when we need
            to make room for new scan which is added at the end.
        """
        if len(self.list_of_scans) != self.num_of_prev_scans + 1:
            self.list_of_scans.append(scan)
        else:
            self.list_of_scans.pop(0)
            self.list_of_scans.append(scan)

        # get median once we have current and previous finite number of scans figured out.
        return self.getmedian()

    def update_range_filter(self, scan):
        """
            method to update range filter
            if any value in scan is less than 0.3, its bumped up to 0.3
            if any value in scan is more than 50.0, its is scaled down to 50.0
            min and max range is defined during object initialization.
        """
        try:
            for i, val in enumerate(scan):
                if val < self.min:
                    scan[i] = self.min
                if val > self.max:
                    scan[i] = self.max

            return scan
        except TypeError:
            print "Please pass valid list as in input"
            return None

