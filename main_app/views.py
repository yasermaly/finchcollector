from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Define the home view


def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


# Add the Cat class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description):
    self.name = name
    self.breed = breed
    self.description = description


finches = [
    Finch('Lola', 'blue finch', 'The blue finch is a small tanager originating in South America, specifically in Brazil and Bolivia. The males have a bright cobalt blue plumage, although after the molt the feathers have a rufous-brown hue with broad edges. Females, on the other hand, have a rufous brown upper plumage, with buffy white underparts marked with dusky streaks.'),
    Finch('zippy', 'safron finch', 'Saffron finch is a small tanager originating in South America. The males with a vibrant yellow body and an orange crown can be distinguished from the females that usually have a somewhat duller coloration. However, females in some subspecies have an olive-brown body consisting of heavy dark markings.'),
    Finch('Raven', 'gouldian finch', 'The Gouldian finch, also known as rainbow finch, Lady Gouldian finch, Goulds finch, Scarlet-headed finch is an attractive and colorful bird. These birds, with a blackish beak have red, yellow or black colored heads because of their color mutations. Female finches have a less bright hue than their male counterparts and are characterized with a light mauve chest. Being classified as endangered in the wild, by the IUCN in 1992, most of these birds are bred in captivity mainly in Australia.'),
    Finch('tweets', 'strawberry finch', 'The strawberry finch is an attractive sparrow-sized bird, originating from Asia. Characterized with colorful plumage, a vivid red bill, and a rounded black tail, it is a popular choice in aviculture. With rapid wing beats, they prefer to fly in small flocks, descending into clumping grasses, where they are not spotted easily. Unlike the females, the males sport a scarlet breeding plumage (during April-November).'),
]


def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})
