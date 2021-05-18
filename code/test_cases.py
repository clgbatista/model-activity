# testing_cases.py
# @clgbatista - May 2021

import pytest
from modelexam import change_mode,pointing

# FEATURE: operational mode transitions

# SCENARIO: The satellite as operational mode, wants to deal with an issue, in order to recover from an fault.
@pytest.mark.parametrize("actual_state,batt,ang_rate,down_flag,img_flag,error_flag",[
    ('SAFE',70,0,0,0,0),
    ('IDLE',60,0,0,0,0),
    ('CAM',50,0,0,0,0),
    ('DOWNLINK',40,0,0,0,0),
    ('DETUMBLING',30,0,0,0,0),
    ('SAFE',20,0,0,0,0),
    ('IDLE',10,0,0,0,0),
    ('SAFE',100,0,0,0,1),
    ('IDLE',90,0,0,0,1),
    ('CAM',80,0,0,0,1),
    ('DOWNLINK',70,0,0,0,1),
    ('DETUMBLING',60,0,0,0,1),
    ('SAFE',50,0,0,0,1),
    ('IDLE',40,0,0,0,1),
])
def test_anytosafe(actual_state,batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is at any mode
    actual_state = actual_state
# WHEN: battery charge is equal or lesser than 70% or error flag is true
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite goes to SAFE mode
    next_state = 'SAFE'
    assert change_mode(actual_state,config_vector) == next_state

# SCENARIO: The satellite as operational mode, wants to prepare the operation, in order to enter in nominal operation.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,0,0,0),
    (90,0,0,0,0),
    (80,0,0,0,0),
])
def test_safetoidle(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in SAFE mode
    actual_state = 'SAFE'
# WHEN: battery charge is greater than 70% and error flag is false
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite change to IDLE mode
    next_state = 'IDLE'
    assert change_mode(actual_state,config_vector) == next_state
    
# SCENARIO: The satellite as operational mode, wants to send telemetries, in order to downlink data to GS.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,1,0,0),
    (90,0,1,0,0),
    (80,0,1,0,0),
])
def test_idletodownlink(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in IDLE mode
    actual_state = 'IDLE'
# WHEN: battery charge is greater than 70% and downlink flag is true and error flag is false
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite change to DOWNLINK mode
    assert change_mode(actual_state,config_vector) == 'DOWNLINK'
    
# SCENARIO: The satellite as operational mode, wants to use the onboard camera, in order to image an area.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,0,1,0),
    (90,0,0,1,0),
    (80,0,0,1,0),
])
def test_idletocam(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in IDLE mode
    actual_state = 'IDLE'
# WHEN: battery charge is greater than 70% and image flag is true and error flag is false
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag] 
# THEN: satellite change to CAM mode
    assert change_mode(actual_state,config_vector) == 'CAM'
    
# SCENARIO: The satellite as operational mode, wants to reduce the tumbling, in order to stabilized the satellite.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,2,0,0,0),
    (90,2,0,0,0),
    (80,2,0,0,0),
])
def test_idletodetumbling(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in IDLE mode
    actual_state = 'IDLE'
# WHEN: battery charge is greater than 70% and the angular rate is greater than 1°/sec
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite change to DETUMBLING mode
    assert change_mode(actual_state,config_vector) == 'DETUMBLING'
    
# SCENARIO: The satellite as operational mode, wants to prepare the operation, in order remain prepared.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,0,0,0),
    (90,0,0,0,0),
    (80,0,0,0,0),
])
def test_idletoidle(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in IDLE mode
    actual_state = 'IDLE'
# WHEN: battery charge is greater than 70% and (no flags are true or angular rate is lesser than 1°/sec)
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite stays in IDLE mode
    assert change_mode(actual_state,config_vector) == 'IDLE'
    
# SCENARIO: The satellite as operational mode, wants to return from downlink mode, in order to be prepared for new tasks.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,0,0,0),
    (90,0,0,0,0),
    (80,0,0,0,0),
])
def test_downlinktoidle(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in DOWNLINK mode
    actual_state  = 'DOWNLINK'
# WHEN: battery charge is greater than 70% and downlink flag is false and error flag is false
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite change to IDLE mode
    assert change_mode(actual_state,config_vector) == 'IDLE'
    
# SCENARIO: The satellite as operational mode, wants to deactivate the onboard camera, in order to be prepared for new tasks.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,0,0,0),
    (90,0,0,0,0),
    (80,0,0,0,0),
])
def test_camtoidle(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in CAM mode
    actual_state = 'CAM'
# WHEN: battery charge is greater than 70% and downlink flag is false and error flag is false
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite change to IDLE mode
    assert change_mode(actual_state,config_vector) == 'IDLE'
    
# SCENARIO: The satellite as operational mode, wants to retunr from detumbling mode, in order to prepared for new tasks.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,0,0,0),
    (90,0,0,0,0),
    (80,0,0,0,0),
])
def test_detumblingtoidle(batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the satellite is in DETUMBLING mode
    actual_state = 'DETUMBLING'
# WHEN: battery charge is greater than 70% and the angular rate is lesser than 1°/sec and error flag is false
    config_vector = [batt,ang_rate,down_flag,img_flag,error_flag]
# THEN: satellite change to IDLE mode
    assert change_mode(actual_state,config_vector) == 'IDLE'
    
# FEATURE: satellite pointing
    
# SCENARIO: the satellie as object, wants to point to the sun, in order to recharge its batteries
@pytest.mark.parametrize("actual_state",[
    ('SAFE'),
    ('IDLE'),
])
def test_sunpointing(actual_state):
# GIVEN: satellite in SAFE mode or IDLE mode
    actual_state = actual_state
# WHEN: error flag is false
    error_flag = 0
# THEN: satellite is SUN-POINTING
    assert pointing(actual_state,error_flag) == 'SUN'
        
# SCENARIO: the satellite as object, wants to point to Nadir, in order to iamge an area
@pytest.mark.parametrize("actual_state",[
    ('CAM'),
])
def test_nadirpointing(actual_state):
# GIVEN: satellite in CAM mode
    actual_state = actual_state
# WHEN: error flag is false
    error_flag = 0
# THEN: satellite is NADIR-POINTING
    assert pointing(actual_state,error_flag) == 'NADIR'
    
# SCENARIO: the satellite as object, wants to point to ECI target, in order to contact a GS
@pytest.mark.parametrize("actual_state",[
    ('DOWNLINK'),
])
def test_ecipointing(actual_state):
# GIVEN:  satellite in DOWNLINK mode
    actual_state = actual_state
# WHEN: error flag is false
    error_flag = 0
# THEN: satellite is ECI TARGET-POINTING
    assert pointing(actual_state,error_flag) == 'ECI'

    
# SCENARIO: the satellite as object, wants to stop poining, in order to detumble
@pytest.mark.parametrize("actual_state",[
    ('DETUMBLING'),
])
def test_nopointing(actual_state):
# GIVEN: satellite in DETUMBLING
    actual_state = actual_state
# WHEN: error flag is false
    error_flag = 0
# THEN: POINTING is not applicable
    assert pointing(actual_state,error_flag) == 'NA'
    
############################################################
# END of the TESTS
############################################################