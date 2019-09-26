
## 1. Installation instructions
#### 1.a. Virtual Environment (Optional)
    ▪ Create and activate a virtual environment.
    ▪ Install python 2.7 and pip inside virtual environment.
		
#### 1.b. Clone the repo
    ▪ git clone https://github.com/harman29/LF.git
    
#### 1.c. After you clone, you will see the following files in LF folder.
	▪ lidar_filters.py
	▪ test_range_filter.py
	▪ test_temporal_filter.py
	▪ test_range_temporal_filters.py
	▪ test_range_filter_output.txt
	▪ test_temporal_filter_output.txt
	▪ conftest.py
	▪ README.md
	▪ requirements.txt
		
#### 1.d Need to install numpy package to calculate the median.
    ▪ sudo pip install numpy
		
#### 1.e Need to install pytest to run the tests
    ▪ sudo apt install python-pytest
		
## 2. Run tests
▪ sudo pytest -v test_range_filter.py(5 tests).  
▪ sudo pytest -v test_temporal_filter.py(5 tests)  
▪ sudo pytest -v test_range_temporal_filters.py(1 test)  
    - test_range_temporal_filters combines the testing of filters. It sends an input to range filter
   followed by temporal filter.
			
			
## 3. Structure of assignment
#### ▪ lidar_filters.py has the following
	▪ Class called LidarSensors
	▪ Constructor which initializes previous number of scans to be considered to get the median.
	▪ Range filter update function
	▪ Temporal filter update function
			
#### ▪ test_range_filter.py
	▪ Unit tests to test range filter.
	
#### ▪ test_temporal_filter.py
	▪ Unit tests to test temporal filter.
	 
#### ▪ test_range_temporal_filters.py
	▪ Unit test to test using output of range filter as input to temporal filter.
	
## 4. Implementation
	▪ List data structure is used to store a finite number of scans in a stack.
	▪ If stack is full with all spots for previous number of scans occupied, its pop(0) method
    is used to remove element at index 0 and new scan is inserted at the end.
	▪ This is followed by a call to getmedian function.
	▪ List of scans is iterated over to form a temporary list which includes elements at one
    of the indexes in each iteration of loop followed by getting a median of those elements.
	▪ That element is then appended to the O/P list which is finally returned.
		
	
## 5. Assumptions / Key Notes
	▪ All objects have a minimum and maximum range set as 0.03 and 50.0 resp. as stated in assignment.
	▪ Previous number of scans cannot be negative, if its given as negative, its modified to be zero,
    which means output contains only current scan.
	▪ Every scan has same number of elements.
	▪ Tests have been done for the following.
		▪ Even number for previous number of scans
		▪ Odd number for previous number of scans.
		▪ Null values for input scan, empty list
		▪ Negative values for input scans, list having negative values(range filter)
    ▪ Negative values for previous number of scans.
		▪ 1000 element scans as it was typical distances as stated by assignment.
	▪ Lint was run to remove all unwanted errors and warnings, score output below.
		
		
## 6. LINT Output for All files
	• --------------------------------------------------------------------
	Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
	No config file found, using default configuration  
    Process finished with exit code 0

## Misc Note:
    ▪ Tests were developed in pycharm on windows, test output attached is also from Windows run.
    ▪ All packages were installed in pycharm using pycharm IDE
    ▪ It was made sure that tests are also able to run on Linux platform, instructions for installating
     packages are based on Linux(Ubuntu 18.04)
    ▪ requirements.txt was generating using pip freeze
