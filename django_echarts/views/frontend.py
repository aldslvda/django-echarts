# coding=utf8

from django.http import JsonResponse
from django.views.generic.base import View
from pyecharts_javascripthon.api import DefaultJsonEncoder
import json
from .base import EChartsMixin


class EChartsFrontView(EChartsMixin, View):
    def get(self, request, **kwargs):
        echarts_instance = self.get_echarts_instance(**kwargs)
        option_snippet = json.dumps(echarts_instance.options, indent=4, cls=DefaultJsonEncoder)
        return JsonResponse(data=json.loads(option_snippet), safe=False)
