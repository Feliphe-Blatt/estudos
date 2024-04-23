def converte_tempo(segundos:int) -> str:

    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    
    return f'\n-> {h}h:{m}m:{s}s\n'

seg = 72634

print(converte_tempo(seg))
