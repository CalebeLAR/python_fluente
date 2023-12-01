# Exemplo 2.11 -Itens de cada linha de um arquivo simples de fatura
invoice = """
... 0........ 6................................................................ 40...............52...55...............
... 1909        Pinoroni PiBrella                                                  $17.50           3    $52.50
... 1489        6m Tactile Switch x20                                              $4.95            2    $9.90
... 1510        Panavise 3r. - PV-201                                              $28.00           1    $28.00
... 1601        PiTFT Mini Kit 320x240                                             $34.95           1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_itens = invoice.split("\n")[2:]

for item in line_itens:
    print(item[UNIT_PRICE], item[DESCRIPTION])
