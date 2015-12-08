# coding=utf-8
import os;
import random
import sys
from threading import Thread
import time

class Io:
     def testcapteur(self):
        print (os.system("gpio read 3"))



class Afficheur(Thread):
    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 200:
            sys.stdout.write(self.lettre+"aaaa")
            sys.stdout.flush()
             #attente += random.randint(1, 60) / 100
            attente = 0.2
            time.sleep(attente)
            i += 1