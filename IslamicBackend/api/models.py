from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True)  # Matches @Id in Spring Boot
    question_text = models.CharField(max_length=255, null=False)  # Matches questionText

    # Remove the direct link to a right_option
    def __str__(self):
        return self.question_text


class Option(models.Model):
    id = models.AutoField(primary_key=True)  # Matches @Id in Spring Boot
    option_text = models.CharField(max_length=255, null=False)  # Matches optionText
    question = models.ForeignKey(
        Question,
        related_name='options',  # Allows Question to access its list of Options
        on_delete=models.CASCADE  # Delete options when the question is deleted
    )
    is_correct = models.BooleanField(default=False)  # Flag to indicate if this is the correct option

    def __str__(self):
        return self.option_text
