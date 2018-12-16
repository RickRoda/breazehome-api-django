from django.test import TestCase
from real_estate.views import ListsViewSet
from real_estate.models import Lists
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
import json


class ListMethodTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='John Doe', 
            email='john@emial.com', 
            password='password'
        )        

    def createList(self, data):
        return self.factory.post('/users/%s/lists' % self.user.id, json.dumps(data), content_type='application/json')

    def test_creation_of_list(self):
        """
        new list created should return successfully
        """

        view = ListsViewSet.as_view({'post': 'create'})
        data = {'title': 'Test List', 'user': self.user.id}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content)['user'], self.user.id)

    def test_deletion_of_list(self):
        """
        new list created should be deleted successfully
        """

        # Create new list
        view = ListsViewSet.as_view({'post': 'create'})
        data = {'title': 'Test List', 'user': self.user.id}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()
        list_id = json.loads(response.content)['id']
        
        # Delete newly created list
        view = ListsViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete("/users/{0}/lists/{1}".format(self.user.id, list_id), content_type='application/json')
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(response.status_code, 204)

    def test_deletion_of_nonexistant_list(self):
        """
        deletion of nonexistant list should be rejected    
        """
        
        # Delete nonexistant list, in this case with ID: 45
        view = ListsViewSet.as_view({'delete': 'destroy'})
        request = self.factory.delete("/users/{0}/lists/{1}".format(self.user.id, 45), content_type='application/json')
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(response.status_code, 404)

    def test_update_of_list(self):
        """
        existing list should be updated
        """

        # Create list to be updated
        view = ListsViewSet.as_view({'post': 'create'})
        data = {'title': 'Test List', 'user': self.user.id}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()
        list_id = json.loads(response.content)['id']

        # Update list
        view = ListsViewSet.as_view({'put': 'update'})
        data = {'title': 'Updated', 'user': self.user.id}
        request = self.factory.put("/users/{0}/lists/{1}".format(self.user.id, list_id), json.dumps(data), content_type='application/json')
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['title'], 'Updated')

    def test_get_all_user_lists(self):
        """
        All lists beloning to user should exist and be retrieved correctly
        """

        view = ListsViewSet.as_view({'post': 'create'})

        # Create lists to retrieved
        for x in range(5):
            request = self.createList({'title': 'List-%s' % x, 'user': self.user.id})
            view(request, user_pk=self.user.id, pk=self.user.id)
        
        view = ListsViewSet.as_view({'get': 'list'})
        request = self.factory.get("/users/{0}/lists".format(self.user.id))
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(len(json.loads(response.content)), 5)

    def test_get_all_lists_of_nonexistant_user(self):
        """
        All lists beloning to user should exist and be retrieved correctly
        """

        view = ListsViewSet.as_view({'get': 'list'})
        request = self.factory.get("/users/{0}/lists".format(45))
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        # Note: Status code should be 200 OK however, the returned array 
        # should be empty. This is a security feature to prevent the
        # exhaustion of userID requests
        self.assertEqual(len(json.loads(response.content)), 0)        

    def test_create_list_for_nonexistant_user(self):
        """
        Lists which are created for a nonexistant user should be rejected
        """

        view = ListsViewSet.as_view({'post': 'create'})
        data = {'title': 'Test List', 'user': 45}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(response.status_code, 400)

    def test_create_list_without_title(self):
        """
        Lists which are created without title should be rejected
        """

        view = ListsViewSet.as_view({'post': 'create'})
        data = {'user': self.user.id}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(response.status_code, 400)

    def test_create_list_without_userID(self):
        """
        Lists which are created without userID should be rejected
        """

        view = ListsViewSet.as_view({'post': 'create'})
        data = {'title': 'My list'}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()

        self.assertEqual(response.status_code, 400)

    def test_update_list_with_nonexistant_user(self):
        """
        updated list should be rejected due to nonexistant userID being added
        """

        # Create list to be updated
        view = ListsViewSet.as_view({'post': 'create'})
        data = {'title': 'Test List', 'user': self.user.id}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()
        list_id = json.loads(response.content)['id']

        # Update list
        view = ListsViewSet.as_view({'put': 'update'})
        data = {'title': 'Updated', 'user': 45}
        request = self.factory.put("/users/{0}/lists/{1}".format(self.user.id, list_id), json.dumps(data), content_type='application/json')
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'user': ['Invalid pk "45" - object does not exist.']})

    def test_create_list_with_extra_keys_(self):
        """
        Any list created that does not strictly match the {title, user} model should still be accepted 
        however, the API should drop the extra key before saving to database
        """

        view = ListsViewSet.as_view({'post': 'create'})
        data = {'title': 'Test List', 'user': self.user.id, 'extra_key': 'should be rejected'}
        request = self.createList(data)
        response = view(request, user_pk=self.user.id, pk=self.user.id)
        response.render()   

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content)['user'], self.user.id)