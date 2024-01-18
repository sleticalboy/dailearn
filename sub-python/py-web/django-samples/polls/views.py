from django import shortcuts
from django.http import HttpResponse

from . import models

# 投票首页
def index(req):
  qlist = models.Question.objects.order_by('-pub_date')[:5]
  # text_list = {it.id: it.question_text for it in qlist}
  # return HttpResponse("Hello, this is the index page of polls.")
  # return HttpResponse(json.dumps(text_list, indent=2, ensure_ascii=False))
  # tpl = template.loader.get_template('polls/index.html')
  context = {"qlist": qlist}
  return shortcuts.render(req, 'polls/index.html', context)
  pass


# 问题详情页
def details(req, question_id):
  q = shortcuts.get_object_or_404(models.Question, pk=question_id)
  # return HttpResponse(f'这里是问题 {question_id} 详情页')
  context = {'question': q}
  return shortcuts.render(req, 'polls/detail.html', context)
  pass


# 问题结果页
def results(req, question_id):
  return HttpResponse(f'这里是问题 {question_id} 结果页')
  pass


# 问题投票页
def vote(req, question_id):
  return HttpResponse(f'这里问题 {question_id} 投票页')
  pass

