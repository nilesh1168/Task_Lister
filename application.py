from task_lister import application,db,mail
from task_lister.models import Task,User
from flask_mail import Message
import datetime, os
from apscheduler.schedulers.background import BackgroundScheduler
from task_lister.config import Config


def sensor():
    with application.app_context():        
        t = Task.query.filter_by(ddate = datetime.date.today()).all()
        if len(t) != 0: 
            for i in range(len(t)):
                u = User.query.filter_by(id = t[i].user_id).first()
                print(u.email)
                msg = Message(subject = 'Deadline',recipients = [u.email], body = "Your "+t[i].t_name+"'s Deadline is approaching soon i.e today.\n This mail is to inform that your task is still pending!!. If you have completed the task please delete the task from the list .\n ======== Daily Task Lister ========\nThank You!!!!",sender=Config.MAIL_USERNAME)
                mail.send(msg)
            print("Scheduler is alive!")
        else:
            print("Scheduler is dead!")    

if __name__ == "__main__":
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(sensor,'interval',hours=23)
    sched.start()
    application.run(debug=Config.IS_DEBUG)
