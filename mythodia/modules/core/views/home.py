from django.views.generic import TemplateView

from ...characters.models import Character


class Home(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        characters = Character.objects.all()
        context["characters"] = characters

        return context
