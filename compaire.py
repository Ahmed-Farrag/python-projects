def names(ahmed, hassan,ali):
    if ahmed>hassan and ahmed> ali:
        return ahmed
    elif hassan>ahmed and hassan>ali:
        return hassan
    else:
        return ali
print(names(50,90,10))