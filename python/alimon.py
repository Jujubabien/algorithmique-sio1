#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
##############################################################################
#
# ALiMon.py : A LInux MONitor
#
##############################################################################
#
# Ce script réalise différentes opérations de monitoring et met en évidence 
# certains points importants comme une partition disque bientôt pleine ou une
# charge processeur trop élevée.
#
# Ce script a été réalisé durant une scéance de travaux pratiques et a des fins
# didactiques. Il est issu du travail collectif des personnes citées ci-dessous
# en auteurs et a nécessité uniquement deux heures de développement.
# 
##############################################################################
# 
# Auteurs :
#
# David BISPO, Christophe CARLIER, Jonathan DUHAIL, Jonathan GAULUPEAU,
# Lahoucine HAMOUCHE, Hicham OUHNA, Manuel PIRES, Yann VAITILINGOM,
# Jérémy PELLAUMAIL et Alexandre GUY
#
# Nous remercions également les connectés du canal #afpy du réseau Freenode
# pour leur aide concernant l'unicode et l'encodage utf-8.
#
# Version : 0.3
#
##############################################################################
#
# Ce script est diffusé sous la licence EUPL v1.1
#
# This script is released under EUPL v1.1
#
# http://ec.europa.eu/idabc/eupl
#
##############################################################################
#
# Ce programme est un logiciel libre ; vous pouvez le re-distribuer et/ou le
# modifier au titre des clauses de la European Union Public Licence (EUPL) 
# version 1.1, telle que publiée par l'Union Européenne.
#
# Ce programme est distribué dans l'espoir qu'il sera utile, 
# mais SANS AUCUNE GARANTIE ; sans même une garantie implicite de 
# COMMERCIABILITÉ ou DE CONFORMITÉ À UNE UTILISATION PARTICULIÈRE. 
# Voir la EUPL version 1.1 pour plus de détails.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the European Union Public Licence (EUPL) version 1.1 
# as published by the European Union.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the EUPL version 1.1 for more details.
#
##############################################################################
#
# Utilisation manuelle : ./alimon.py
#
# Utilisation automatisée : Rajouter dans le cron :
# 55 23 * * * root alimon.py
#
##############################################################################


#########################################
#### Configuration & pré-traitements ####
#########################################


#### Modules importés ####
import commands, unicodedata, os, sys, getopt


#### Fonction Affichage du titre formaté ####
def titre(message):
  message = unicode(message,'utf-8')
  print "\n", "#" * 59
  print "######", message.center(45).encode('utf-8'), "######"
  print "#" * 59, "\n"


#### Fonction affichant l'aide ####
def usage():
  print "###### Aide de alimon ######"
  print "./alimon.py [-f] [-d] [-h]"
  print "   -f	Lance le programme en mode dégradé. Utile si certaines commandes"
  print "	ne sont pas installées sur le serveur."
  print "   -d	Lance le programme en mode debug."
  print "   -h	Affiche l'aide du programme."


#### Variables globables ####
# Active / désactive le mode debug
debug = 0
# Active / désactive le mode dégradé
force = 0
# Seuil maxi du loadavg
seuil_maxi_loadavg = 1.0
# Température maxi des disques durs
temperature_hdd_maxi = 45
# Taux d'occupation maxi des disques durs
taux_occupation_maxi = 80
# Logins autorisés
loginsok = ['alex', 'jo']
# Liste des daemons qui doivent être en cours d'exécution
proclist = ['sshd', 'apache2', 'mysqld', 'named', 'master', 'murmurd', 'pop3-login', 'teamspeak-serve', 'couriertcpd']
# Pourcentage maxi de swap
pourcentage_mem_maxi = 10
# Mémoire mini disponible en Mo
mem_mini = 200
# Liste des sites à 'pinguer'
url_ping = ['www.google.fr']
# Liste des périphériques RAID (exemple : ['md0', 'md1'])
raidlist = []


#### Récupère les arguments ####
# Récupère la liste des arguments
try:
    optlist, list = getopt.getopt(sys.argv[1:], 'dhf')
# Si un argument ne figure pas dans la liste prédéfinie, affiche la fonction 'usage' (aide) puis quitte
except getopt.GetoptError:
    usage()
    sys.exit(1)
# Traite les arguments donnés
for opt in optlist:
  if opt[0] == '-h':
    usage()
    sys.exit(0)
  if opt[0] == '-d':
    debug = 1
  if opt[0] == '-f':
    force = 1


#### Test de présence des commandes shell et récupération de leur chemin ####
commandes_utilisees = ['cat','hostname','last','hddtemp','df','ps','free','ping','grep','uniq','who','uname']
# Contrôle la commande 'mdadm' uniquement si une liste de disques raid est définie
if raidlist:
  commandes_utilisees.append('mdadm')
commandes = {}
for comm in commandes_utilisees:
  (res,commande) = commands.getstatusoutput("/usr/bin/which %s" % comm)
  # Si une commande n'existe pas mais que le mode Force est activé
  if res and force:
    print "La commande", comm, "n'est pas présente sur votre système, fonctionnement en mode dégradé."
    commandes[comm] = ""
  # Si une commande n'exite pas
  elif res:
    print "La commande", comm, "n'est pas présente sur votre système. Arrêt du programme."
    print "Tapez './alimon.py -h' pour en savoir plus."
    sys.exit(1)
  else:
    commandes[comm] = commande


#### Récupération de la liste des disques durs ####
result = commands.getoutput("%s /proc/partitions" % commandes['cat']).split("\n")
result.pop(0)
hddlist = []
for ligne in result:
  if debug: print "debug> Ligne du fichier '/proc/partitions' en cours de traitement :", ligne
  hdd = ''.join(ligne.split()[-1:])[:3]
  if debug: print "debug> Disque dur à ajouter à la liste :", hdd
  if hdd and hdd not in hddlist:
    hddlist.append(hdd)



#############################
#### Programme principal ####
#############################


#### INFOS SERVEUR ####
if commandes['hostname'] and commandes['uname'] and commandes['cat'] and commandes['grep'] and commandes['uniq']:
  titre("Informations sur le serveur")
  # On récupère la première ligne du fichier /etc/issue qui contient généralement le nom et la version de la distribution Linux
  version = open("/etc/issue", "r").readlines()[0][:-1]
  if debug: print "debug> Version de la distribution :", version
  # On récupère le nom du serveur
  hostname = commands.getoutput(commandes['hostname'])
  if debug: print "debug> Hostname :", hostname
  print "Serveur %s sous %s" % (hostname, version)
  print
  # On récupère et affiche la version du noyau par la commande 'uname -r'
  print "Noyau Linux   :", commands.getoutput("%s -r" % commandes['uname'])
  # On récupère et affiche le(s) processeur(s) installé(s) sur le serveur
  cpu = commands.getoutput("%s /proc/cpuinfo | %s \"model name\" | %s" % (commandes['cat'], commandes['grep'], commandes['uniq']))
  if debug: print "debug> Liste des processeurs non post-traitée :", cpu
  print "Processeur(s) :", cpu.split(': ')[1]
  # On récupère et affiche la quantité de mémoire installée sur le serveur
  mem = commands.getoutput("%s /proc/meminfo | %s \"MemTotal\"" % (commandes['cat'], commandes['grep']))
  if debug: print "debug> Quantité de mémoire non post-traitée :", mem
  print "Mémoire vive  :", ' '.join(mem.split()[1:])


#### DUREE DE FONCTIONNEMENT DU SERVEUR ####
if commandes['cat']:
  titre("Durée de fonctionnement")
  # On récupère la durée de fonctionnement en secondes dans /proc/uptime
  result = commands.getoutput("%s /proc/uptime" % (commandes['cat'])).split()[0]
  duree = float(result)
  if debug: print "debug> Résultat de cat '/proc/uptime' :", duree
  # On calcule le reste en secondes
  secondes = duree%60
  if debug: print "debug> Secondes :", secondes
  # On calcule le reste en minutes
  minutes = duree/60%60
  if debug: print "debug> Minutes :", minutes
  # On calcule le reste en heures
  heures = duree/60/60%24
  if debug: print "debug> Heures :", heures
  # On calcule le nombre de jours
  jours = int(duree/60/60/24)
  if debug: print "debug> Jours :", jours
  print "Serveur lancé depuis %i jour(s), %i heure(s), %i minute(s) et %i seconde(s)." % (jours, heures, minutes, secondes)


#### VERIFICATION DU LOAD AVERAGE ####
if commandes['cat']:
  titre("Vérification du load average")
  # On appelle une commande Unix et on récupère le résultat dans la variable result
  result = commands.getoutput("%s /proc/loadavg" % (commandes['cat']))
  if debug: print "debug> Résultat de 'cat /proc/loadavg' :", result
  # On découpe la chaine de caractères en une liste selon le caractère espace
  liste_result = result.split()
  if debug: print "debug> La liste découpée :", liste_result
  if debug: print "debug> La première valeur de la liste :", liste_result[0]
  # On compare le load avg de la dernière minute avec le seuil maxi
  # Attention, on converti la chaine de caractère liste_result[0] en nombre flottant via float()
  if float(liste_result[0]) > seuil_maxi_loadavg:
    print "Alerte ! charge CPU supérieure à", seuil_maxi_loadavg, "!!!"
  else:
    print "Charge CPU %s normale car inférieure à %.2f" % (liste_result[0],seuil_maxi_loadavg)


#### CONNECTIONS DU JOUR ####
if commandes['last'] and commandes['grep']:
  titre("Connections du jour")
  # On récupère les dernières connections avec la commande 'last', on filtre avec 'grep'
  login = commands.getoutput("%s | %s \"$(LANG=C date +\"%%a %%b %%-d\")\"" % (commandes['last'], commandes['grep']))
  if login == "":
    login = commands.getoutput("%s | %s \"$(LANG=C date +\"%%a %%b  %%-d\")\"" % (commandes['last'], commandes['grep']))
  print login


#### TEMPERATURE DES HDD ####
if commandes['hddtemp']:
  titre("Températures des disques durs")
  # On vérifie la température pour chaque disque dans la liste 'hddlist' avec la commande 'hddtemp'
  for disque in hddlist:
    if debug: print "debug> Disque en cours de contrôle :", disque
    # On récupère la température du disque
    temperature = commands.getoutput("%s -n /dev/%s" % (commandes['hddtemp'], disque))
    if debug: print "debug> Température du disque en cours :", temperature
    # On vérifie que la température du disque n'est pas supérieure au seuil de tolérance, sinon on imprime un message d'alerte
    # S'il y a une erreur (disque non compatible SMART), on passe au disque suivant
    try:
      if int(temperature) > temperature_hdd_maxi:
	print "Alerte ! Le disque dur /dev/%s a dépassé %s°C, il est actuellement à %s°C !!!" % \
	  (disque, temperature_hdd_maxi, temperature)
      else:
	print "Le disque dur /dev/%s est à %s°C et inférieur au seuil de %s°C" % \
	  (disque, temperature, temperature_hdd_maxi)
    except:
      pass


#### VERIFICATION DE L'ESPACE DISQUE ####
if commandes['df'] and commandes['grep']:
  titre("Vérification de l'espace disque")
  # On récupère le pourcentage d'espace libre sur toutes les partitions dont le périphérique commence par '/dev' avec la commande 'df'
  result = commands.getoutput("%s -P | %s -e '^/dev'" %(commandes['df'], commandes['grep']))
  if debug: print "debug> Résultat du 'df' :", result
  # On fait un contrôle sur chaque ligne du résultat du 'df'
  for disque in result.split('\n'):
    taux_occupation = disque.split()[4][:-1]
    if debug: print "debug> Disque en cours de contrôle :", disque
    if debug: print "debug> Taux d'occupation du disque en cours :", taux_occupation
    # On vérifie que le taux d'occupation n'est pas supérieur au seuil de tolérance, sinon on imprime un message d'alerte
    if int(taux_occupation) > taux_occupation_maxi: 
      print "Attention la partition %s est rempli à %s !!!" %(disque.split()[0], disque.split()[4])
    else:
      print "La partition %s est pleine à %s." %(disque.split()[0], disque.split()[4])


#### VERIFICATION ETAT RAID ####
# Se lance si une liste de périphériques a été définie
if raidlist:
  if commandes['mdadm']:
    titre("Vérification de l'état du RAID")
    # On teste chaque périphérique de la liste
    for hddraid in raidlist:
      # On récupère le status de la commande qui vérifie l'état d'un RAID
      (raidstatus, raid) = commands.getstatusoutput("%s --detail -t /dev/%s" %(commandes['mdadm'], hddraid))
      # On teste si le status est différent de 0 (donc status en erreur)
      if raidstatus!=0:
	print "Attention, le périphérique RAID /dev/%s a au moins un disque en dysfonctionnement !" % hddraid
      else:
	print "Le périphérique RAID /dev/%s fonctionne normalement." % hddraid


#### VERIFICATION CONNECTIONS EN COURS ####
if commandes['who']:
  titre("Vérification des logins actuellement connectés")
  # On récupère les noms des utilisateurs actuellement connectés avec la commande 'who'
  wholiste = commands.getoutput(commandes['who']).split('\n')
  if debug: print "debug> Liste des utilisateurs connectés :", wholiste
  liste_logins_connectes = []
  # On récupère uniquement la première colonne de chaque ligne
  for ligne in wholiste: 
    if ligne:
      if debug: print "debug> Ligne en cours de traitement :", ligne
      user = ligne.split()[0]
      if debug: print "debug> Utilisateur en cours de traitement :", user
      # On ajoute l'utilisateur à une liste s'il n'y est pas déjà (évite les doublons)
      if user not in liste_logins_connectes:
	liste_logins_connectes.append(user)
  # On vérifie que les utilisateurs précédemment récupérés sont bien dans la liste des utilisateurs autorisés, sinon on imprime un message d'alerte
  for user in liste_logins_connectes:
    if user in loginsok:
      print "utilisateur", user, "OK"
    else:
      print "ATTENTION L'utilisateur", user, "est connecte MAIS n'est pas dans la liste"


#### VERIFICATION DES PROCESSUS ####
if commandes['ps']:
  titre("Vérification des processus")
  # On récupère les processus lancés avec la commande 'ps'
  result = commands.getoutput("%s -e" % (commandes['ps'])).split('\n')
  # On supprime la première ligne
  result.pop(0)
  if debug: print "debug> Résultat de la commande 'ps' :", result
  # On récupère uniquement le nom de chaque processus (dernière colonne)
  psliste=[]
  for processus in result:
    if debug: print "debug> Processus à ajouter :", processus
    psliste.append(processus.split()[-1])
  if debug: print "debug> Contenu de la liste des processus :", psliste
  # On vérifie que chaque processus de la liste définie au début du script est présent dans la liste récupérée précedemment
  for processus in proclist:
    if debug: print "debug> Processus en cours de vérification :", processus
    if not processus in psliste:
      print "Attention : le process %s n'est pas lancé actuellement !!!" %(processus)
    else:
      print "Le processus", processus, "est bien en cours d'exécution."


#### VERIFICATION DE LA MEMOIRE ####
if commandes['free']:
  titre("Vérification de la mémoire")
  # On récupère la quantité de mémoire libre avec la commande 'free'
  result = commands.getoutput(commandes['free'])
  if debug: print "debug> Résultat de la commande 'free' :", result
  listefree = result.split("\n")
  if debug: 
    print "debug> On truque le résultat de la commande free pour tester"
    listefree = ['             total       used       free     shared    buffers     cached', 'Mem:       2066032     850780    1215252          0     114496     368584', '-/+ buffers/cache:     367700    1698332', 'Swap:      2048276          350500    2048276']
    print "debug> Free truqué :", listefree
  # On récupère la quantité de mémoire totale
  ligne1=listefree[1].split()
  memoire=float(ligne1[1])
  if debug: print "debug> Mémoire totale :", memoire
  # On récupère la quantité de swap totale
  ligne3=listefree[2].split()
  swap=float(ligne3[1])
  if debug: print "debug> Swap total :", swap
  # On calcule le rapport de swap par rapport à la mémoire installée
  pourcentage = (swap/memoire)*100.0
  if debug: print "debug> Pourcentage de Swap :", pourcentage
  # On vérifie que le rapport ne dépasse pas le seuil limite autorisé, sinon on imprime un message d'alerte
  if pourcentage > pourcentage_mem_maxi:
    print "Alerte ! memoire swap supérieur a %d%% de la mémoire (utilisation %.2f%%) !!!" % (pourcentage_mem_maxi, pourcentage)
  else:
    print "Mémoire swap inférieure à %d%% (utilisation %.2f%%)" % (pourcentage_mem_maxi, pourcentage)
  # On récupère la quantité de mémoire libre en Mo avec la commande 'free -m'
  result = commands.getoutput("%s -m" % (commandes['free']))
  result = result.split('\n')
  if debug: print "debug> Résultat de la commande 'free -m' :", result
  mem = result[2].split()[3]
  if debug: print "debug> Quantité de mémoire libre en Mo :", mem
  # On vérifie que la quantité de mémoire libre ne soit pas inférieure au seuil limite, sinon on imprime un message d'alerte
  if int(mem) < mem_mini:
    print "Attention !! il reste moins de %sMo de mémoire libre !!! (%sMo)" %(mem_mini, mem)
  else:
    print "Il y a", mem, "Mo de mémoire libre."


#### TEMPS DE REPONSE SERVEUR WEB ####
if commandes['ping']:
  titre("Temps de réponse du serveur")
  # On lance la commande 'ping' sur chaque url définie dans 'url_ping'
  for url in url_ping:
    print "Résultat de la commande ping sur %s" % (url)
    print commands.getoutput("%s -c 1 %s" % (commandes['ping'], url)).split("\n")[-1]

print