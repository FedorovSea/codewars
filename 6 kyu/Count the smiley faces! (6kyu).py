def count_smileys(arr):
    count = 0
    smiles = [":)", ";)", ":~)", ";~)", ":-)", ";-)", ":D", ";D", ":~D", ";~D", ":-D", ";-D"]
    for word in arr:
        if word in smiles:
            count +=1
    return count