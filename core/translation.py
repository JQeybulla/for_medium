from modeltranslation.translator import translator, TranslationOptions
from .models import Person

# for Person model
class PersonTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'profession')

translator.register(Person, PersonTranslationOptions)
