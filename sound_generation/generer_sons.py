# Importation des bibliothèques
from scipy.io.wavfile import write
import numpy as np
import colorednoise as cn

# Générer un fichier audio de bruit brownien
def generer_bruit(nom_fichier, sample_rate, duree):
    
    #Génération bruit
    t = np.linspace(0, duree, int(sample_rate * duree), endpoint=False) 
    signal_bruit = cn.powerlaw_psd_gaussian(2, sample_rate * duree)  # 2 : brown noise  0 : white noise

    facteur = 40 
    signal_gauche = signal_bruit * facteur
    signal_droit = signal_bruit * facteur

    stereo_signal = np.column_stack((signal_gauche, signal_droit))

    # Normalisation
    valeur_max = np.max(np.abs(stereo_signal))
    if valeur_max > 1.0:
        stereo_signal /= valeur_max

    #Enregistrement
    write(nom_fichier, sample_rate, (stereo_signal * 32767).astype(np.int16))

# Calculer l'amplitude du signal carré utilisé pour les tons isochrones
def generer_amplitude(duree, amp_0, amp_1):
    t = np.linspace(0, duree, int(duree * 44100), endpoint=False)

    signal_carre = np.zeros_like(t)

    #Définition d'une période
    periode_carre = amp_0 + amp_1
    temps_carre = t % periode_carre
    signal_carre[temps_carre < amp_0] = 0
    signal_carre[(temps_carre >= amp_0) & (temps_carre < periode_carre)] = 1
    return signal_carre

# Générer un fichier audio de bruit brownien et d'isochronic tones
def generer_isochronic_tones_bruit(nom_fichier, sample_rate, duree, freq, amp_0, amp_1):
    dt = 1/ sample_rate
    number_times = int(duree / dt)
    t = np.linspace(0, duree, int(sample_rate * duree), endpoint=False)

    #Générer les tons isochrones
    amplitude = generer_amplitude(duree, amp_0, amp_1)
    signal = np.sin(2 * np.pi * freq * t)
    signal_tons = np.multiply(amplitude, signal)

    #Générer bruit brownien
    signal_bruit = cn.powerlaw_psd_gaussian(2, sample_rate * duree) # 2 : brown noise  0 : white noise

    # Combinaison des tons isochrones et du bruit
    facteur_tons = 0.05 
    bruit_facteur = 40 

    signal_gauche = (signal_tons * facteur_tons + signal_bruit * bruit_facteur)
    signal_droit = (signal_tons * facteur_tons + signal_bruit * bruit_facteur)
    stereo_signal = np.column_stack((signal_gauche, signal_droit))

    # Normalisation
    valeur_max = np.max(np.abs(stereo_signal))
    if valeur_max > 1.0:
        stereo_signal /= valeur_max

    #Enregistrement
    write(nom_fichier, sample_rate, (stereo_signal * 32767).astype(np.int16))


# Paramètres
duree = 540 # en secondes
frequence = 500  # en Hz
amp_0 = 0.05 # temps de pause
amp_1 = 0.05 # temps de son

# Générer les fichiers audio
generer_isochronic_tones_bruit('./isochronic_tones_bruit.wav', 44100, duree, frequence, amp_0, amp_1)
generer_bruit('./bruit.wav', 44100, duree)
