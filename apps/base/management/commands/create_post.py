from django.core.management.base import BaseCommand
from faker import Faker
from apps.user.models import User
from apps.post.models import Post, Like
import random

import requests
from django.core.files.base import ContentFile
from io import BytesIO

fake = Faker()


class Command(BaseCommand):
    help = 'Create a default user with multiple posts and likes'

    def add_arguments(self, parser):
        parser.add_argument('--posts', type=int, default=10, help='Number of default posts to create')

    def create_default_user(self):
        user, created = User.objects.get_or_create(
            username="default_user",
            defaults={
                "email": "default_user@example.com",
                "password": "password123"
            }
        )
        if created:
            user.set_password("password123")  # Сбрасываем пароль, чтобы он был зашифрован
            user.save()
            self.stdout.write(f"Created default user: {user.username}")
        else:
            self.stdout.write(f"Default user already exists: {user.username}")
        return user

    def fetch_image_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return ContentFile(response.content)
        return None

    def create_default_posts(self, user, num_posts):
        posts = []
        for _ in range(num_posts):
            image_url = fake.image_url(width=800, height=600)

            image_content = self.fetch_image_from_url(image_url)
            post = Post(
                author=user,
                title=fake.sentence(),
                description=fake.paragraph(),
            )
            if image_content:
                post.content.save(f"{fake.word()}.jpg", image_content, save=True)

            post.save()
            posts.append(post)
            self.stdout.write(f'Created post: "{post.title}" by {user.username} with image from {image_url}')
        return posts

    def add_likes_to_posts(self, user, posts):
        for post in posts:
            if random.choice([True, False]):
                Like.objects.get_or_create(user=user, post=post)
                self.stdout.write(f'{user.username} liked post "{post.title}" by {post.author.username}')

    def handle(self, *args, **options):
        num_posts = options.get('posts')
        user = self.create_default_user()
        posts = self.create_default_posts(user, num_posts)
        self.add_likes_to_posts(user, posts)
