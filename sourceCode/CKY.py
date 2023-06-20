import os

# RULE CNF
cnf = {

}
checkValid = ["I Bapa mamula padi di uma ituni semengan",
              "Gubernur Wayan Koster negesan indik kauratiang Desa Adat ring Bali ring pidartane",
              "Benjang pungkur Gunung Batur pastika ngerauhan bencana",
              "Tetujone nyujur Indonesia sane berdaulat",
              "Ring pemargi sejarah bangsa Indonesia",
              "Pinaka sinalih tunggil sane strategis",
              "Akeh pamikarya ring Bali sane kantos keni PHK",
              "Istri Gubernur Bali Wayan Koster punika taler",
              "Bali kaloktah ring dura Negara sangkaning kawentenan budayane",
              ]
Non_valid = 0
# FUNCTION CYK ALGORITHM


def CYK(sentence, cell, kalimat):
    global Non_valid
    for i, word in enumerate(sentence, 0):
        for j in range(i, -1, -1):
            if i is j:
                # print('sama '+str(j)+','+str(i))
                cell[j][i] = checkLexicon(word)
                if not cell[j][i]:
                    return {'validasi': 'Non-Valid', "Alasan": "tidak terdapat dalam leksikon", "kata": sentence}
            else:
                # print('beda '+str(j)+','+str(i)+' selisih : '+str(i-j))
                for k in range((i-j)):
                    # print('rumus ('+str(j)+','+str(j+k)+' , '+str(j+k+1)+','+str(i)+')')
                    if cell[j][i]:
                        cell[j][i] = list(set().union(
                            cell[j][i], checkGrammer(cell[j][j+k], cell[j+k+1][i])))
                    else:
                        cell[j][i] = checkGrammer(cell[j][j+k], cell[j+k+1][i])

    if 'K' in cell[0][(len(sentence)-1)]:
        if kalimat in checkValid:
            Non_valid = Non_valid + 1
        return {'validasi': 'Valid', "kata": sentence}
    else:
        return {'validasi': 'Non-Valid', "Alasan": "pola kalimat salah", "kata": sentence}

# FUNCTION RULE LEXICON


def checkLexicon(key):
    result = []
    for k in cnf:
        if key.lower() in [x.lower() for x in cnf[k]]:
            result.append(k)
    return result

# FUNCTION RULE GRAMMER


def checkGrammer(arr1, arr2):
    result = []
    # print(str(arr1)+' '+str(arr2))
    for i in arr1:
        for j in arr2:
            result = list(set().union(result, checkLexicon(i+' '+j)))
    return result


def cetak(arr):
    res = []
    k = -1
    for i in range(len(arr)-1, -1, -1):
        k = k + 1
        res.append([])
        for j in range(len(arr)):
            # print(arr[j][i], end="")
            res[k].append(arr[j][i])
        # print("")

    # for d in res:
    #     for j in d:
    #         print(j, end=" ")
    #     print('')

    return res


def check(sentence):
    # INPUT KEYWORD
    kalimat = sentence
    sentence = [item for item in sentence.split(' ')]
    # REMOVE EMPTY STRING IN KEYWORD
    sentence = list(filter(None, sentence))
    # ERROR IF INPUT IS EMPTY STRING
    if not sentence:
        return 'sentence tidak valid'
    else:
        # DECLARE LIST (TABLE)
        cell = [[None for i in range(len(sentence))]
                for j in range(len(sentence))]
        # RUN CYK
        return {"CYK": CYK(sentence, cell, kalimat), "cell":  cetak(cell)}


# ======================================= MAIN ========================================
# READ SENTENCE FROM TXT FILE
def main(Krules, Srules, Prules, Orules, Pelrules, Ketrules, FNrules, FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules):
    global cnf
    global Non_valid
    Non_valid = 0
    cnf = {'K': Krules,
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
    context = []
    file = "parse/script/Sentence.txt"
    if (file):
        f = open(file, "r")
        data = f.read().splitlines()
        for sentence in data:
            context.append(
                {'kalimat': sentence, 'check': check(sentence[:-1])})
        print(Non_valid)
        akurasi = (len(data) - Non_valid)/len(data) * 100
        return context, akurasi
# sentence = 'bapan tiange pilot'
# print(sentence)
# print(main(sentence))


def checkSentence(Krules, Srules, Prules, Orules, Pelrules, Ketrules, FNrules, FVrules, FSrules, Gtrules, Pnrules, Psrules, Prrules, Ktrules, sentence):
    global cnf
    cnf = {'K': Krules,
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
    context = []
    sentence = sentence.replace(".", "")
    context.append(
        {'kalimat': sentence, 'check': check(sentence)})
    return context

