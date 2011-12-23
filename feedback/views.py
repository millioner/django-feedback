from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.contrib import messages

from feedback.forms import FeedbackForm

def leave_feedback(request, template_name='feedback/feedback_form.html'):
    form = FeedbackForm(request.POST or None, initial={
        'next': getattr(settings, 'FEEDBACK_REDIRECT_URL', request.get_full_path())
    })
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.user = request.user
        feedback.save()
        messages.success(request, _("Your feedback has been saved successfully."))
        return HttpResponseRedirect(form.cleaned_data.get('next', request.META.get('HTTP_REFERER', '/')))
    return render_to_response(template_name, {'feedback_form': form}, context_instance=RequestContext(request))

