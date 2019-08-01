def checkMagazine(magazine, note):
    magazine = magazine.split(' ')
    note = note.split(' ')
    m = {}
    for i in magazine:
        try:
            m[i] += 1
        except KeyError:
            m[i] = 1
    n = {}
    for i in note:
        try:
            n[i] += 1
        except KeyError:
            n[i] = 1
    success = True
    for i in n:
        try:
            if m[i] >= n[i]:
                success = True
            else:
                success = False
                break
        except KeyError:
            success = False
            break
    if success:
        print('Yes')
    else:
        print('No')





checkMagazine('apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg', 'elo lxkvg bg mwz clm w')