# mode_transition.feature
# @clgbatista - May 2021

FEATURE: operational mode transitions

    SCENARIO: The satellite as operational mode, wants to deal with an issue, in order to recover from an fault.
        GIVEN: the satellite is at any mode
        WHEN: battery charge is equal or lesser than 70% or error flag is true
        THEN: satellite goes to SAFE mode
    
    SCENARIO: The satellite as operational mode, wants to prepare the operation, in order to enter in nominal operation.
        GIVEN: the satellite is in SAFE mode
        WHEN: battery charge is greater than 70% and error flag is false
        THEN: satellite change to IDLE mode
        
    SCENARIO: The satellite as operational mode, wants to send telemetries, in order to downlink data to GS.
        GIVEN: the satellite is in IDLE mode
        WHEN: battery charge is greater than 70% and downlink flag is true and error flag is false
        THEN: satellite change to DOWNLINK mode
    
    SCENARIO: The satellite as operational mode, wants to use the onboard camera, in order to image an area.
        GIVEN: the satellite is in IDLE mode
        WHEN: battery charge is greater than 70% and image flag is true and error flag is false
        THEN: satellite change to CAM mode
        
    SCENARIO: The satellite as operational mode, wants to reduce the tumbling, in order to stabilized the satellite.
        GIVEN: the satellite is in IDLE mode
        WHEN: battery charge is greater than 70% and the angular rate is greater than 1°/sec
        THEN: satellite change to DETUMBLING mode
        
    SCENARIO: The satellite as operational mode, wants to prepare the operation, in order remain prepared.
        GIVEN: the satellite is in IDLE mode
        WHEN: battery charge is greater than 70% and (no flags are true or angular rate is lesser than 1°/sec)
        THEN: satellite stays in IDLE mode
        
    SCENARIO: The satellite as operational mode, wants to return from downlink mode, in order to be prepared for new tasks.
        GIVEN: the satellite is in DOWNLINK mode
        WHEN: battery charge is greater than 70% and downlink flag is false and error flag is false
        THEN: satellite change to IDLE mode
    
    SCENARIO: The satellite as operational mode, wants to deactivate the onboard camera, in order to be prepared for new tasks.
        GIVEN: the satellite is in CAM mode
        WHEN: battery charge is greater than 70% and image flag is false and error flag is false
        THEN: satellite change to IDLE mode
        
    SCENARIO: The satellite as operational mode, wants to retunr from detumbling mode, in order to prepared for new tasks.
        GIVEN: the satellite is in DETUMBLING mode
        WHEN: battery charge is greater than 70% and the angular rate is lesser than 1°/sec and error flag is false
        THEN: satellite change to IDLE mode