#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """           GaD�^����[�iXq ���4j:�J��֝ܪ��4��B�	��L���3B=�G��L1?}HR�t_�DG����g1�}"�hZ
�� P7`h�ӓ"X���;�@LT0V�m���7t������\
"""
from hashlib import sha256
print sha256("""1020 470e 6144 9a5e 1eba d119 d2df 5bfb
1c69 58f1 00aa 84f0 346a 3ad2 4a92 a1d6
9ddc aaef d834 11fb 8b42 f61b 0926 f94c
909d c119 3342 3dac 4787 85cc 313f 7d48
52b9 7416 5fd1 4447 958f d7f2 8e67 3111
c17d 223d 685a 020a a9b3 0050 3760 68b8
d393 2258 a7c5 c13b fa40 4c54 1bb0 0f56
9e6d be92 da37 749b 11c5 1279 8ae2 cb5c
""").hexdigest()
print sha256("""1020 470e 6144 9a5e 1eba d119 d2df 5bfb
1c69 5871 00aa 84f0 346a 3ad2 4a92 a1d6
9ddc aaef d834 11fb 8b42 f61b 09a6 f84c
909d c119 3342 3dac 4787 854c 313f 7d48
52b9 7416 5fd1 4447 958f d7f2 8e67 3111
c17d 22bd 685a 020a a9b3 0050 3760 68b8
d393 2258 a7c5 c13b fa40 4c54 1b30 1056
9e6d be92 da37 749b 11c5 12f9 8ae2 cb5c
""").hexdigest()
print sha256(blob.decode('utf8')).hexdigest()
