s = input()
quant_glas = 0
quant_soglas = 0
for i in range(len(s)):
    if s[i] in "АаОоУуЫыЭэЕеИиЮюЯя":
        quant_glas += 1
    if s[i] in "БбВвГгДдЖжЗзЙйКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщ":
        quant_soglas += 1
print("Количество гласных букв равно ", quant_glas)
print("Количество согласных букв равно ", quant_soglas)
