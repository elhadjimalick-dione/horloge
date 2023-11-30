import time

en_pause = False
pause_applied = False 

# aller plus loin
def mettre_en_pause(duree):
    global en_pause, pause_applied
    if not pause_applied:  
        en_pause = True
        print("Horloge en pause pendant {} secondes.".format(duree))
        time.sleep(duree)
        en_pause = False
        pause_applied = True  
        print("Reprise de l'horloge.")
# aller plus loin
def différents_modes(heure, minute, seconde, mode_24_heures=True):
    if mode_24_heures:
        heure_format = "{:02d}:{:02d}:{:02d}".format(heure, minute, seconde)
    else:
        if heure >= 12:
            heure_format = "{:02d}:{:02d}:{:02d} PM".format(heure - 12 if heure > 12 else heure, minute, seconde)
        else:
            heure_format = "{:02d}:{:02d}:{:02d} AM".format(heure if heure > 0 else 12, minute, seconde)

    return heure_format

mode_24_heures = input("Voulez-vous utiliser le format 24 heures ? (Oui/Non) ").lower() == 'oui'


heure_choisie = différents_modes(16, 30, 0, mode_24_heures)
print(heure_choisie)
 

def afficher_heure(heure_actuelle, nouvelle_heure, mode_24_heures=True):
    if mode_24_heures:
        heure_actuelle_format = différents_modes(heure_actuelle[0], heure_actuelle[1], heure_actuelle[2], True)
    else:
        heure_actuelle_format = différents_modes(heure_actuelle[0], heure_actuelle[1], heure_actuelle[2], False)

    print(heure_actuelle_format)

    
    nouvelle_seconde = (heure_actuelle[2] + nouvelle_heure[2]) % 60
    nouvelle_minute = heure_actuelle[1] + nouvelle_heure[1] + (heure_actuelle[2] + nouvelle_heure[2]) // 60
    nouvelle_heure_result = heure_actuelle[0] + nouvelle_heure[0] + nouvelle_minute // 60
    nouvelle_heure_result = nouvelle_heure_result % 24
    nouvelle_minute = nouvelle_minute % 60
    nouvelle_seconde = nouvelle_seconde % 60
    
    if (nouvelle_heure_result, nouvelle_minute, nouvelle_seconde) != heure_actuelle:
        heure_format = différents_modes(nouvelle_heure_result, nouvelle_minute, nouvelle_seconde, mode_24_heures)
        
    
    return (nouvelle_heure_result, nouvelle_minute, nouvelle_seconde)

def regler_alarme(nouvelle_heure_alarme, mode_24_heures=True):
    heure_alarme_format = différents_modes(nouvelle_heure_alarme[0], nouvelle_heure_alarme[1], nouvelle_heure_alarme[2], mode_24_heures)
    print("Alarme réglée à :", heure_alarme_format)
    return nouvelle_heure_alarme

def verifier_alarme(heure_actuelle, heure_alarme):
    if heure_actuelle == heure_alarme:
        print("Réveil ! L'heure de l'alarme est atteinte.")
        return True  
    return False

heure_alarme = regler_alarme((16, 31, 0), mode_24_heures)
heure_actuelle = (16, 30, 0)

while True:
    heure_actuelle = afficher_heure(heure_actuelle, (0, 0, 1), mode_24_heures)
    if heure_actuelle >= (16, 30, 25) and not en_pause:
        mettre_en_pause(5)
    if verifier_alarme(heure_actuelle, heure_alarme):
        break  
    time.sleep(1)