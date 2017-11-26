from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse

from certifications.models import Certification, Topic
from courses.models import Course
# Create your views here.
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['certification'] = Certification.objects.filter(num_code=99)[0]
        context['courses'] = Course.objects.all()
        return context

def form_mail(request):
	if request.method == "POST":
		title = request.POST.get('title')
		name = 'name: ' + request.POST.get('name')
		_email = 'email: ' + request.POST.get('email')
		body = '\n'.join([name, _email])
		
		_from = 'noreply@bookkeepingnc3academy.com'
		response = "Thank you, we have received your request."

		# send email to administrator
		email = EmailMessage(title, body, to=['hctura.official@gmail.com'])
		if email.send():
			# send confirmation message to client
			message = '\n'.join([
					response,
					'We received the following:',
					title,
					name,
					_email
				])

			confirmed = send_mail(
			    'Greetings from Bookkeeping NC3 Academy',
			    message,
			    _from,
			    [request.POST.get('email')],
			    fail_silently=False,
			)

			if confirmed:
				return render(request, 'public/alerts/email_sent.html')