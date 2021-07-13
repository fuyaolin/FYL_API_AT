# -*- coding: utf-8 -*-

import pytest
import requests
import os
from public.read_yaml import YamlUtil


class TestApi():
    @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'\\test_api.yaml').read_yaml())
    def test_01(self, args):
        url = args['request']['url']
        params = args['request']['params']
        headers = args['request']['headers']
        response = requests.post(url, params=params, headers=headers)
        print(response)
        print(response.text)

if __name__ == '__main__':
    pytest.main(['-vs'])
