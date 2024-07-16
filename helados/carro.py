class Carro:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            self.carro = self.session['carro'] = {}
        else:
            self.carro = carro

    def agregar(self, producto, tipo_producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen_url':producto.foto.url,
                'tipo_producto': tipo_producto
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] += 1
                    break
        
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def eliminar(self, producto_id):
        producto_id = str(producto_id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['cantidad'] -= 1
                if value['cantidad'] == 0:
                    self.eliminar(producto.id)
                break
        self.guardar_carro()
    
    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True

