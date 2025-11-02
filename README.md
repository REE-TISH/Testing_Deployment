# comicBackend 

A full-stack web application to read manga and manhwa with **real-time group chat** functionality.  
Users can log in, join manga-specific groups, and chat while reading.

#Live/Demo
 [View Live Project]/(https://reetish-bookstore.vercel.app)

 ## 🛠️ Tech Stack
**Frontend:** React, TailwindCSS  
**Backend:** Django, Django REST Framework, Django Channels  
**Database:** PostgreSQL  
**Deployment:** Vercel (frontend), Render (backend)


##Installation (Local setup)

initialize git by typing 'git init' in terminal <br/>
git clone https://github.com/REE-TISH/comicBackend.git <br/>
cd comicBackend <br/>
python -m venv venv #Creates virtual Env <br/>
.\venv\scripts\activate #For Windows Activates Virtual Env<br/>
source venv/bin/activate #For Mac or Linus <br/>
pip install -r requirements.txt <br/>
python manage.py migrate <br/> 
python manage.py runserver<br/>


##Additional change 
if you want to add your personal DATABASE then you could pass the DATABASE_URL otherwise you could use default sqllite3 database by replacing DATABASE in settings.py in comicBackend By this :<br/>
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
 }





