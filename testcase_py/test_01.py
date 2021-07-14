# -*- coding: utf-8 -*-

import pytest
import requests
import os
from public.yaml.read_yaml import ReadYaml


class TestApi():
    @pytest.mark.parametrize('args', ReadYaml(os.getcwd()+'\\test01.yaml').read_yaml())
    def test_01(self, args):
        url = args['request']['url']
        params = args['request']['params']
        headers = args['request']['headers']
        response = requests.post(url, params=params, headers=headers)
        print(response)
        print(response.text)

# if __name__ == '__main__':
    # pytest.main(['-vs'])
