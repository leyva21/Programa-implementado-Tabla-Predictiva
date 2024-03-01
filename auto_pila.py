from tablaPredictiva import PredictTable
import re

terminales, no_terminales, tabla_predictiva = PredictTable()

#Parsing
#Clase para realizar el análisis sintáctico predictivo
class AutoPila:
    def __init__(self, input):
        self.input_string = re.findall(r'function|\(|\)|var|string|boolean|:|;|[a-z]|empty', input)
        self.pila = ["$", "S"] #Se comienza con el símbolo inicial de la gramática.
        self.recorrido = [] #Lista
        

    def analis(self):
        i = 0
        try:
            while len(self.pila) > 0 and i < len(self.input_string):
                arriba = self.pila[-1] # Obtiene el símbolo en la parte superior de la pila
                self.recorrido.append(self.pila[:])
                print(f"Pila:'{self.input_string[i]}': {' '.join(self.pila)}")
                if arriba in terminales: # Si el símbolo en la parte superior de la pila es terminal
                    if arriba == self.input_string[i]: #Compara
                        self.pila.pop()
                        i += 1
                    else:
                        return False
                elif arriba in no_terminales: # Si el símbolo en la parte superior de la pila es no terminal
                    if tabla_predictiva[arriba] is None or self.input_string[i] not in tabla_predictiva[arriba]: 
                        return False
                    else:
                        produccion = tabla_predictiva[arriba][self.input_string[i]] # Obtiene la producción de la tabla
                        self.pila.pop()
                        if produccion is not None:
                            if produccion != ['empty']:
                                self.pila.extend(produccion[::-1])

                                # Verifica si la producción es para la declaración de función y hay un identificador de función y al menos un argumento presente
                                if arriba == 'S' and produccion == ['function', 'F', 'N', 'PM']:
                                    # Si no hay identificador de función o argumentos, la cadena no es válida
                                    if 'function' not in self.input_string[i:] or '(' not in self.input_string[i:] or ')' not in self.input_string[i:]:
                                        return False
                                    if 'function' not in self.input_string[i:]:
                                        return False
                else:
                    return False

            # Verificar si la pila está vacía al finalizar el análisis
            if len(self.pila) == 1 and self.pila[0] == "$":
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
