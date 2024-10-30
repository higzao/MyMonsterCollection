from django.shortcuts import render


def index (request):
    data = {
    1: {'name': 'Monster Energy Dragon Ice Tea Lemon',
        'line': 'Dragon Ice Tea',
        'country': 'Brazil',
        'continent' : 'South America',
        'size': '473ml',
        'sku': '0819B',
        'manufacturer': 'ball',
        'color': {
            'main': 'green',
            'details': 'green',
            'lid': 'green',
            'top': 'silver'},
        'logo_lid': True,
        'sugar_warning': False,
        'condition': 97,
        'top_intact': False,
        'promotion': {
            'is_promotion': False,
            'name': '',
            'details': ''},
        'bottle': False,
        'tasted': True,
        'notes': {
            'top': 'CHÁ COM LIMÃO / LEMON / NÃO GASEFICADO',
            'bottom': 'COMPOSTO LÍQUIDO PRONTO PARA O CONSUMO À BASE DE TAURINA E CAFEÍNA COM SUCO DE FRUTAS E CHÁ. CONTÉM AROMATIZANTE.'},
        'images': {
            'front': 'br-dragonicetea-front.png',
            'back': 'xxxx',
            'back_2': 'xxxx',
            'top': 'xxx'},
        'gift': {
            'is_gift': True,
            'friend': 'Ludwig'}
     },
    2: {'name': 'Monster Energy Original (COD)',
        'line': 'Energy',
        'country': 'Poland',
        'continent' : 'Europe',
        'size': '500ml',
        'sku': '0623',
        'manufacturer': 'CP',
        'color': {
            'main': 'black',
            'details': 'green',
            'lid': 'black',
            'top': 'silver'},
        'logo_lid': False,
        'sugar_warning': False,
        'condition': 100,
        'top_intact': True,
        'promotion': {
            'is_promotion': True,
            'name': 'Call of Duty',
            'details': 'não sei qual foi kkk'},
        'bottle': False,
        'tasted': True,
        'notes': {
            'top': 'L-KARNITYNA + TAURYNA + ZENSZEN + WITAMINY Z GRUPY B',
            'bottom': ''},
        'images': {
            'front': 'pl-og-cod-front.png',
            'back': 'xxxx',
            'back_2': 'xxxx',
            'top': 'xxx'},
        'gift': {
            'is_gift': False,
            'friend': 'Ludwig'}

    }
}
    return render(request, 'showcase/index.html', {'cards':data})

def image (request):
    return render(request, 'showcase/image.html')