from application.core.http import HTTPHandler
from application.core.scheduler import SchedulerHandler, SchedulerTasker
from application.controllers import *
from application.functions.simulated_data.get_reservations import *
from application.functions.simulated_data.get_properties import *
from application.functions.simulated_data.get_chats import *
from application.functions.web_scraping.get_properties_scraped import *
from application.functions.web_scraping.get_reservations_scraped import *


@HTTPHandler()
def api(event, context):
    return HTTPRouter.route_request(event, context)

@SchedulerHandler()
def scheduler(event, context):
    return SchedulerTasker.task_request(event, context)
    

