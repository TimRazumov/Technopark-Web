import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','server_engine.settings')
import django
django.setup()
import random
from django.contrib.auth.models import User
from bomonka_forum.models import Profile, Question, Answer, Tag
from faker.providers.person.en import Provider
from faker import Faker
fake = Faker()

'''TODO добавить лайки и дизлайки пользователей (аналогично тэгам в generate_questions)'''

def generate_users(user_size):
    usernames = list(set(Provider.first_names))
    random.seed(4321)
    random.shuffle(usernames)
    for i in range(user_size):
        email = fake.email()
        user = User.objects.create(username=usernames[i], email=email, password="timatima123")
        Profile.objects.create(user=user, email=email)
        
def generate_tags(tags_size):
    tags = list(Tag.objects.all())
    for i in range(tags_size):
        title = fake.text()[0:10].replace(" ", "")
        while title in tags:
            title = fake.text()[0:10].replace(" ", "")
        tags.append(title)
        Tag.objects.create(title=title)

def generate_questions(questions_size):
    for i in range(questions_size):
        title = fake.text()[0:20]
        body = fake.text()[0:300]
        num_like = random.randint(0, 1000)
        num_dislike = random.randint(0, 1000)
        max = Profile.objects.all().order_by("-pk")[0].pk
        min = Profile.objects.all().order_by("pk")[0].pk
        author = Profile.objects.get(pk=random.randint(min, max))
        max = Tag.objects.all().order_by("-pk")[0].pk
        min = Tag.objects.all().order_by("pk")[0].pk
        tags = []
        for j in range(3):
            tmp = Tag.objects.get(pk=random.randint(min, max))
            while tmp in tags:
                tmp = Tag.objects.get(pk=random.randint(min, max))
            tags.append(tmp)
        q = Question.objects.create(title=title, body=body, author=author, num_like=num_like, num_dislike=num_dislike, slug=str(i))
        q.tags.set(tags)

def generate_answers(answers_size):
    for i in range(answers_size):
        body = fake.text()[0:300]
        num_like = random.randint(0, 1000)
        num_dislike = random.randint(0, 1000)
        max = Profile.objects.all().order_by("-pk")[0].pk
        min = Profile.objects.all().order_by("pk")[0].pk
        author = Profile.objects.get(pk=random.randint(min, max))
        max = Question.objects.all().order_by("-pk")[0].pk
        min = Question.objects.all().order_by("pk")[0].pk
        questions = Question.objects.get(pk=random.randint(min, max))
        correctness = random.choice((False, True))
        Answer.objects.create(body=body, author=author, correctness=correctness, num_like=num_like, num_dislike=num_dislike, questions=questions)


from django.core.management.base import BaseCommand, CommandError
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--users', type=int)
        parser.add_argument('--questions', type=int)
        parser.add_argument('--answers', type=int)
        parser.add_argument('--tags', type=int)

    def handle(self, *args, **options):
        if options['users']:
            print("Generating users", options['users'])
            generate_users(options['users'])
        if options['questions']:
            print("Generating questions", options['questions'])
            generate_questions(options['questions'])
        if options['answers']:
            print("Generating answers", options['answers'])
            generate_answers(options['answers'])
        if options['tags']:
            print("Generating tags", options['tags'])
            generate_tags(options['tags'])
