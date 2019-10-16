from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import View
from django.forms.models import model_to_dict
from .models import Runner, Lap

class NextlapView(View):
  template_name = 'competition/nextlap.html'
  def get(self, request, *args, **kwargs):
    return render(request, self.template_name)

  def post(self, request, *args, **kwargs):
    nextlap = Lap.objects.order_by('registration_time').first()

    if nextlap == None:
      return JsonResponse({'success':'false'})
    else:
      obj = model_to_dict(nextlap)
      obj.update({'success': True})
      return JsonResponse(obj)
    

def inside(request):
  template = loader.get_template('competition/inside.html')
  context = {}
  return HttpResponse(template.render(context, request))

def signup(request):
  try:
    selected_runner = Runner.objects.get(identification=request.POST['user_identification'])
  except KeyError:
    return render(request, 'competition/signup.html', {
      'error_message': "Please enter a valid identification.",
    })
  except Runner.MultipleObjectsReturned:
    return render(request, 'competition/signup.html', {
      'error_message': "Multiple runners found with this identification. Try using you university number, or use your full name.",
    })
  except Runner.DoesNotExist:
    return render(request, 'competition/signup.html', {
      'error_message': "No runner found with this identification. Try using you university number, or use your full name.",
    })
  else:
    lap = Lap(runner=selected_runner)
    lap.save()
    return HttpResponseRedirect(reverse('competition:signup'))