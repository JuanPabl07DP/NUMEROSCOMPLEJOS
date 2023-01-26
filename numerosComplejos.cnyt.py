#Juan Pablo Daza Pereira
#2023

import math

def addition(c1, c2):
    """ La función suma recibe dos números complejos y retorna un único número complejo (suma de la parte real y
    la suma de la parte imaginaria) """
    return [c1[0] + c2[0], c1[1] + c2[1]]


def subtraction(c1, c2):
    """ La función resta recibe dos números complejos y retorna un único número complejo (resta de la parte real y
    la resta de la parte imaginaria) """
    return [c1[0] - c2[0], c1[1] - c2[1]]


def product(c1, c2):
    """ La función producto recibe dos números complejos [a,b] y [c,d] y retorna un único número complejo""" 
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, imaginario]


def division(c1, c2):
    """ La función división recibe dos números complejos y retorna un único número complejo (operación a/b) """
    num = producto(c1, conjugado(c2))
    denomi = producto(c2, conjugado(c2))
    real = num[0] / denomi[0]
    imaginario = num[1] / denomi[0]
    return [real, imaginario]


def conjugate(c1):
    """ La función conjugado recibe un número complejo y retorna un número complejo (halla el conjugado de un número complejo) """
    return [c1[0], c1[1]*-1]


def module(c1):
    """ La función modulo recibe un número complejo y retorna el modulo de un número complejo """
    return math.sqrt(c1[0]**2 + c1[1]**2)



def cartesian_polar(c1):
    """ La función cart_pol recibe un número complejo y retorna la operación de cartesianas a polares """
    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angle = math.degrees(math.atan2(c1[1], c1[0]))
    return [r, angle]


def polar_cartesian(c1):
    """ La función pol_cart recibe un número complejo y retorna la operación polares a cartesianas (coordenadas X y Y) """
    r, angle = c1[0], math.radians(c1[1])
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]


def phase(c1):
    """ La función fase recibe un número complejo y retorna la fase de un número complejo """
    return math.degrees(math.atan2(c1[1], c1[0]))
