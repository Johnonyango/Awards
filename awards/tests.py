from django.test import TestCase
from .models import Profile, Project, Rating


class ProfileTestClass(TestCase):
  """  
  Test class that tests profile
  """
 def setUp(self):
    self.prof =Profile(profpic='test.jpg', bio='test bio', contact='hello@hello.com',user=1)

  def test_instance(self):
      self.assertTrue(isinstance(self.prof, Profile))

  def test_save_method(self):
      """
      Function to test that profile is being saved
      """
      self.prof.save_profile()
      profiles = Profile.objects.all()
      self.assertTrue(len(profiles) > 0)



    