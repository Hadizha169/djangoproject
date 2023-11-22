from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import RunString, GamePostModel, Afisha, Slider


def string_post_view(request):
    if request.method == 'GET':
        string_ = RunString.objects.all()
        game_list = GamePostModel.objects.all()
        afisha = Afisha.objects.all()
        slider = Slider.objects.all()
        return render(request, template_name='main_page/index.html',
                      context={
                          'string_': string_,
                          'game_list': game_list,
                          'afisha': afisha,
                          'slider_list': slider

                      })


def game_detail_view(request, id):
    if request.method == 'GET':
        game_id = get_object_or_404(GamePostModel, id=id)
        return render(request, template_name='main_page/game_detail.html', context={'game_id': game_id})
