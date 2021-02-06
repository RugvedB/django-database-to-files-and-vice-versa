import os

PROJECT_NAME = 'DemoProject'

def main():
    from app.models import Category,Book,Author
    import uuid
    from random import randrange
    
    categor_ids = []
    for i in range(100):
        c = Category.objects.create(name = str(i+1) +" - "+uuid.uuid4().hex[:6]+"-categoryname")
        categor_ids.append(c.id)
    
    author_ids = []
    for i in range(5):
        a = Author.objects.create(name = str(i+1) +" - "+uuid.uuid4().hex[:6]+"-authorname")
        author_ids.append(a.id)
    
    for i in range(30):
        #  Generate random number between 0 to 4
        author_id = author_ids[randrange(5)]

        book = Book.objects.create(
            name = str(i+1) +" - "+uuid.uuid4().hex[:6]+"-bookname",
            author = Author.objects.get(id = author_id),
        )

        #  Generate random number between 0 to 5 - this will be equal to how many category items should we pick
        num_of_category = randrange(6)

        for i in range(num_of_category):
            book.categories.add(Category.objects.get(id = categor_ids[randrange(100)]))
        
        book.save()
    

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % PROJECT_NAME)
    import django
    django.setup()
    main()