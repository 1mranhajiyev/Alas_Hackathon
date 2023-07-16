from pydantic import BaseModel
# 2. Class which describes mobile Notes measurements
class MobileNotes(BaseModel):
    battery_power:int
    blue:int
    clock_speed:float
    dual_sim:int
    fc:int
    four_g:int
    int_memory:int
    m_dep:float
    mobile_wt:int
    n_cores:int
    pc:int
    px_height:int
    px_width:int
    ram:int
    sc_h:int
    sc_w:int
    talk_time:int
    three_g:int
    touch_screen:int
    wifi:int

   