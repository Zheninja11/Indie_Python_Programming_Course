if (a := int(input())) <= 10000:
    print(f"Сумма {a} не превышает лимит, проходите")
else:
    print(f"Ого! {a}! Куда вам столько? Мы заберем {a - 10000}")