message = "this should make the same hash"
h = md5(m)
print h.hexdigest()
blob = """ 0�5L!ʠ����X"�����4B	�E�˦��~���k0?D�/
h.update(blob)
print h.hexdigest()