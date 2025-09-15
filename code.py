def sort(w,h,l,m):
    vol = w*h*l
    bulky = vol>=1000000 or w>=150 or h>=150 or l>=150
    Heavy = m>=20
    
    if bulky and Heavy:
        return "REJECTED"
    elif bulky or Heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
