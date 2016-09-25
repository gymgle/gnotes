from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib

@csrf_exempt
def WeChat(request):
    token = 'xxx'    # 填入你的 Token

    signature = request.GET.get('signature', '')
    timestamp = request.GET.get('timestamp', '')
    nonce = request.GET.get('nonce', '')

    # 计算排序后的哈希值并比较
    tmp_sig = hashlib.sha1(''.join(sorted([token, timestamp, nonce]))).hexdigest()
    if tmp_sig == signature:
        return HttpResponse(request.GET.get('echostr', ''))

    return HttpResponse('error')
