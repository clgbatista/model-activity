# modelexam.py
# @clgbatista - May 2021

# @function change_mode(str actual_state, int config_vector[5])
#            function to control the changes on the operational modes of a satellite
# @params::actual_state
#            variable that determines the actual state of the operational mode
# @params::config_vector
#            configuration vector with the entries and conditions of different measures or signal.
#            config_vector[0] - batt - battery cappacity in [%]
#            config_vector[1] - ang_rate - angular rate estimation from the onboard gyroscopes [°/min]
#            config_vector[2] - down_flag - doownlink flag: takes the value 0 or 1 based if the GS is visible or not
#            config_vector[3] - img_flag - imaging flag: takes the value 0 or 1 based if the imaging area is visible or not
#            config_vector[4] - error_flag - error flag: takes the value 0 or 1 based on errors in the ADCS.

def change_mode(actual_state,config_vector):
    
# getting the config vector
    batt = config_vector[0]
    ang_rate = config_vector[1]
    down_flag = config_vector[2]
    img_flag = config_vector[3]
    error_flag = config_vector[4]
    
# SAFE mode behaviour (HIGHEST priority)
    if (error_flag or batt <= 70):
        return 'SAFE'
    else:
        if (actual_state == 'SAFE'):
            return 'IDLE'
        
# IDLE mode behaviour
        elif (actual_state == 'IDLE'):
            if (ang_rate > 1):
                return 'DETUMBLING'
            elif (down_flag):
                return 'DOWNLINK'
            elif (img_flag):
                return 'CAM'
            else:
                return 'IDLE'
            
# DETUMBLING mode behaviour
        elif (actual_state == 'DETUMBLING'):
            if (ang_rate <= 1):
                return 'IDLE'
            else:
                return 'DETUMBLING'
            
# DOWNLINK mode behaviour
        elif (actual_state == 'DOWNLINK'):
            if (not down_flag):
                return 'IDLE'
            else:
                return 'DOWNLINK'

# CAM mode behaviour (LOWEST priority)
        elif (actual_state == 'CAM'):
            if (not img_flag):
                return 'IDLE'
            else:
                return 'CAM'

# @function pointing(str actual_state, int error_flag)
#            function to control the pointing of a satellite at the different operational modes
# @params::actual_state
#            variable that determines the actual state of the operational mode
# @params::error_flag
#            error flag takes the value 0 or 1 based on errors in the ADCS
           
def pointing(actual_state,error_flag):    
# error flag has the HIGHEST priority
    if (not error_flag):
        if (actual_state == 'IDLE' or actual_state == 'SAFE'):
            return 'SUN'
        elif (actual_state == 'CAM'):
            return 'NADIR'
        elif (actual_state == 'DOWNLINK'):
            return 'ECI'
        elif (actual_state == 'DETUMBLING'): # pointing is not applicable (NA)
            return 'NA'
    else:
        return 'ADCS FAULT'