
# Exam app 

This project is a system to manage student grades.



## Environment Variables

Before you start, you must supply enviroment variables. I give you freedom to complete the .env file. **Some variables are options as long as you run the app in _dev_ mode**; because in dev, the database is sqlite.

`SECRET_KEY` 

`DEBUG`

`POSTGRES_DB` 'optional'

`POSTGRES_USER` 'optional'

`POSTGRES_PASSWORD` 'optional'

`POSTGRES_HOST` 'optional'

`POSTGRES_PORT` 'optional'
## Usage

To deploy this project run with docker.

```bash
  docker build -t exam-app .
  docker run -t -i -p 8000:8000 exam-app 
```

or if you prefer, docker compose.

```bash
  docker-compose build
  docker-compose up
```

or if you prefer "old school". 🤔

```bash
  python manage.py migrate --settings=core.settings.dev
  python manage.py runserver --settings=core.settings.dev
```


## Documentation API's

Please go to this link [Swagger](http://localhost:8000/swagger/) or [Redoc](http://localhost:8000/redoc/)


## About development

### Use Case

It's a simple use case. 

![Logo](https://raw.githubusercontent.com/Corrales368/technical-test/main/use%20case.png)

### About the folder structure

The folder structure is a very typical one, where there is a container folder that stores the "apps", including an app, called shared, as its name indicates, I store things in common, or shared. The main app is core.

The project has 5 subapplications authentication, exam, shared, student and user. This separating the logic.

![Logo](https://raw.githubusercontent.com/Corrales368/technical-test/main/arquitech.png)


### Do you want to know my backoffice?
I have nothing to show on this occasion, it was a couple of lined notebook pages. I prefer to write ideas by hand than digitally

### About database

The tables created for the project are highlighted here.

- User
- Student
- Exam
- Question
- Answer
- AnswerStudent

![Logo](https://raw.githubusercontent.com/Corrales368/technical-test/main/database_exam_app.png)




## Feedback

If you have any feedback, please reach out to us at santi368444110@gmail.com

