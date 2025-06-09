from django.core.management.base import BaseCommand
from store.models import Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with diverse fake products including images'

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = [
            'Electronics', 'Books', 'Clothing',
            'Home', 'Toys', 'Beauty', 'Sports',
            'Grocery', 'Automotive', 'Footwear'
        ]

        image_urls = [
            "https://via.placeholder.com/150",
            "https://picsum.photos/200",
            "https://placehold.co/200x200",
            "https://dummyimage.com/200x200/000/fff.png&text=Product",
            "https://source.unsplash.com/random/200x200?product"
        ]

        Product.objects.all().delete()  # Optional: clear existing products

        for _ in range(100):
            category = random.choice(categories)
            name = f"{category} {fake.word().capitalize()}"
            description = fake.sentence(nb_words=12)
            price = round(random.uniform(100, 5000), 2)
            image = random.choice(image_urls)

            Product.objects.create(
                name=name,
                description=description,
                price=price,
                category=category,
                image=image  # ✅ Include image
            )

        self.stdout.write(self.style.SUCCESS('✅ 100 diverse products with images created.'))
