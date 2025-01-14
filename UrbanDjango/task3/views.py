from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def main_page(requset):
    return render(requset, 'third_task/platform.html')


def store_games(requset):
    games = {
        'game1': 'Atomic Heart',
        'game2': 'Cyberpunk 2077',
        'game3': 'PayDay 2'
    }
    return render(requset, 'third_task/games.html', {'games': games})


def cart_page(request):
    cart_items = {
        'Atomic Heart': {'price': 1500, 'quantity': 1},
        'Cyberpunk 2077': {'price': 2000, 'quantity': 1},
    }
    total = sum(item['price'] * item['quantity'] for item in cart_items.values())
    discount = 0.1 if total > 200 else 0
    final_total = total - (total * discount)
    discount_percent = discount * 100
    return render(request, 'third_task/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'final_total': final_total,
        'discount_percent': discount_percent
    })