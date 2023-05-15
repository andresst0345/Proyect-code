#clases

class Marcador():
    
    def init(self,color:str) -> None:
        self.color = color 
        
    def request_color(self):
        return self.color
        
marcador_1 = Marcador("rojo")
marcador_2 = Marcador()


color_marcador_1 = marcador_1.request_color()
color_marcador_2 = marcador_2.request_color()
print(color_marcador_1)
print(color_marcador_2)