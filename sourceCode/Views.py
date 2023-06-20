from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .script.CKY import checkSentence, main as cky
from .script.kalimat import getKal


def index(request):
    Krules, Srules, Prules, Orules, Pelrules, Ketrules, FNrules, FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules = getRules()
    cky(Krules, Srules, Prules, Orules, Pelrules, Ketrules, FNrules,
        FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules)
    return render(request, 'parse/index.html')


def validasi(request):
    Krules, Srules, Prules, Orules, Pelrules, Ketrules, FNrules, FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules = getRules()
    if(request.GET):
        sentence = request.GET['keywords']
        context = {'data': checkSentence(Krules, Srules, Prules, Orules, Pelrules, Ketrules,
                                         FNrules, FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules, sentence)}
    else:
        data, akurasi = cky(Krules, Srules, Prules, Orules, Pelrules, Ketrules,
                            FNrules, FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules)
        context = {'data': data, "akurasi": akurasi}
    return render(request, 'parse/validasi.html', context)


def getKalimat(request):
    kalimat = getKal()
    return JsonResponse({'kalimat': kalimat}, status=200)


def rules(request):
    Krules, Srules, Prules, Orules, Pelrules, Ketrules, FNrules, FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules = getRules()
    rules = {'K': Krules,
             'S': Srules,
             'P': Prules,
             'O': Orules,
             'Pel': Pelrules,
             'Ket': Ketrules,
             'FN': FNrules,
             'FV': FVrules,
             'FS': FSrules,
             'Gt': Gtrules,
             'Pn': Pnrules,
             'Ps': Psrules,
             'Pr': Prrules,
             'Kt': Ktrules}
    context = {'data': rules}
    return render(request, 'parse/rules.html', context)


def getRules():
    Krules = K.objects.values_list('rules', flat=True)
    Srules = S.objects.values_list('rules', flat=True)
    Prules = P.objects.values_list('rules', flat=True)
    Orules = O.objects.values_list('rules', flat=True)
    Pelrules = Pel.objects.values_list('rules', flat=True)
    Ketrules = Ket.objects.values_list('rules', flat=True)
    FNrules = FN.objects.values_list('rules', flat=True)
    FVrules = FV.objects.values_list('rules', flat=True)
    FSrules = FS.objects.values_list('rules', flat=True)
    Gtrules = Gt.objects.values_list('rules', flat=True)
    Pnrules = Pn.objects.values_list('rules', flat=True)
    Psrules = Ps.objects.values_list('rules', flat=True)
    Prrules = Pr.objects.values_list('rules', flat=True)
    Ktrules = Kt.objects.values_list('rules', flat=True)
    # print("K :" + str(list(Krules)))
    # print("S :" + str(list(Srules)))
    # print("P :" + str(list(Prules)))
    # print("O :" + str(list(Orules)))
    # print("Pel :" + str(list(Pelrules)))
    # print("Ket :" + str(list(Ketrules)))
    # print("FN :" + str(list(FNrules)))
    # print("FV :" + str(list(FVrules)))
    # print("Gt :" + str(list(Gtrules)))
    # print("Pn :" + str(list(Pnrules)))
    # print("Ps :" + str(list(Psrules)))
    return list(Krules), list(Srules), list(Prules), list(Orules), list(Pelrules), list(Ketrules), list(FNrules), list(FVrules), list(FSrules), list(Gtrules), list(Pnrules), list(Psrules), list(Prrules), list(Ktrules)

