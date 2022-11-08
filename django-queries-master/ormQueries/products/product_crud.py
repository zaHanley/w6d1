from .models import Product 
from django.db.models import Q, Avg, Max, F
from django.db.models.functions import Length


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model):
        return Product.objects.get(model=model)

    @classmethod
    def last_record(cls):
        return Product.objects.latest('id')
    
    @classmethod 
    def by_rating(cls, rating):
        return Product.objects.filter(rating=rating)

    @classmethod
    def by_rating_range(cls, low, high):
        return Product.objects.filter(rating__range=(low,high))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating=rating, color=color)
    
    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(Q(rating=rating) | Q(color=color))
    
    @classmethod
    def no_color_count(cls):
        return len(Product.objects.filter(color=None))
    
    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        return Product.objects.filter(Q(price_cents__lt=price) | Q(rating__gt=rating))
        
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents')
    
    @classmethod
    def products_by_manufacturer_with_name_like(cls, name):
        return Product.objects.filter(manufacturer__contains=name)

    # @classmethod
    # def manufacturer_names_for_query(cls, name):
    #     return Product.objects.filter(manufacturer=name)

    @classmethod
    def not_in_a_category(cls, cat):
        return Product.objects.exclude(category=cat)

    @classmethod
    def limited_not_in_a_category(cls, cat, num):
        return Product.objects.exclude(category=cat)[:num]
    
    @classmethod
    def category_manufacturers(cls, cat):
        return Product.objects.filter(category=cat).values_list('manufacturer', flat=True)

    @classmethod
    def average_category_rating(cls, cat):
        return Product.objects.filter(category=cat).values('rating').aggregate(rating__avg = Avg('rating'))
    
    @classmethod
    def greatest_price(cls):
        return Product.objects.values('price_cents').aggregate(price_cents__max = Max('price_cents'))
    
    @classmethod
    def longest_model_name(cls):
        modelname = Product.objects.values('id').values('model').aggregate(Max('model'))
        modelname = modelname['model__max']
        length = len(modelname)
        return length

    @classmethod
    def ordered_by_model_length():
        return Product.objects.values('model')