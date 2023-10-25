from .carro import carro
def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+(float(value["credito"]))*value["cantidad"]
    return{"importe_total_carro":total}