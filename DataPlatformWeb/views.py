from django.shortcuts import render
from django.template import RequestContext,loader
from django.http import HttpResponse,Http404
from .models import TbUser,TbUserContribution
from django.db import connections,connection
#
def ChangeMobile(request):
    try:
     TbUser_list = TbUser.objects.using('kawsstagedb').filter(username = 'hjghjghjghjghj')
    except TbUser.DosenotExist:
        raise Http404('user not exist')
    template = loader.get_template('dataplatform/ChangeMobile.html')
    context = RequestContext(request,{'TbUser_list':TbUser_list})
    return HttpResponse(template.render(context))
#
def ChangeMobileView(request):
    # 获取username的值
    test = request.GET['username']
    try:
        TbUser_view_list = TbUser.objects.using('kawsstagedb').filter(username=test)
    except TbUser.DosenotExist:
        raise Http404('user not exist')
    context = {'Tbuser_view_list':TbUser_view_list}
    return render(request,'dataplatform/ChangMobileView.html',context)
#
def ChangeMobileCompelet(request):
    mobilechange = request.POST['mobile_valuse']
    userkey = request.POST['userkey']
    TbUser_lists = TbUser.objects.using('kawsstagedb').get(userkey=userkey)
    TbUser_lists.mobile = mobilechange
    TbUser_lists.save()
    template = loader.get_template('dataplatform/ChangeMobileCompelet.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
#
def ChangeContribute(request):
     return render(request,'dataplatform/ChangeContribute.html')

#
def ChangeContributeview(request):
    cursor = connections['kawsstagedb'].cursor()
    getusername = request.GET['username']
    # try:
    #     TbUser_list = TbUser.objects.using('stagedb').filter(username= getusername).values()
    # except TbUser.DoseNoteExist:
    #     raise Http404('not exist')
    # for e in  TbUser_list:
    #     TbUserContribution_list = TbUserContribution.objects.using('stagedb').filter(userkey = e.get('userkey'))
    cursor.execute("SELECT DISTINCT * FROM tb_user u,tb_user_contribution c WHERE username =%s and u.userkey=c.userkey",[getusername])
    TbUserContribution_list = dictfetchall(cursor)
    context = { 'tbusercontribute_list': TbUserContribution_list}
    return render(request,'dataplatform/ChangeContributeView.html',context)

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc],row))
        for row in cursor.fetchall()
    ]
def ChangeContibuteComplete(request):
    getuserkey = request.POST['userkey']
    getcontribute = request.POST['contribute_values']
    contribute_list = TbUserContribution.objects.using('kawsstagedb').get(userkey = getuserkey)
    contribute_list.contributioinvalue = getcontribute
    contribute_list.save()
    contribute_list2 = TbUserContribution.objects.using('kawsstagedb').get(userkey = getuserkey)
    context = {'contribute_list':contribute_list2}
    return  render(request,'dataplatform/ChangeContributeCompelet.html',context)