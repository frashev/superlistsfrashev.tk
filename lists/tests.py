from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        
        # Save
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        # Retrieve
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        #request = HttpRequest()
        #print("request is {}".format(request))
        #response = home_page(request)
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        # self.assertIn('A new list item', response.content.decode())
        #print("response -- {}".format(response.content.decode()))
        self.assertTemplateUsed(response, 'home.html')


