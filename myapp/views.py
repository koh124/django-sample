from django.shortcuts import render, redirect
import json
from django.http import HttpResponse

# Create your views here.
def index(req):
  return HttpResponse('Hello, Django')

def api(req):
  print(req.GET, req.POST)
  print(req.path) # パス判別
  if (req.path == 'hoge'):
    return redirect('/admin') # リダイレクト処理
  if ('you' == 'needs json'):
    json_str = json.dumps({
      'status': 'ok'
    }, ensure_ascii=False, indent=2)
    return HttpResponse(json_str)
  return render(req, 'index.html', { 'mykey': 'myvalue' }) # テンプレート指定、viewに変数を渡す
