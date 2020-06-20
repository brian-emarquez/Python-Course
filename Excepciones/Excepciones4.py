#Excepciones 4

def evalua(edad):
    if edad<0:
        raise TypeError("No se permite edades negativas")
    if edad<20:
        return "Eres muy Joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return " Eres Maduro"
    elif edad < 100:
        return " Cuidate..."
    


print(evalua(-18))
    
    
