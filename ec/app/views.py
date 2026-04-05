from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
import razorpay
from .models import Product,Cart,Payment,OrderPlaced,Wishlist
from .forms import CustomerProfileForm,CustomerRegistrationForm
from django.contrib import messages
from .models import Customer
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator






# Create your views here.
@login_required
def home(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    return render(request,'app/home.html',locals())
def about(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    return render(request,'app/about.html',locals())


def Agriculturepractices(request):
    return render(request,'app/Agriculturepractices.html')
def agriArticle(request):
    return render(request,'app/agriArticle.html')
def evolution(request):
    return render(request,'app/evolution.html')
def kannada(request):
    return render(request,'app/kannada.html')
def schemes(request):
    return render(request,'app/schemes.html')
def livestock(request):
    return render(request,'app/livestock.html')
def equipment(request):
    return render(request,'app/equipment.html')
def soil(request):
    return render(request,'app/soil.html')
def Science(request):
    return render(request,'app/Science.html')
def river(request):
    return render(request,'app/river.html')


class CategoryView(View):
    def get(self,request,val):
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
              totalitem=len(Cart.objects.filter(user=request.user))
              wishitem=len(Wishlist.objects.filter(user=request.user))
        product =Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values()
        return render(request,'app/category.html',locals())
 
@method_decorator(login_required,name='dispatch')
class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
          totalitem=len(Cart.objects.filter(user=request.user))
          wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/category.html", locals())

   
@method_decorator(login_required,name='dispatch')
class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user)) if request.user.is_authenticated else None
        totalitem = 0
        wishitem=0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/productdetail.html', locals())


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
           totalitem=len(Cart.objects.filter(user=request.user))
           wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/customerregistration.html', locals())
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Registred Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'app/customerregistration.html', locals())
  
class ProfileView(View):
        def get(self, request):
            form=CustomerProfileForm()
            totalitem=0
            wishitem=0
            if request.user.is_authenticated:
               totalitem=len(Cart.objects.filter(user=request.user))
               wishitem=len(Wishlist.objects.filter(user=request.user))
            return render(request, 'app/profile.html', locals())
        def post(self,request):
            form=CustomerProfileForm(request.POST)
            if form.is_valid():
                user = request.user
                name = form.cleaned_data
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                mobile = form.cleaned_data['mobile']
                state = form.cleaned_data['state']
                pincode = form.cleaned_data['pincode']
                reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state ,pincode=pincode )
                reg.save()
                messages.success(request,"Congragulations! Profile Saved Successfully")
            else:
                messages.warning(request,"Invalid input data")
            
            return render(request, 'app/profile.html', locals())
        
       
def address(request):
        add=Customer.objects.filter(user=request.user)
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/address.html', locals())


class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        totalitem=0
        if request.user.is_authenticated:
          totalitem=len(Cart.objects.filter(user=request.user))
          wishitem=len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/updateAddress.html', locals())
    def post(self,request,pk):
         form=CustomerProfileForm(request.POST)
         if form.is_valid():
           add = Customer.objects.get(pk=pk)
           add.name = form.cleaned_data['name']
           add.locality = form.cleaned_data['locality']
           add.city = form.cleaned_data['city']
           add.mobile = form.cleaned_data['mobile']
           add.state = form.cleaned_data['state']
           add.pincode = form.cleaned_data['pincode']
           add.save()
    
           messages.success(request, "Congratulations! Profile Updated Successfully")
         else:
            messages.warning(request, "Invalid Input Data")

         return redirect("address")
    
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')
@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount=0
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    for p in cart:
        value=p.quantity*p.product.discounted_price
        amount=amount + value
    totalamount=amount + 40
    return render(request, 'app/addtocart.html', locals())

@login_required
def show_wishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request, "app/wishlist.html", locals())



@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem=0
        wishitem=0
        if request.user.is_authenticated:
            totalitem=len(Cart.objects.filter(user=request.user))
            wishitem=len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value=p.quantity*p.product.discounted_price
            famount=famount+value
        totalamount=famount+40
        razoramount= int(totalamount*100)
        client =razorpay.Client(auth=(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))
        data={"amount":razoramount,"currency":"INR","receipt":"order_rcptid_12"}
        payment_response=client.order.create(data=data)
        print(payment_response)
        #{'amount': 508000, 'amount_due': 508000, 'amount_paid': 0, 'attempts': 0, 'created_at': 1741627358, 'currency': 'INR', 'entity': 'order', 'id': 'order_Q5AVXkcYlvSTrG', 'notes': [], 'offer_id': None, 'receipt': 'order_rcptid_12', 'status': 'created'}
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
                payment = Payment(
                    user=user,
                    amount=totalamount,
                    razorpay_order_id=order_id,
                    razorpay_payment_status=order_status
                  )
                payment.save()

        return render(request,'app/checkout.html',locals())
    

def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')

    # 🚀 Ensure cust_id is valid
    try:
        customer = Customer.objects.get(id=cust_id)
        user = customer.user  # Fetch the authenticated user from the customer
    except Customer.DoesNotExist:
        return JsonResponse({"error": "Invalid customer ID"}, status=400)

    # ✅ Update payment status
    payment = get_object_or_404(Payment, razorpay_order_id=order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()

    # ✅ Save order details
    cart = Cart.objects.filter(user=user)  # Now user is fetched from Customer
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, payment=payment).save()
        c.delete()

    return redirect("orders")

@login_required
def orders(request):
    totalitem=0
    wishitem=0
    if request.user.is_authenticated:
        totalitem=len(Cart.objects.filter(user=request.user))
        wishitem=len(Wishlist.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    
    return render(request, 'app/orders.html', locals())



@login_required
def plus_cart(request):
    if request.method =="GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.filter(product_id=prod_id, user=request.user).first()
    if c:
         c.quantity += 1
         c.save()
         user=request.user
         cart=Cart.objects.filter(user=user)
         amount=0
         for p in cart:
            value=p.quantity*p.product.discounted_price
            amount=amount+value
         totalamount=amount+40

        #print(prod_id)
         data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }
         return JsonResponse(data)
    
@login_required 
def minus_cart(request):
    if request.method =="GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.filter(product_id=prod_id, user=request.user).first()
    if c:
         c.quantity -= 1
         c.save()
         user=request.user
         cart=Cart.objects.filter(user=user)
         amount=0
         for p in cart:
            value=p.quantity*p.product.discounted_price
            amount=amount+value
         totalamount=amount+40

        #print(prod_id)
         data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount

        }
         return JsonResponse(data)
    

def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        print(f"Removing product ID: {prod_id}")

        try:
            cart_items = Cart.objects.filter(product_id=prod_id, user=request.user)
            
            if cart_items.exists():
                cart_items.delete()
                print(f"All occurrences of product {prod_id} removed from cart")
            else:
                print(f"Product {prod_id} not found in cart")

        except Exception as e:
            print(f"Error: {e}")

        # ✅ Recalculate cart totals
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        amount = sum(item.quantity * item.product.discounted_price for item in cart_items)
        totalamount = amount + 40 if amount > 0 else 0  

        return JsonResponse({"amount": amount, "totalamount": totalamount})



@login_required
def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
       
        Wishlist.objects.get_or_create(user=request.user, product=product)
        data = {'message': 'Wishlist Added Successfully'}
        return JsonResponse(data)
 

@login_required
def minus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        product = get_object_or_404(Product, id=prod_id)
       
        # Check if the product exists in the user's wishlist
        wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
        
        if wishlist_item.exists():
            wishlist_item.delete()
            data = {'message': 'Wishlist Removed Successfully'}
        else:
            data = {'message': 'Item not in wishlist'}  

        return JsonResponse(data)
    

def search(request):
    query = request.GET['search']
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Product.objects.filter(Q(title__icontains=query))
    return render(request, "app/search.html", locals())



from django.conf import settings
from django.http import JsonResponse
import google.generativeai as genai

genai.configure(api_key=settings.GOOGLE_GENAI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        try:
            response = chat.send_message(user_input)
            return JsonResponse({'response': response.text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'app/chat.html')
