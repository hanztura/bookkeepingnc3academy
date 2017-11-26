from django.shortcuts import render, get_object_or_404
from django.forms import model_to_dict

from .models import Certification, Topic
from .forms import TopicForm

# Create your views here.
class TopicViews():
	"""docstring for TopicViews"""
	def detail(request, id):
		model = get_object_or_404(Topic, pk=id)
		
		form = TopicForm(instance=model, initial=model_to_dict(model))

		context = {
			'model': model,
			'form': form
		}

		return render(request, 'certifications/topics/detail.html', context)

	def update(request, id):
		if request.method == 'POST':
			model = get_object_or_404(Topic, pk=id)
			form = TopicForm(request.POST, instance=model)

			context = {
			'form' : form,
			'model': model,
			}

			fail = render(request, 'certifications/topics/detail.html', context)

			if form.has_changed():
				if form.is_valid():
					form.save()
				else:
					return fail

		return HttpResponseRedirect(reverse('public:index'))