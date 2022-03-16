from django.test import TestCase

from . import analyzer


class ReadabilityTestCase(TestCase):

    text_one = 'This sentence, taken as a reading passage unto itself, is being used to prove a point.'
    score_one = 69

    text_two = 'The Australian platypus is seemingly a hybrid of a mammal and reptilian creature.'
    score_two = 37.5

    text_three = 'The cat sat on the mat.'
    score_three = 116

    def test_one(self):
        calculated_score = round(analyzer.reading_score(self.text_one), 0)
        self.assertEquals(self.score_one, calculated_score)

    def test_two(self):
        calculated_score = round(analyzer.reading_score(self.text_two), 1)
        self.assertEquals(self.score_two, calculated_score)

    def test_three(self):
        calculated_score = round(analyzer.reading_score(self.text_three), 0)
        self.assertEquals(self.score_three, calculated_score)

    def test_four(self):

        text = self.text_one + ' '
        text += self.text_two + ' '
        text += self.text_three

        print(analyzer.analyze(text))
