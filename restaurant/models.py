from django.db import models


class Feedback(models.Mode):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Feedback {self.id} - {self.comment[ :20]}"