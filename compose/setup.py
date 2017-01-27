
#Create the docker-compose file
from jinja2 import Template
from ConfigParser import ConfigParser
import urllib
import zipfile

DOMA_URL='http://www.matstroeng.se/doma/download.php?version='

config = ConfigParser()
config.readfp(open("settings.conf"))

def produceConfig():
    temp_file = open("template/docker-compose.yaml.j2")
    content = temp_file.read()

    settings = {}


    for key,val in config.items("DB"):
        print val
        settings[key] = val

    renderer = Template(content)
    res = renderer.render(settings)
    f = open("docker-compose.yaml", "w")
    f.write(res);
    f.close();

def getDoma():
    doma_version = config.get("Doma", "Version")
    durl = DOMA_URL + doma_version
    urllib.urlretrieve(durl, 'doma.zip')

    zip = zipfile.ZipFile("doma.zip")
    zip.extractall(path="code")


getDoma()


