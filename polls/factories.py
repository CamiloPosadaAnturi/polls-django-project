import factory
from factory.django import DjangoModelFactory
from django.utils import timezone
from polls.models import Question, Choice

class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    question_text = factory.Faker("sentence")
    pub_date = factory.LazyFunction(timezone.now)

    @factory.post_generation
    def choices(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for choice_text in extracted:
                ChoiceFactory(question=self, choice_text=choice_text)

class ChoiceFactory(DjangoModelFactory):
    class Meta:
        model = Choice

    question = factory.SubFactory("polls.factories.QuestionFactory")
    choice_text = factory.Faker("word")
    votes = 0
