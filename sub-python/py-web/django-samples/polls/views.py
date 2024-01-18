from django import shortcuts, urls
from django.views import generic

from . import models


# 投票首页
# def index(req):
#   qlist = models.Question.objects.order_by('-pub_date')[:5]
#   # text_list = {it.id: it.question_text for it in qlist}
#   # return HttpResponse("Hello, this is the index page of polls.")
#   # return HttpResponse(json.dumps(text_list, indent=2, ensure_ascii=False))
#   # tpl = template.loader.get_template('polls/index.html')
#   context = {"qlist": qlist}
#   return shortcuts.render(req, 'polls/index.html', context)
#   pass
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'qlist'

    def get_queryset(self):
        return models.Question.objects.order_by('-pub_date')[:5]
    pass


# 问题详情页
# def details(req, question_id):
#     q = shortcuts.get_object_or_404(models.Question, pk=question_id)
#     # return HttpResponse(f'这里是问题 {question_id} 详情页')
#     return shortcuts.render(req, 'polls/detail.html', {'question': q})
#     pass
class DetailView(generic.DetailView):
    model = models.Question
    template_name = 'polls/detail.html'
    pass


# 问题结果页
# def results(req, question_id):
#     # return HttpResponse(f'这里是问题 {question_id} 结果页')
#     q = shortcuts.get_object_or_404(models.Question, pk=question_id)
#     return shortcuts.render(req, 'polls/results.html', {'question': q})
#     pass
class ResultsView(generic.DetailView):
    model = models.Question
    template_name = 'polls/results.html'
    pass


# 问题投票页
def vote(req, question_id):
    # return HttpResponse(f'这里问题 {question_id} 投票页')
    q = shortcuts.get_object_or_404(models.Question, pk=question_id)
    try:
        choice: models.Choice = q.choice_set.get(pk=req.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return shortcuts.render(req, 'polls/detail.html', {
            'question': q, 'error_message': '没有选择投票项'
        })
    else:
        from django.db.models import F
        choice.votes = F('votes') + 1
        choice.save()
        return shortcuts.redirect(urls.reverse('polls:results', args=(question_id,)))
    pass
