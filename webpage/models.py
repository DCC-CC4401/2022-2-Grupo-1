from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return (f"User("
                f"username={self.username}, "
                f"name={self.first_name} {self.last_name}, "
                f"email={self.email}"
                f")")
