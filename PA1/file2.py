#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """          ���HE7�	Y��Y5�M�խ#2B�n�Ŵܱ��+�}g"XśU��ݨUc���O�2s��kcsq�}K����W8�\1&r����F��ET�шKUW�x�Y�@�m��\"�� """
from hashlib import sha256
print sha256(blob).hexdigest()
