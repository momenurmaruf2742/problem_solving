from lib2to3.pgen2 import driver
from time import sleep
from datetime import time, datetime, timezone, timedelta
from typing import Tuple
begin_time = time(17,40)
end_time = time(17,45)
gmt = timezone(timedelta(hours=+6), 'GMT')
def check_current_time(begin_time:time, end_time:time) -> Tuple[time, bool]:
    '''
    Check current time is between 00:00 and 00:15. 
    Returns current time and if it is between begin and end time.
    '''
    dt_now = datetime.now(gmt)
    current_time = time(dt_now.hour, dt_now.minute, dt_now.second)
    return current_time, (begin_time <= current_time) and (current_time < end_time)

print(check_current_time(begin_time,end_time))

while True:
    if not is_during_running_time:
          print(f'Not Running the program. It is {current_time} and not between {begin_time} and {end_time}')
          # sleep less as the time gets close to the begin_time
          if current_time >= time(23,59,59):
            sleep(0.001)
          elif time(23,59,58) <= current_time < time(23,59,59):
            sleep(0.5)
          else:
            sleep(1)
          current_time, is_during_running_time= check_current_time(begin_time, end_time)
          continue
    # Step 2 goes here
    # Step 3 goes here

    try:
        print(driver.get("https://eticket.railway.gov.bd/booking/train/search?fromcity=Dhaka&tocity=Joypurhat&doj=06-Jun-2024&class=S_CHAIR"))
        # Step 3 goes here
        # elements[reservation_time-10].click()
    except Exception as e:
      print(e)
    finally:
        # close the drivers
        driver.quit()