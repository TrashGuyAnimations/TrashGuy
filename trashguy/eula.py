# uncompyle6 version 3.6.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.8.0 (default, Dec 14 2019, 23:51:55) 
# [GCC 7.4.0]
# Embedded file name: .\eula.py
# Compiled at: 2019-12-17 21:28:50
# Size of source mod 2**32: 1842 bytes
import json, os
EULA = '\n ┌─────────────────────────────────────────────────────────────────────────────────\n │ END-USER LICENSE AGREEMENT FOR TRASHGUY SOFTWARE\n │\n │ IMPORTANT-READ CAREFULLY: This End-User License Agreement ("EULA")\n │ is a legal agreement between you (either an individual or a single\n │ entity) and Zac (t.me/Zacci) ("The Developer") for the TrashGuy\n │ software  accompanying this EULA, which includes computer software\n │ and may include associated media, printed materials, and "on-line"\n │ or electronic documentation ("SOFTWARE PRODUCT" or "SOFTWARE").\n │ By exercising your rights to make and use copies of the SOFTWARE\n │ PRODUCT, you agree to be bound by the terms of this EULA. If you do\n │ not agree to the terms of this EULA, you may not use the SOFTWARE PRODUCT.\n └─────────────────────────────────────────────────────────────────────────────────\n'

def eula():
    data = {}
    print(EULA)
    try:
        input('<Ok>')
    except:
        pass

    data['eula-accepted'] = True
    return data


data_file = os.path.dirname(os.path.realpath(__file__)) + '\\eula.json'
data = {}
accepted = False
if os.path.isfile(data_file):
    with open(data_file, mode='r', encoding='utf8') as (efile):
        try:
            data = json.load(efile)
            accepted = bool(data['eula-accepted'])
        except:
            pass

if not accepted:
    with open(data_file, mode='w+', encoding='utf8') as (efile):
        json.dump(eula(), efile)
# okay decompiling eula.pyc
