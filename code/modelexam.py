# modelexam.py

def change_mode(actual_state,config_vector):
    
# getting the config vector
    batt = config_vector[0]
    ang_rate = config_vector[1]
    down_flag = config_vector[2]
    img_flag = config_vector[3]
    error_flag = config_vector[4]
    
# SAFE mode behaviour (HIGH )
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

# CAM mode behaviour
        elif (actual_state == 'CAM'):
            if (not img_flag):
                return 'IDLE'
            else:
                return 'CAM'

def pointing(actual_state,error_flag):
    if (not error_flag):
        if (actual_state == 'IDLE' or actual_state == 'SAFE'):
            return 'SUN'
        elif (actual_state == 'CAM'):
            return 'NADIR'
        elif (actual_state == 'DOWNLINK'):
            return 'ECI'
        elif (actual_state == 'DETUMBLING'):
            return 'NA'
    else:
        return 'ADCS FAULT'