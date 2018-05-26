def maFuncCont(machaine, uneAutreChaine):
    try:
        yield machaine + " " + uneAutreChaine
        yield 2
    except StopIteration:
        print("bou de chaine")


uneChaine = iter(maFuncCont("Salut salut", "mes loulou"))
print(next(uneChaine))
print(next(uneChaine))
