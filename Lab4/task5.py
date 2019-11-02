from math import sqrt
from constMod import SpecificHeatW as C, OceanMass as Mo, OceanTemp
def EvolutionEnd (speed = 10**4, mass = 10**4): 
    """Расчет энергии столкновения астероида с Землей
    speed(m/s), mass(kg). Mo - масса океана, C - удельная теплоемкость воды
    OceanTemp - средняя температура мирового океана.
    """
    Q = (mass * speed**2) / 2
    temp = Q / (C * Mo)
    if temp + OceanTemp  < 100:
     speed =  sqrt(((100 - OceanTemp) * C * Mo * 2) / mass)
     print('To kill planet, Asteroid speed =', speed)
    else: print('Ocean have evaporated. YOU KILL THE PLANET’)

EvolutionEnd(20000, 6 * 10**22)