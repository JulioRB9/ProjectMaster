class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        else:
            self.carro = carro

    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carro:
            self.carro[producto_id] = {
                'nombre': producto.nombre, 
                'precio': str(producto.precio), 
                'cantidad': 0,
                'imagen': producto.imagen.url 
                }
        self.carro[producto_id]['cantidad'] += 1
        self.guardar()