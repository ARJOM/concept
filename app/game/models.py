from django.db import models
from app.core.models import CreateUpdateModel, UUIDUser


# Concept
# - - - - - - - - - - - - - - - - - - - -
class Concept(CreateUpdateModel):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'concept'
        verbose_name_plural = 'concepts'


# Item
# - - - - - - - - - - - - - - - - - - - -
class Item(CreateUpdateModel):

    name = models.CharField(max_length=30)
    concepts = models.ManyToManyField(Concept, related_name='concepts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'


# Game
# - - - - - - - - - - - - - - - - - - - -
class Game(CreateUpdateModel):

    player = models.ForeignKey(UUIDUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='items')
    concluded = models.BooleanField(default=False)
    correct = models.IntegerField(default=0)
    total = models.IntegerField(default=10)

    def __str__(self):
        return self.player.username

    class Meta:
        verbose_name = 'game'
        verbose_name_plural = 'games'
