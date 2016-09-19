#!/usr/bin/python
# MELEYCA CABRERA (UNEFA)
#ver: https://repl.it/DcQR/0
# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		nodo = self.__primero
		for i in range (self.__n):
			print nodo.info
			nodo=nodo.sig		
			
	def pos_actual (self, pos):

		nodo  = self.__primero
		cont = 0
		while (nodo != None) :
			
			if (cont == pos):
				self.__actual=nodo
				self.__pos=cont
				return self.__actual.info
			
			nodo = nodo.sig
			cont=cont+1
		return 
		

        # Metodo para buscar un elemento de la lista 
	def buscar_elem (self, valor):

		nodo  = self.__primero
		p = 0
		while (nodo != None) :
			if (nodo.info == valor):
				print p 
			
			nodo = nodo.sig
			p = p + 1
			
		return -1    


	def eliminar_primero(self):
		
		if (self.__primero == None):
			return None
		nodo = self.__primero
		self.__primero = nodo.sig
		if (nodo == self.__actual):
			
			self.__actual = nodo.sig
			
		if (self.__ultimo == nodo):
			
			self.__ultimo = None
			
		self.__n = self.__n - 1
		self.__pos = self.__pos - 1
		del nodo
			

	
# PRINCIPAL 

# Crea la lista de elementos
l = Lista()

# Inserta elementos en la lista 
l.insertar_actual(5);
l.insertar_actual(10);
l.insertar_actual(25);
l.insertar_actual(30);
l.insertar_actual(15);
l.insertar_actual(35);
l.mostrar()
l.eliminar_primero()
l.buscar_elem(15)
l.mostrar()
l.pos_actual(4)
print (l.pos_actual(4))raw_input()
