FEATURE: satellite pointing
    
    SCENARIO: the satellie as object, wants to point to the sun, in order to recharge its batteries
        GIVEN: satellite in SAFE mode or IDLE mode
        WHEN: error flag is false
        THEN: satellite is SUN-POINTING
        
    SCENARIO: the satellite as object, wants to point to Nadir, in order to iamge an area
        GIVEN: satellite in CAM mode
        WHEN: error flag is false
        THEN: satellite is NADIR POINTING
    
    SCENARIO: the satellite as object, wants to point to ECI target, in order to contact a GS
        GIVEN:  satellite in DOWNLINK mode
        WHEN: error flag is false
        THEN: satellite is ECI TARGET-POINTING
    
    SCENARIO: the satellite as object, wants to stop poining, in order to detumble
        GIVEN: satellite in DETUMBLING
        WHEN: error flag is false
        THEN: POINTING is not applicable