#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse, os
from urllib.request import urlopen
from bs4 import BeautifulSoup

os.system("rm -rf includes/js/index.js")
os.system("touch includes/js/index.js")
js = """angular.module("app",["ui.bootstrap","ngAnimate"]).factory("sortable",["$filter","$rootScope",function(e,r){return function(t,o,s,a){t.sortingOrder=a,t.reverse=!1,t.filteredItems=[],t.groupedItems=[],t.itemsPerPage=s,t.pagedItems=[],t.currentPage=1,t.items=o,t.maxSize=5;t.search=function(){t.filteredItems=e("filter")(t.items,r.query),""!==t.sortingOrder&&(t.filteredItems=e("orderBy")(t.filteredItems,t.sortingOrder,t.reverse)),t.currentPage=1,t.groupToPages(),t.totalItems=t.filteredItems.length},t.groupToPages=function(){t.pagedItems=[];for(var e=0;e<t.filteredItems.length;e++)e%t.itemsPerPage==0?t.pagedItems[Math.floor(e/t.itemsPerPage)]=[t.filteredItems[e]]:t.pagedItems[Math.floor(e/t.itemsPerPage)].push(t.filteredItems[e])},t.range=function(e,r){var t=[];r||(r=e,e=0);for(var o=e;o<r;o++)t.push(o);return t},t.search(),t.sort_by=function(e){t.sortingOrder==e&&(t.reverse=!t.reverse),t.sortingOrder=e,t.search()},t.sort_by(a),t.totalItems=t.filteredItems.length}}]).controller("main",["$scope","$rootScope","sortable",function(e,r,t){r.query="",e.gridToggle=!0,e.onQueryChange=function(t){r.query=t,e.search()},t(e,["""
arquivo = open('includes/js/index.js', 'r', encoding="utf8")
conteudo = arquivo.readlines()
conteudo.append(js)
arquivo = open('includes/js/index.js', 'w', encoding="utf8")
arquivo.writelines(conteudo)
arquivo.close()

def buscanoyoutube(result_term, categoria):
    dt = list()
    query = urllib.parse.quote(result_term)
    url = "https://www.youtube.com/results?q=" + query
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    
    for row in soup.find("div",{"class":"yt-lockup-content"}).find_all("a",{"class":"yt-uix-tile-link"}):
        titulo = row["title"] #TITULO DO VIDEO
        contador = 0
        
        while contador <= 0:
            
            for row in soup.find("ul",{"class":"yt-lockup-meta-info"}).find_all("a",{"class":"yt-uix-sessionlink"}):
                url = ('https://youtube.com' + row["href"]) #URL DA PLAYLIST
                respostaplaylist = urlopen(url)
                canal = respostaplaylist.read()
                playlis = BeautifulSoup(canal, "html.parser")
                
                for row in playlis.find("ul", {'class' : 'pl-header-details'}).find_all("a",{"class":"g-hovercard"}):
                    canalurl = ('https://youtube.com' + row['href']) # PEGA A URL DO CANAL
                    respostacanal = urlopen(canalurl)
                    entranocanal = respostacanal.read()
                    resultadocanal = BeautifulSoup(entranocanal, "html.parser")
                    
                    for row in resultadocanal.findAll("img", {'class' : 'channel-header-profile-image'}):
                        nomedocanal = (row['title']) # PEGA O NOME DO CANAL
                        
                        for row in resultadocanal.findAll("img",{"class":"channel-header-profile-image"}):
                            urlimg = row["src"] #PEGA O URL DA IMAGEM
                print("Web Crawling " + titulo + " feito com sucesso")
                json ="""{'name' : '%s',   'urlplay' : '%s', 'nomecanal' : '%s', 'urlcanal'  :   '%s', 'img'  :   '%s' },""" % (titulo,url,nomedocanal,canalurl,urlimg)
                arquivo = open('includes/js/index.js', 'r', encoding="utf8")
                conteudo = arquivo.readlines()
                conteudo.append(json)
                arquivo = open('includes/js/index.js', 'w', encoding="utf8")
                arquivo.writelines(conteudo)
                arquivo.close()
            contador += 1
            
def inicio():
    
    categorias = ["Python", "Zabbix", "Fedora FMS", "Windows Server 2012", "Windows Server 2016", "Linux", "LPI", "Docker", "PHP", "Java",".NET","C#","C++","MySQL","SQL","SQLServer", "amriaDB", "apache", "Redes", "Pentest", "Segurança da informação", "sqlmap", "nmap", "kali linux", "Google dorcks", "Inglês", "Advanced Pentest", "Análise Forense Computacional", "Nmap + NSE", "Shodan", "Vuln Scan", " Brute Force", "Metasploit""NodeJS", "AngularJS", "PHP", "Zend Framework", "CakePHP", "MongoDB", "React", "Redux",
             "Silex", "Slim", "Laravel", "Django", "Inglês", "Marketing", "Vagrant", "Jenkins", "Machine Learning", "Symfony", "Amazon AWS",
             "Ruby", "Ruby on Rails", "Elixir", "Clojure", "Git", "PHPunit", "Composer", "Bower"
             "Redis", "PostgreSQL", "Be MEAN"]

    try:
        for termos in categorias:
            buscanoyoutube("curso de " + termos, termos)
    finally:
        final = """{}],6,"updated_at")}]);"""
        arquivo = open('includes/js/index.js', 'r', encoding="utf8")
        conteudo = arquivo.readlines()
        conteudo.append(final)
        arquivo = open('includes/js/index.js', 'w', encoding="utf8")
        arquivo.writelines(conteudo)
        arquivo.close()
try:
    if __name__ == "__main__":
        inicio()
except KeyboardInterrupt:
    print("Parece que você finalizou o Web Crawling com Ctrl + C ou Esc.")


"""
.BIBLIOTEC DE VARIAVEIS
    titulo      = Titulo da Playlist
    url         = Link da playlist
    urlimg      = Link da imagem do canal
    nomedocanal = Nome do canal
    canalurl    = Link do canal

.JS
],6,"updated_at")}]);

"""
