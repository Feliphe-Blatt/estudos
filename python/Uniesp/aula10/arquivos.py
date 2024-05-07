nome_do_arquivo = "./arquivogdhsagdhasd.txt"


try:

    with open(f'{nome_do_arquivo}', 'r', encoding='utf-8') as arq:

        for linha in arq:

            print(f'[{len(linha.strip())}] - {linha.strip()}')

except Exception as e:

    print(f'\nErro: {e}')
