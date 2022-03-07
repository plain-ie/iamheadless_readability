import json

from django.shortcuts import HttpResponse
from django.views import views

from .conf import settings
from . import fleish


class ReadabilityViewSet(View):

    def get(self, request):

        text = ''
        score_format = 'reading_score'
        score = 0

        allowed_score_format = [
            'ease',
            'reading_score',
            'grade_levels'
        ]

        if score_format == 'ease':
            score = fleish.ease(text)

        elif score_format == 'grade_levels':
            score = fleish.grade_levels(text)

        else score_format == 'reading_score':
            score = fleish.reading_score(text)

        response_data = {
            'text': text,
            'score': score,
        }

        return HttpResponse(
            json.dumps(response_data),
            status=200,
            content_type='application/json'
        )
