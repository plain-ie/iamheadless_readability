import json

from django.core.exceptions import SuspiciousOperation
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from iamheadless_publisher_admin import decorators

from . import analyze


class ReadabilityViewSet(View):

    @method_decorator(decorators.login_required(), name='dispatch')
    def get(self, request):

        request_body = json.loads(request.body.decode('utf-8'))

        text = request_body.get('text', None)

        if text is None:
            raise SuspiciousOperation('Payload is missing "text"')

        data = analyzer.analyze(text)

        return HttpResponse(
            json.dumps(data),
            status=200,
            content_type='application/json'
        )
