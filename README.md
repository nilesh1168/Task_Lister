# Task Lister
## My First Web Application in Python-Flask.
### Description
> 1. This is a basic web application, which allows the user to login and create tasks/to-do items.
> 2. User creates task by entering the task heading, task description and the deadline *(till when the task is to be completed)* . 
> 3. The user can **update, delete** the tasks accordingly. The application also sends ***email notification*** to the registered email about the deadline of the task. 


### Working
> - The user has to first register himself/herself using basic details like *email*.
> - Once the registration is complete the user gets a *Welcome Email*.
> - The user can the login and start creating tasks.
>     - *The user gets an email notification 24 hrs prior to the task deadline*.

### Preview
![Home Page](home.png "Home Page")
![New Task](task_new.png "New Task")
![Task](task.png "Task")


### Note
- In config.py use your own environment variables
    - database URL
    - Email  *(Mandatory for email notification)*
    - Password  *(Mandatory for email notification)*

| **Environment Variable** | **Description**                                       |
|---------------------------|-------------------------------------------------------|
| `SECRET_KEY`              | Secret key for your application                      |
| `MAIL_SERVER`             | Mail server for the email notifications              |
| `EMAIL`                   | Email address from which notifications would be sent |
| `EMAIL_TOKEN`             | Password for the email address account               |

### Setting Up Google SMTP for Sending Emails

If you are using a Google SMTP server for sending emails in your application, follow the steps below:

1. Log in to your Google account.
2. Navigate to [Google Account Settings](https://myaccount.google.com).
3. Go to **2-Step Verification** and enable it if not already enabled.
4. Access **App Passwords** from the security settings.
5. Provide a desired name for the app and click **Create**. This will generate a password for your application.
6. Copy the password displayed on the screen and use it as the value for the `EMAIL_TOKEN` environment variable in your application.
