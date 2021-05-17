# Modelling assumptions

Consider that you have a satellite which has 5 modes of operation, these are Safe, IDLE, Downlink, Camera and Detumbling. The names suggest their intended behaviour:

- Safe: recovery mode to which the satellite should fall in case of low power or any errors, panels should be sun-pointing in case there’s no error with the ADCS

- IDLE: nominal mode of operations during which the satellite is not using any payloads, panels should be sun-pointing

- Downlink: mode during which high-speed data is downlinked, the antenna must be ECI target-pointing (Earth-Centered-Inertial)

- Cam: mode during which images are being acquired from an onboard camera, the camera must be in Nadir-pointing

- Detumbling: mode which takes care of stabilizing the satellite (reducing its angular rate to 0) in case it is spinning uncontrollably
 
Consider that you have the following measurable parameters/flags from the satellite (some of them may be sent from the ground station):

- Battery capacity (you can think of this as % from the full battery)

- Angular rate estimation from the onboard gyroscopes

- Downlink Flag: takes the value 0 or 1 based on the satellite’s location (GS is visible or not)

- Imaging Flag: takes the value 0 or 1 based on the satellite’s location (imaging area is visible or not)

- Error Flag: takes the value 0 or 1 based on errors in the ADCS.

# Problems

1. Complete a matrix of transitions for the satellite based on the measurable parameters and existing operational modes as follows: For each row X and column Y fill under what logical condition should Mode X transition into Mode Y.

|   X \ Y  |SAFE                     |IDLE                        |DOWNLINK                   |CAM                       |DETUMBLING                  |
|:--------:|:-----------------------:|:-------------------------: |:-------------------------:|:------------------------:|:--------------------------:|
|SAFE      |batt <= 70% or error_flag|batt > 70% and !error_flag  |NA                         |NA                        |NA                          |
|IDLE      |batt <= 70% or error_flag|batt > 70% and !any_flag    |batt > 70% and down_flag   |batt > 70% and img_flag   |batt > 70% and ang_rate > 1 |
|DOWNLINK  |batt <= 70% or error_flag|batt > 70% and !down_flag   |batt > 70% and down_flag   |NA                        |NA                          |
|CAM       |batt <= 70% or error_flag|batt > 70% and !img_flag    |NA                         ||batt > 70% and img_flag  |NA                          |
|DETUMBLING|batt <= 70% or error_flag|batt > 70% and ang_rate <= 1|NA                         |NA                        |batt > 70% and ang_rate > 1 |

2. Consider that the satellite measures (directly or otherwise) all quantities periodically and decides whether to remain in the same mode or transition to another one based on the transition matrix above. Prepare a logical function in Python which takes as an input the current mode and the current values of all parameters and which outputs the new mode to which the satellite should transition.

3. Prepare a complete set of test cases in Python (as a separate script) which test the logical function and all possible transition decisions which it makes. Consider the battery as [%] (i.e. number between 0 and 100) and any dimension for the angular rate (based on how you formulate your operations).

# Running the Test Cases

In order to run the test cases, it was used the *pytest* tool.

> pip install pytest

To generate the csv file test report

>  pip install pytest-csv

To run the tests:

> git clone https://github.com/clgbatista/model-activity.git

> cd model-activity/code

> pytest --csv report.csv

