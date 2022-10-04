# GreenScore Python Django Application Server 

## Structure of the server

### Configuration
Edit server configuration in */greenscore_server/settings.py*  
Edit url redirections in */greenscore_server/urls.py*  
The rest in */greenscore_server/* are just boilerplate files  

### Managing
run server commands with */manage.py*

### Apps

The functionality of the server is broken into several apps.

#### statsnyc 
The statsnyc app contains models (Django's framework for handling databases) imported from our RDS statsNYC database  
The statsnyc app will serve to fetch data from the database  
  
Edit url redirections in */greenscore_server/statsnyc/urls.py*  
Edit admin site in */greenscore_server/statsnyc/admin.py*  
Edit models(database) in */greenscore_server/statsnyc/models.py*  

The rest is boilerplate  

## Testing

Run the server locally with *python3 manage.py runserver*  

So far you can do http requests as such:  
*http://localhost:8000/statsnyc/greeninfra/?lat=40.703234573353875&lng=-73.744505292328*  
*http://localhost:8000/statsnyc/airq/?place=Bronx*  
  