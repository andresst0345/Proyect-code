#clases

class Marcador():
    
    def __init__(self,color:str) -> None:
        self.color = color 
        
    def request_color(self):
        return self.color
    
    def __str__(self) -> str:
        pass
        
marcador_1 = Marcador("rojo")
marcador_2 = Marcador()


color_marcador_1 = marcador_1.request_color()
color_marcador_2 = marcador_2.request_color()
print(color_marcador_1)
print(color_marcador_2)