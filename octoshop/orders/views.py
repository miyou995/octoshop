from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from .models import OrderItem, Order
from livraison.models import Wilaya, Commune
from django.views.generic import TemplateView
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart



def order_create(request):
    cart = Cart(request)
    wilayas= Wilaya.objects.all()
    form = OrderCreateForm()

    if request.method == 'POST':
        if len(cart):
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                print('le formulaire est valid')
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'], taille=item['taille'], color=item['color'])
                cart.clear()
                order_created.delay(order.id)
                return render(request, 'created.html', {'order': order})
        else:
            return redirect(reverse('main:index'))
    else:
        form = OrderCreateForm()
    
    return render(request, 'create.html', {'cart':cart, 'form' : form, 'wilayas' : wilayas})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/order-detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    # weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])# ajouter le style plus t ard erreur ???
    weasyprint.HTML(string=html).write_pdf(response)
    return response

def load_communes(request):
    wilaya_id = request.GET.get('wilaya')
    communes = Commune.objects.filter(Wilaya__id=wilaya_id)
    return render(request, 'commune_dropdown_list_options.html', {'communes': communes})


