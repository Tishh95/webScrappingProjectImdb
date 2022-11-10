
# PROJET DE WEBSCRAPING DU SITE IMDB

le projet est écrit en python 

les Packages utilisé sont:

1. beatifulsoup4
2. flask
3. pandas
4. pymongo
5. requests
6. openpyxl
7. jupyter notebook

La base de donnée: Mongo

front: html/css

## Pour lancer le projet 

il faut entrer les commandes suivantes:
```` bash
sudo docker-compose build
````   

```` bash
sudo docker-compose up
````   

Pour entrer directement dans la base de données mongo sous docker 

```` docker
sudo docker exec -it <nom du container> mongosh -u root -p root
````
Pour quitter le container
```` mongosh
exit ou ctrl + c
````

# Construction du dataset 

Pour le dataset nous récuperons

- Les noms des films
- les années de parutions
- les crews 
- le rating imdb
- le rang du film sur imdb 


