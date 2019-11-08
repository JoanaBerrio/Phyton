#!/usr/bin/env python3
from goto import with_goto
@with_goto  # Decorador necesario.

class mi_calculadora:
    a=0
    b=0
    resultado=0
    tareas_definidas = ['+', '-', '/', '*']
    def defineA(self,entrada): self.a=float(entrada);#print(self.a)
    def defineB(self,entrada): self.b=float(entrada);#print(self.b)
    def defineTrabajo(self,tarea): 
       #index=self.tareas_definidas.index(tarea);
        if tarea=='+':
            resultado=self.a+self.b;
            print(resultado);
        elif tarea=='-':
            print(self.a-self.b);
        elif tarea=='*':
            print(self.a*self.b);
        elif tarea=='/':
            print(self.a/self.b);
        else:
            print("Esandako lana ez dago definitua");
def main():
    print('Ongi etorri nire kalkulagailura:');
    mi_calculator=mi_calculadora();
    label .init_calculator  # Definir porción del código.
    mi_calculator.defineA(input('Sartu lehenengo parametroa: '));
    mi_calculator.defineB(input('Sartu bigarren parametroa: '));
    mi_calculator.defineTrabajo(input('Zer egin behar da? (+,-,/,*): '));
    fin=input('Beste eragiketa bat egin behr dozu? (B/E): ');
    if fin =='B':
       goto .init_calculator  # Regresar a get_input.
    else:
        print('Agur');
if __name__=='__main__':main()
