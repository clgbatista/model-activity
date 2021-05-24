# testing_cases.py
# @clgbatista - May 2021

# SCENARIO: The satellite as operational mode, wants to not change mode, in order to not allow trasitions.
@pytest.mark.parametrize("batt,ang_rate,down_flag,img_flag,error_flag",[
    (100,0,1,0,0),
])
def test_fi_detumbling(actual_state,batt,ang_rate,down_flag,img_flag,error_flag):
# GIVEN: the sattelite is in DETUMBLING mode
    actual_state = 'DETUMBLING'
# WHEN: downlink flag is true
    config_vector = (batt,ang_rate,down_flag,img_flag,error_flag)
# THEN: satellite stays in DETUMBLING mode
    assert change_mode(actual_state,config_vector)