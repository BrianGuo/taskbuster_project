# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
# REMOVING INTERNATIONALIZATION
# from django.utils.translation import activate


class TestHomePage(TestCase):

    def test_uses_index_template(self):
        # REMOVING INTERNATIONALIZATION
        # activate('en')
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'taskbuster/index.html')

    def test_uses_base_template(self):
        # REMOVING INTERNATIONALIZATION
        # activate('en')
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'base.html')
