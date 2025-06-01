# Project Library API 

## 1. General description

### Project is designed for the Library functionality and allows to scale up for several libraries if it will be needed

#### Project includes several models, which are interacting with each other to keep updated info flow between labrary and clients.
#### All data is stored in the database postgres, notification for clients are peformed with Celery and Celery Beat.

#### External server operations are performed by Nginx

#### API has different level of access, limitations to take books and all historical orders are archived in separate table

## 2. Models

### There are models 11, describing library functionality

### Books app
#### - Library

#### - Author
#### - BookGenre
#### - BookFeature 
- gives fixed options (Status Choice)
#### - BookGeneral (FK Library, FK Author, FK Genre)
- gives general description about a book, having in the mind, that different editions of the same book can be linked to BookGeneral
#### - BookDetail (FK BookGeneral, FK User, FK Feature)
- gives detail description of particular book, including user, who is taking, prolonging and returning the book
#### - BookVolume (FK BookDetail)
- gives details about particular volume, if book is written in several volumes 
#### - BookFinance (OnetoOne BookDetail)
- gives finance description about a book, keeps calculation in case of overdue
#### - BookContent (FK BookDetail)
- gives content of the book (optional)
#### - Archive (FK BookDetail)
- keeps all history about particular book. Who take it, when, prolong, return date, overdue, overdue paymen
### Users app
#### - User
- gives info about user, including user card (automatically generated), tg credentials (optional)

#### Database are prepopulated with users and books on command

     python3 manage.py add_database

#### Database are prepopulated with admin on command
     python3 manage.py createadmin
## 3. Permission
#### - Library
- CRUD - admin
#### - Author
- Create, Update, Delete - Librarian 
- Retrieve, List - All
#### - BookGenre
- CRUD - Librarian
#### - BookFeature 
- CRUD - admin
#### - BookGeneral
- CRUD - Librarian
#### - BookDetail
- Create - Librarian
- List - Librarian, Admin
- UseList - User
- PublicList - all
- Retrieve - Librarian, Admin
- RetrieveUser - User
- RetrievePublic - all
- Update, Delete - Librarian
#### - BookVolume
- CRUD - Librarian
#### - BookFinance
- CRUD - admin
#### - BookContent
- CRUD - Librarian
#### - Archive
- List - Librarian, Admin
- UseList - User

#### - User
-

### All views are added with Ordering, Filtering, Search functions

## 3. Logic
### All logic operations happen in Validator IsBookTaken
#### Main logics
- User cannot have more than 4 books on hands
- User can prolong one book only two times
- User cannot take any book if at least one book on hand is overdue
- User cannot take any book, which is now at another user

#### The process of taking a book is under path book_client-update
#### Only Librarian can do it. Firstly chosen a particular book and then either choosing user or choosing null, in case book is returned

#### Archiving logic
- All orders are kept separately in Archive
- When book is taken or prolonging or returning, several tables are updated accordingly
- BookDetail, BookFinance keep current info (on-line) who is having now book, how long, how many times book prolonged, when is due date
- Archive keeps only what already happened

#### Overdue logic
- When overdue happened, automatically days are started to be calculated, fee summ is calculating every day
- Due date and fees are calculated depending on BookFeature
- If book is overdue, the return is possible, when needed fees are paid. This is reflected in Archive
- After book is returned, it becomes available for order for the next client 

#### Notification logic
- User gets notification when book is taken (with due date), when book is prolonged (with new due date), when book is returned
- In addition to that notification comes 3 and 1 day before due date
- When due date happens, user gets a message, informing about due date and fee per day
- All communication goes via email or TG BOT (optional)
#### Celery and Celery Beat
- Some logic and notification happens via Celery
- ALl fees calculation, overdue days calculation, info about coming soon overdue performs by Celery Beat 

## Start project
   1) Create a directory 


            mkdir <directory_name>


1) Copy docker-compose.yml (branch pre_develop) to your directory

2) Set there file .env (or copy .env_sample)


            touch .env

3) Open .env for adding variables


       nano .env


5) Insert next variables


SECRET_KEY=     

DEBUG=True  


POSTGRES_DB=test_library

POSTGRES_USER=postgres  

POSTGRES_PASSWORD=postgres  

POSTGRES_HOST=db  

POSTGRES_PORT=5432  


BOT_TOKEN=


CELERY_BROKER_URL=redis://redis:6379/0

CELERY_RESULT_BACKEND=redis://redis:6379/0

EMAIL_HOST=      

EMAIL_PORT=     

EMAIL_HOST_USER=

EMAIL_HOST_PASSWORD=

EMAIL_USE_TLS=


EMAIL_USE_SSL=


To generate SECRET_KEY


    tr -dc 'A-Za-z0-9!#$%&\()*+,-./:;<=>?@[\]^_{|}~' </dev/urandom | head -c 50  ; echo


To generate BOT_TOKEN follow instructions here https://t.me/BotFather

To set up variables for email follow instruction here https://yandex.ru/support/mail/mail-clients/others.html#smtpsetting
6) Insert command in the terminal


       docker compose up --build


6) If container library_celery_beat does not get connection to the postgres (log error "connection to server at "db" (172.18.0.3), port 5432 failed: Connection refused

        Is the server running on that host and accepting TCP/IP connections?

7) stop the container  start it again


       docker stop final_task_celery_beat


       docker start final_task_celery_beat


5) App is available

http://51.250.46.204/books/public/



9) To stop the programme


            docker stop $(docker ps -aq)


5) To start the programme again


            docker start $(docker ps -aq)


6) To remove all containers


            docker compose down


#### If you want to receive reminder via Telegram


#### Add your user profile http://51.250.46.204/user/create/


1) Find out you Telegram ID (e.g via @userinfobot)

2) Add field telegram_chat_id (Telegram ID) when you creating your profile 


#### Project documentation is placed 


http://51.250.46.204/swagger/


LINKs, Finalize README, push to Github (new SERVER API in Actions))