import dli_controller
import valve_delegate
import sched
import time

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()



def water_seedlings() :
    # print("start seedling watering...")
    # valve_delegate.setRelayState("1100000000000000")
    # time.sleep(1)
    # dli_controller.set_pump_state(0, True)
    # print(dli_controller.get_all_states())
    # time.sleep(10)
    # dli_controller.set_pump_state(0, False)
    # time.sleep(1)
    # valve_delegate.setRelayState("0000000000000000")
    # print(dli_controller.get_all_states)
    # print("end seedling watering")
    print(valve_delegate.getRelayState())

def relay_soft_failsafe() :
    valve_delegate.setRelayState("0000000000000000")


scheduler.add_job(water_seedlings, 'cron', second=30)


scheduler.start()