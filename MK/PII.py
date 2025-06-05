#person imformation Masking
def mask_email(email):
    local, domain = email.split('@')
    if len(local) <= 2:
        masked_local = local[0] + '*' * (len(local)-1)
    else:
        masked_local = local[0] + '*' * (len(local)-2) + local[-1]
    return masked_local + '@' + domain




