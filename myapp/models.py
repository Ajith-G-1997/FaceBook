from django.db import models

# User model
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords
    profile_picture = models.ImageField(upload_to='static/profile_pic')

    def __str__(self):
        return self.username


# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


# Post model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=1000, blank=True)
    image_or_video = models.FileField(upload_to='static/posts')
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username} - {self.publication_date}"




