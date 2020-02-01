import os
import pathlib

present_path=str(pathlib.Path().absolute())

os.chdir(present_path+"/elasticsearch")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------elasticsearch done--------------\n")

os.chdir(present_path+"/mysql")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------mysql done--------------\n")

os.chdir(present_path+"/hadoop")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------hadoop done--------------\n")

os.chdir(present_path+"/nginx")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------nginx done--------------\n")

os.chdir(present_path+"/postgresql")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------postgresql done--------------\n")

os.chdir(present_path+"/zookeeper")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------zookeeper done--------------\n")

os.chdir(present_path+"/cassandra")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------cassandra done--------------\n")

os.chdir(present_path+"/tomcat")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------tomcat done--------------\n")

os.chdir(present_path+"/mongodb")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------mangodb done--------------\n")

os.chdir(present_path+"/solr")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------solr done--------------\n")

os.chdir(present_path+"/kafka")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------kafka done--------------\n")

os.chdir(present_path+"/activemq")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------activemq done--------------\n")

os.chdir(present_path+"/websphere")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------websphere done--------------\n")

os.chdir(present_path+"/ceph")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------ceph done--------------\n")

os.chdir(present_path+"/jboss")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------jboss done--------------\n")

os.chdir(present_path+"/hbase")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------hbase done--------------\n")


"""
os.chdir(present_path+"/weblogic")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------weblogic done--------------\n")

os.chdir(present_path+"/apache")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------apache done--------------\n")

os.chdir(present_path+"/kafkaconsumer")
mycmd= 'sudo docker-compose stop'
os.system(mycmd)
print("-----------kafkaconsumer done--------------\n")

"""

