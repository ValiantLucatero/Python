# -*- coding: utf-8 -*-
"""Este modulo nos servirá para usar Fibonacci"""
__module__="Fibonacci"
__author__="Alan Garrido"
__copyright__="Copyright (c) 2016, Proteco"

def Fibonacci(n):
	"""Imprime la serie de Fibonacci hasta antes de n"""
	a,b=0,1
	while b<n:
		print(a,end=' ')
		a,b=b,a+b
	print()

def Fibonacci2(n):
	lista=[]
	a,b=0,1
	while b<n:
		lista.append(a)
		a,b=b,a+b
	return lista