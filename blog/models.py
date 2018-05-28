from django.db import models


class Articles(models):
    def title(self):
        title = "010101"
        return title

    def description(self):
        descriptions = "010101"

        return descriptions

    def body(self):
        body = "10101"
        return body

    def date(self):
        date = "101010"
        return date

    def category(self, category):
        category = "010101"
        return category
    # Create your models here.
